import signal
import pytdbot
import asyncio

from platform import python_implementation, python_version
from os.path import join as join_path
from pathlib import Path
from getpass import getpass
from importlib import import_module

from typing import Callable, Union
from logging import getLogger, DEBUG
from base64 import b64encode
from deepdiff import DeepDiff
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread, main_thread
from json import dumps

from .tdjson import TdJson
from .handlers import Decorators, Handler
from .methods import Methods
from .types import Plugins, Result, LogStream, Update
from .filters import Filter
from .exception import StopHandlers, AuthorizationError


logger = getLogger(__name__)


class Client(Decorators, Methods):
    """Pytdbot, a TDLib client

    Args:
        api_id (``int``):
            Identifier for Telegram API access, which can be obtained at https://my.telegram.org

        api_hash (``str``):
            Identifier hash for Telegram API access, which can be obtained at https://my.telegram.org

        database_encryption_key (``str`` | ``bytes``):
            Encryption key for database encryption

        files_directory (``str``):
            Directory for storing files and database

        token (``str``, *optional*):
            Bot token or phone number

        lib_path (``str``, *optional*):
            Path to TDLib library. Default is ``None`` (auto-detect)

        plugins (:class:`~pytdbot.types.Plugins`, *optional*):
            Plugins to load

        update_class (:class:`~pytdbot.types.Update`, *optional*):
            Update class to use. Default is :class:`~pytdbot.types.Update`

        default_parse_mode (``str``, *optional*):
            The default ``parse_mode`` for methods: :meth:`~pytdbot.Client.sendTextMessage`, :meth:`~pytdbot.Client.sendPhoto`, :meth:`~pytdbot.Client.sendAudio`, :meth:`~pytdbot.Client.sendVideo`, :meth:`~pytdbot.Client.sendDocument`, :meth:`~pytdbot.Client.sendAnimation`, :meth:`~pytdbot.Client.sendVoice`, :meth:`~pytdbot.Client.sendCopy`, :meth:`~pytdbot.Client.editTextMessage`; Default is ``None`` (Don\'t parse)
            Supported values: ``markdown``, ``markdownv2``, ``html``

        system_language_code (``str``, *optional*):
            System language code. Default is ``en``

        device_model (``str``, *optional*):
            Device model. Default is ``None`` (auto-detect)

        use_test_dc (``bool``, *optional*):
            If set to true, the Telegram test environment will be used instead of the production environment. Default is ``False``

        use_file_database (``bool``, *optional*):
            If set to true, information about downloaded and uploaded files will be saved between application restarts. Default is ``True``

        use_chat_info_database (``bool``, *optional*):
            If set to true, the library will maintain a cache of users, basic groups, supergroups, channels and secret chats. Implies ``use_file_database``. Default is ``True``

        use_message_database (``bool``, *optional*):
            If set to true, the library will maintain a cache of chats and messages. Implies use_chat_info_database. Default is ``True``

        enable_storage_optimizer (``bool``, *optional*):
            If set to true, old files will automatically be deleted. Default is ``True``

        ignore_file_names (``bool``, *optional*):
            If set to true, original file names will be ignored. Otherwise, downloaded files will be saved under names as close as possible to the original name. Default is ``False``

        loop (:py:class:`asyncio.AbstractEventLoop`, *optional*):
            Event loop. Default is ``None`` (auto-detect)

        options (``dict``, *optional*):
            Pass key-value dictionary to set TDLib options. Check the list of available options at https://core.telegram.org/tdlib/options

        sleep_threshold (``int``, *optional*):
            Sleep threshold for all ``FLOOD_WAIT_X`` a.k.a ``Too Many Requests: retry after`` errors occur to this client.
            If any request is rate limited (flood waited) the client will repeat the request after sleeping the required amount of seconds returned by the error. If the ``retry after`` value is higher than ``sleep_threshold`` the error is returned. Default is ``None`` (Disabled)

        workers (``int``, *optional*):
            Number of workers to handle updates. Default is ``5``. If set to ``None``, updates will be immediately handled instead of being queued, which can impact performance.

        td_verbosity (``int``, *optional*):
            Verbosity level of TDLib. Default is ``2``

        td_log (:class:`~pytdbot.types.LogStream`, *optional*):
            Log stream. Default is ``None`` (Log to ``stdout``)
    """

    def __init__(
        self,
        api_id: int,
        api_hash: str,
        database_encryption_key: Union[str, bytes],
        files_directory: str,
        token: str = None,
        lib_path: str = None,
        plugins: Plugins = None,
        update_class: Update = Update,
        default_parse_mode: str = None,
        system_language_code: str = "en",
        device_model: str = None,
        use_test_dc: bool = False,
        use_file_database: bool = True,
        use_chat_info_database: bool = True,
        use_message_database: bool = True,
        enable_storage_optimizer: bool = True,
        ignore_file_names: bool = False,
        loop: asyncio.AbstractEventLoop = None,
        options: dict = None,
        sleep_threshold: int = None,
        workers: int = 5,
        td_verbosity: int = 2,
        td_log: LogStream = None,
    ) -> None:
        self.__api_id = api_id
        self.__api_hash = api_hash
        self.__token = token
        self.__database_encryption_key = database_encryption_key
        self.files_directory = files_directory
        self.lib_path = lib_path
        self.plugins = plugins
        self.update_class = update_class
        self.default_parse_mode = (
            default_parse_mode
            if isinstance(default_parse_mode, str)
            and default_parse_mode in {"markdown", "markdownv2", "html"}
            else None
        )
        self.system_language_code = system_language_code
        self.device_model = device_model
        self.use_test_dc = use_test_dc
        self.use_file_database = use_file_database
        self.use_chat_info_database = use_chat_info_database
        self.use_message_database = use_message_database
        self.enable_storage_optimizer = enable_storage_optimizer
        self.ignore_file_names = ignore_file_names
        self.td_options = options
        self.sleep_threshold = (
            sleep_threshold if isinstance(sleep_threshold, int) else 0
        )
        self.workers = workers
        self.queue = asyncio.Queue()
        self.td_verbosity = td_verbosity
        self.connection_state: str = None
        self.is_running = None
        self.me = None
        self.is_authenticated = False
        self.options = {}

        self._check_init_args()

        self._handlers = {"initializer": [], "finalizer": []}
        self._results = {}
        self._tdjson = TdJson(lib_path, td_verbosity)
        self._retry_after_prefex = "Too Many Requests: retry after "
        self._workers_tasks = None
        self.__authorization_state = None
        self.__authorization = None
        self.__cache = {"is_coro_filter": {}}
        self.__local_handlers = {
            "updateAuthorizationState": self.__handle_authorization_state,
            "updateMessageSendSucceeded": self.__handle_update_message_succeeded,
            "updateMessageSendFailed": self.__handle_update_message_failed,
            "updateConnectionState": self.__handle_connection_state,
            "updateOption": self.__handle_update_option,
            "updateUser": self.__handle_update_user,
        }
        self.__login = False
        self.__is_closing = False

        self.loop = (
            loop
            if isinstance(loop, asyncio.AbstractEventLoop)
            else asyncio.get_event_loop()
        )

        if plugins is not None:
            self._load_plugins()

        if isinstance(td_log, LogStream):
            self._tdjson.execute(
                {"@type": "setLogStream", "log_stream": td_log.to_dict()}
            )

    async def __aenter__(self):
        await self.start()
        await self.login()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.stop()
        except Exception:
            pass

    @property
    def authorization_state(self) -> str:
        """Current authorization state"""
        return self.__authorization_state

    async def start(self, login: bool = True) -> None:
        """Start pytdbot client

        Args:
            login (``bool``, *optional*):
                Login after start. Default is ``True``
        """
        if not self.is_running:
            logger.info("Starting pytdbot client...")

            if isinstance(self.workers, int):
                self._workers_tasks = [
                    self.loop.create_task(self._queue_update_worker())
                    for x in range(self.workers)
                ]
                self.__is_queue_worker = True

                logger.info("Started with %s workers", self.workers)
            else:
                self.__is_queue_worker = False
                logger.info("Started with unlimited updates processes")

            self.loop.create_task(self.__listen_loop())

        if login:
            await self.login()

    async def login(self) -> None:
        """Login to Telegram."""

        if self.is_authenticated:
            return

        self.__login = True

        await self.getOption("version")  # Ping TDLib to start authorization process

        while self.authorization_state != "authorizationStateReady":
            await asyncio.sleep(0.1)
            if self.authorization_state == "authorizationStateClosed":
                return

        if not self.is_running:
            return

        self.me = await self.getMe()
        if self.me.is_error:
            logger.error(f"Get me error: {self.me['message']}")

        self.me = self.me.result
        self.is_authenticated = True
        logger.info(
            "Logged in as {} {}".format(
                self.me["first_name"],
                str(self.me["id"])
                if "usernames" not in self.me
                else "@" + self.me["usernames"]["editable_username"],
            )
        )

    def add_handler(
        self,
        update_type: str,
        func: Callable,
        filters: pytdbot.filters.Filter = None,
        position: int = None,
    ) -> None:
        """Add an update handler

        Args:
            update_type (``str``):
                An update type

            func (``Callable``):
                A callable function

            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                message filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            TypeError
        """
        if not isinstance(update_type, str):
            raise TypeError("update_type must be str")
        elif not isinstance(func, Callable):
            raise TypeError("func must be callable")
        elif filters is not None and not isinstance(filters, Filter):
            raise TypeError("filters must be instance of pytdbot.filters.Filter")
        else:
            func = Handler(func, update_type, filters, position)
            if update_type not in self._handlers:
                self._handlers[update_type] = []
            if isinstance(position, int):
                self._handlers[update_type].insert(position, func)
            else:
                self._handlers[update_type].append(func)
        self._handlers[update_type].sort(key=lambda x: (x.position is None, x.position))

    def remove_handler(self, func: Callable) -> bool:
        """Remove an update handler

        Args:
            func (``Callable``):
                A callable function

        Raises:
            TypeError

        Returns:
            :py:class:`bool`: True if handler was removed, False otherwise
        """
        if not isinstance(func, Callable):
            raise TypeError("func must be callable")
        for update_type in self._handlers:
            for handler in self._handlers[update_type]:
                if handler.func == func:
                    self._handlers[update_type].remove(handler)
                    self._handlers[update_type].sort(
                        key=lambda x: (x.position is None, x.position)
                    )
                    return True
        return False

    async def invoke(
        self,
        request: dict,
    ) -> Result:
        """Invoke a new TDLib request

        Example:
            .. code-block:: python

                from pytdbot import Client

                async with Client(...) as client:
                    res = await client.invoke({"@type": "getOption", "name": "version"})
                    if not res.is_error:
                        print(res)

        Args:
            request (``dict``):
                The request to be sent

        Returns:
            :class:`~pytdbot.types.Result`
        """

        result = Result(request)
        self._results[result.id] = result

        if (
            logger.root.level >= DEBUG
        ):  # dumping all requests may create performance issues
            logger.debug(f"Sending: {dumps(result.request, indent=4)}")

        self.__send(result.request)
        await result

        if result.is_error:
            if result["code"] == 429:
                retry_after = self.get_retry_after_time(result["message"])

                if retry_after <= self.sleep_threshold:
                    result.reset()

                    logger.error(
                        f"Sleeping for {retry_after}s (Caused by {result.request['@type']})"
                    )

                    await asyncio.sleep(retry_after)
                    self._results[result.id] = result
                    self.__send(result.request)
                    await result
            elif not self.use_message_database and (
                result["code"] == 400
                and result["message"] == "Chat not found"
                and "chat_id" in result.request
            ):
                chat_id = result.request["chat_id"]

                logger.debug(f"Attempt to load chat {chat_id}")

                load_chat = await self.getChat(chat_id)

                if not load_chat.is_error:
                    logger.debug(f"Chat {chat_id} is loaded")

                    message_id = result.request.get("reply_to", {}).get(
                        "message_id", result.request.get("message_id", 0)
                    )

                    # If there is a message_id then
                    # we need to load it to avoid "Message not found"
                    if message_id > 0:
                        await self.getMessage(chat_id, message_id)

                    # repeat the first request
                    result.reset()
                    self._results[result.id] = result
                    self.__send(result.request)
                    await result
                else:
                    logger.error(f"Couldn't load chat {chat_id}")

        return result

    async def call_method(self, method: str, **kwargs) -> Result:
        """Call a method. with keyword arguments (``kwargs``) support

        Example:
            .. code-block:: python

                from pytdbot import Client

                async with Client(...) as client:
                    res = await client.call_method("getOption", name="version"})
                    if not res.is_error:
                        print(res)

        Args:
            method (``str``):
                TDLib method name

        Returns:
            :class:`~pytdbot.types.Result`
        """

        kwargs["@type"] = method

        return await self.invoke(kwargs)

    def run(self, login: bool = True) -> None:
        """Start the client and block until the client is stopped

        Example:
            .. code-block:: python

                from pytdbot import Client

                client = Client(...)

                @client.on_updateNewMessage()
                async def new_message(c,update):
                    await update.reply_text('Hello!')

                client.run()

        Args:
            login (``bool``, *optional*):
                Login after start. Default is ``True``
        """

        self._register_signal_handlers()

        self.loop.run_until_complete(self.start(login))
        self.loop.run_until_complete(self.idle())

    async def idle(self):
        """Idle and wait until the client is stopped."""

        while self.is_running:
            await asyncio.sleep(1)

    async def stop(self) -> bool:
        """Stop the client

        Raises:
            `RuntimeError`:
                If the instance is already stopped

        Returns:
            :py:class:`bool`: ``True`` on success
        """
        if (
            self.is_running is False
            and self.authorization_state == "authorizationStateClosed"
        ):
            raise RuntimeError("Instance is not running")

        logger.info("Waiting for TDLib to close...")

        self.__is_closing = True

        await self.close()

        while self.authorization_state != "authorizationStateClosed":
            await asyncio.sleep(0.1)
        else:
            self.__stop_client()

            logger.info("Instance closed")

            return True

    def __send(self, request: dict) -> None:
        return self._tdjson.send(
            request
        )  # tdjson.send is non-blocking method, So we don't need run_in_executor. This improves performance

    def _check_init_args(self):
        if not isinstance(self.__api_id, int):
            raise TypeError("api_id must be int")
        elif not isinstance(self.__api_hash, str):
            raise TypeError("api_hash must be str")
        elif not isinstance(self.__database_encryption_key, str) and not isinstance(
            self.__database_encryption_key, bytes
        ):
            raise TypeError("database_encryption_key must be str or bytes")
        elif not isinstance(self.files_directory, str):
            raise TypeError("files_directory must be str")
        elif not isinstance(self.td_verbosity, int):
            raise TypeError("td_verbosity must be int")
        elif type(Update) is not type(self.update_class):
            raise TypeError(
                "update_class must be instance of class pytdbot.types.Update"
            )

        if isinstance(self.workers, int) and self.workers < 1:
            raise ValueError("workers must be greater than 0")

    def get_retry_after_time(self, error_message: str) -> int:
        """Get the retry after time from flood wait error message

        Args:
            error_message (``str``):
                The returned error message from TDLib

        Returns:
            py:class:`int`
        """

        try:
            return int(error_message.removeprefix(self._retry_after_prefex))
        except Exception:
            return 0

    def _load_plugins(self):
        count = 0
        handlers = 0
        plugin_paths = sorted(Path(self.plugins.folder).rglob("*.py"))

        if self.plugins.include:
            plugin_paths = [
                path
                for path in plugin_paths
                if ".".join(path.parent.parts + (path.stem,)) in self.plugins.include
            ]
        elif self.plugins.exclude:
            plugin_paths = [
                path
                for path in plugin_paths
                if ".".join(path.parent.parts + (path.stem,))
                not in self.plugins.exclude
            ]

        for path in plugin_paths:
            module_path = ".".join(path.parent.parts + (path.stem,))

            try:
                module = import_module(module_path)
            except Exception:
                logger.exception(f"Failed to import plugin {module_path}")
                continue

            plugin_handlers_count = 0
            handlers_to_load = []
            handlers_to_load += [
                obj._handler
                for obj in vars(module).values()
                if hasattr(obj, "_handler")
                and isinstance(obj._handler, Handler)
                and obj._handler not in handlers_to_load
            ]

            for handler in handlers_to_load:
                if asyncio.iscoroutinefunction(handler.func):
                    self.add_handler(
                        handler.update_type,
                        handler.func,
                        handler.filter,
                        handler.position,
                    )
                    handlers += 1
                    plugin_handlers_count += 1

                    logger.debug(f"Handler {handler.func} added from {module_path}")
                else:
                    logger.warning(
                        f"Handler {handler.func} is not an async function from module {module_path}"
                    )
            count += 1

            logger.debug(
                f"Plugin {module_path} is fully imported with {plugin_handlers_count} handlers"
            )

        logger.info(f"From {count} plugins got {handlers} handlers")

    def is_coro_filter(self, func: Callable) -> bool:
        if func in self.__cache["is_coro_filter"]:
            return self.__cache["is_coro_filter"][func]
        else:
            is_coro = asyncio.iscoroutinefunction(func)
            self.__cache["is_coro_filter"][func] = is_coro
            return is_coro

    async def __listen_loop(self):
        with ThreadPoolExecutor(1, "pytdbot_listener") as thread:
            try:
                self.is_running = True
                logger.info("Listening to updates...")

                while self.is_running:
                    update = await self.loop.run_in_executor(
                        thread, self._tdjson.receive, 100000.0  # Seconds
                    )
                    if update is None:
                        continue
                    self.loop.create_task(self._process_update(update))

            except Exception:
                logger.exception("Exception in __listen_loop")
            finally:
                self.is_running = False

    async def _process_update(self, update):
        del update["@client_id"]

        if "@extra" in update:
            if (
                logger.root.level >= DEBUG
            ):  # dumping all results may create performance issues
                logger.debug(f"Received: {dumps(update, indent=4)}")
            if update["@extra"]["id"] in self._results:
                result: Result = self._results.pop(update["@extra"]["id"])
                result.set_result(update)
            elif update["@type"] == "error" and "option" in update["@extra"]:
                logger.error(f"{update['@extra']['option']}: {update['message']}")
        else:
            update_handler = self.__local_handlers.get(update["@type"])
            if update_handler:
                self.loop.create_task(update_handler(update))

            if self.__is_queue_worker:
                self.queue.put_nowait(update)
            else:
                await self._handle_update(update)

    async def __run_initializers(self, update):
        for initializer in self._handlers["initializer"]:
            try:
                if initializer.filter is not None:
                    filter_function = initializer.filter.func

                    if self.is_coro_filter(filter_function):
                        if not await filter_function(self, update):
                            continue
                    elif not filter_function(self, update):
                        continue

                await initializer(self, update)
            except StopHandlers as e:
                raise e
            except Exception:
                logger.exception(f"Initializer {initializer} failed")

    async def __run_handlers(self, update):
        update_type = update["@type"]
        for handler in self._handlers[update_type]:
            try:
                if handler.filter is not None:
                    filter_function = handler.filter.func
                    if self.is_coro_filter(filter_function):
                        if not await filter_function(self, update):
                            continue
                    elif not filter_function(self, update):
                        continue

                await handler(self, update)
            except StopHandlers as e:
                raise e
            except Exception:
                logger.exception(f"Exception in {handler}")

    async def __run_finalizers(self, update):
        for finalizer in self._handlers["finalizer"]:
            try:
                if finalizer.filter is not None:
                    filter_function = finalizer.filter.func

                    if self.is_coro_filter(filter_function):
                        if not await filter_function(self, update):
                            continue
                    elif not filter_function(self, update):
                        continue

                await finalizer(self, update)
            except StopHandlers as e:
                raise e
            except Exception:
                logger.exception(f"Finalizer {finalizer} failed")

    async def _handle_update(self, update):
        if (
            logger.root.level >= DEBUG
        ):  # dumping all updates can create performance issues
            logger.debug(
                f"Received: {dumps(update, indent=4)}",
            )

        if update["@type"] in self._handlers:
            update = self.update_class(self, update)
            if (
                update["@type"] == "updateNewMessage"
                and update["message"]["is_outgoing"]
                and "sending_state" in update["message"]
            ):
                return

            try:
                await self.__run_initializers(update)
                await self.__run_handlers(update)
            except StopHandlers:
                pass
            finally:
                await self.__run_finalizers(update)

    async def _queue_update_worker(self):
        self.is_running = True
        while self.is_running:
            try:
                await self._handle_update(await self.queue.get())
            except Exception:
                logger.exception("Got worker exception")

    async def set_td_parameters(self):
        """Make a call to :meth:`~pytdbot.Client.setTdlibParameters` with the current client init parameters

        Raises:
            `AuthorizationError`
        """
        if isinstance(self.__database_encryption_key, str):
            self.__database_encryption_key = self.__database_encryption_key.encode(
                "utf-8"
            )

        res = await self.setTdlibParameters(
            use_test_dc=self.use_test_dc,
            api_id=self.__api_id,
            api_hash=self.__api_hash,
            system_language_code=self.system_language_code,
            device_model=f"{python_implementation()} {python_version()}",
            use_file_database=self.use_file_database,
            use_chat_info_database=self.use_chat_info_database,
            use_message_database=self.use_message_database,
            use_secret_chats=False,
            system_version=None,
            enable_storage_optimizer=self.enable_storage_optimizer,
            ignore_file_names=self.ignore_file_names,
            files_directory=self.files_directory,
            database_encryption_key=b64encode(self.__database_encryption_key).decode(
                "utf-8"
            ),
            database_directory=join_path(self.files_directory, "database"),
            application_version=f"Pytdbot {pytdbot.__version__}",
        )
        if res.is_error:
            raise AuthorizationError(res.result["message"])

    async def _set_bot_token(self):
        res = await self.checkAuthenticationBotToken(self.__token)
        if res.is_error:
            raise AuthorizationError(res.result["message"])

    async def _set_options(self):
        if not isinstance(self.td_options, dict):
            return

        for k, v in self.td_options.items():
            v_type = type(v)

            if v_type is str:
                data = {"@type": "optionValueString", "value": v}
            elif v_type is int:
                data = {"@type": "optionValueInteger", "value": v}
            elif v_type is bool:
                data = {"@type": "optionValueBoolean", "value": v}
            else:
                raise ValueError(f"Option {k} has unsupported type {v_type}")

            self.__send(
                {
                    "@type": "setOption",
                    "name": k,
                    "value": data,
                    "@extra": {"option": k, "value": v, "id": ""},
                }
            )
            logger.debug(f"Option {k} sent with value {v}")

    async def __handle_authorization_state(self, update):
        if update["@type"] == "updateAuthorizationState":
            old_authorization_state = self.authorization_state
            self.__authorization_state = update["authorization_state"]["@type"]
            self.__authorization = update["authorization_state"]

            logger.info(
                f"Authorization state changed to {self.authorization_state.removeprefix('authorizationState')}"
            )

            if self.__login:
                if self.authorization_state == "authorizationStateWaitTdlibParameters":
                    await self._set_options()
                    await self.set_td_parameters()
                elif self.authorization_state == "authorizationStateWaitPhoneNumber":
                    self._print_welcome()
                    await self.__handle_authorization_state_wait_phone_number()
                elif self.authorization_state == "authorizationStateWaitEmailAddress":
                    await self.__handle_authorization_state_wait_email_address()
                elif self.authorization_state == "authorizationStateWaitEmailCode":
                    await self.__handle_authorization_state_wait_email_code()
                elif self.authorization_state == "authorizationStateWaitCode":
                    await self.__handle_authorization_state_wait_code()
                elif self.authorization_state == "authorizationStateWaitRegistration":
                    await self.__handle_authorization_state_wait_registration()
                elif (
                    old_authorization_state != "authorizationStateWaitPassword"
                    and self.authorization_state == "authorizationStateWaitPassword"
                ):
                    await self.__handle_authorization_state_wait_password()
                elif (
                    self.authorization_state == "authorizationStateClosed"
                    and self.__is_closing is False
                ):
                    self.__stop_client()

    async def __handle_connection_state(self, update):
        if update["@type"] == "updateConnectionState":
            self.connection_state: str = update["state"]["@type"]
            logger.info(
                f"Connection state changed to {self.connection_state.removeprefix('connectionState')}"
            )

    async def __handle_update_message_succeeded(self, update):
        m_id = f'{update["old_message_id"]}{update["message"]["chat_id"]}'

        if m_id in self._results:
            result: Result = self._results.pop(m_id)
            result.set_result(update["message"])

    async def __handle_update_message_failed(self, update):
        m_id = f'{update["old_message_id"]}{update["message"]["chat_id"]}'

        if m_id in self._results:
            if update["error"]["code"] == 429:
                retry_after = update["message"]["sending_state"]["retry_after"]

                if retry_after <= self.sleep_threshold:
                    result: Result = self._results.pop(m_id)

                    logger.error(
                        f"Sleeping for {retry_after}s (Caused by {result.request['@type']})"
                    )

                    await asyncio.sleep(retry_after)
                    res = await self.invoke(result.request)

                    self._results[
                        f'{res.result["id"]}{update["message"]["chat_id"]}'
                    ] = result
            else:
                result: Result = self._results.pop(m_id)
                result.set_result(update["error"])

    async def __handle_update_option(self, update):
        if update["value"]["@type"] == "optionValueBoolean":
            self.options[update["name"]] = bool(update["value"]["value"])
        elif update["value"]["@type"] == "optionValueEmpty":
            self.options[update["name"]] = None
        elif update["value"]["@type"] == "optionValueInteger":
            self.options[update["name"]] = int(update["value"]["value"])
        else:
            self.options[update["name"]] = update["value"]["value"]

        if self.is_authenticated:
            logger.info(
                f"Option {update['name']} changed to {self.options[update['name']]}"
            )

    async def __handle_update_user(self, update):
        if self.is_authenticated and update["user"]["id"] == self.me["id"]:
            logger.info(
                "Updating {} ({}) info".format(
                    self.me["first_name"],
                    str(self.me["id"])
                    if "usernames" not in self.me
                    else "@" + self.me["usernames"]["editable_username"],
                )
            )
            try:
                deepdiff(self.me, update["user"])
            except Exception:
                logger.exception("deepdiff failed")
            self.me = update["user"]

    async def __handle_authorization_state_wait_phone_number(self):
        if self.authorization_state != "authorizationStateWaitPhoneNumber":
            return

        if not isinstance(self.__token, str):
            while self.is_running:
                user_input = await self.__ainput("Enter a phone number or bot token: ")

                if user_input:
                    y_n = await self.__ainput(f'Is "{user_input}" correct? (y/n): ')

                    if y_n == "" or y_n.lower() in {"y", "yes"}:
                        if ":" in user_input:
                            res = await self.checkAuthenticationBotToken(user_input)
                        else:
                            res = await self.setAuthenticationPhoneNumber(user_input)

                        if res.is_error:
                            print(res["message"])
                        else:
                            break
        else:
            if ":" in self.__token:
                res = await self.checkAuthenticationBotToken(self.__token)
            else:
                res = await self.setAuthenticationPhoneNumber(self.__token)

            if res.is_error:
                raise AuthorizationError(res["message"])

    async def __handle_authorization_state_wait_email_address(self):
        if self.authorization_state == "authorizationStateWaitEmailAddress":
            return

        while self.is_running:
            email_address = await self.__ainput("Enter your email address: ")

            res = await self.setAuthenticationEmailAddress(email_address)
            if res.is_error:
                print(res["message"])
            else:
                break

    async def __handle_authorization_state_wait_email_code(self):
        if self.authorization_state != "authorizationStateWaitEmailCode":
            return

        while self.is_running:
            code = await self.__ainput(
                "Enter the email authentication code you received: ",
            )

            res = await self.checkAuthenticationEmailCode(
                code={"@type": "emailAddressAuthenticationCode", "code": code}
            )
            if res.is_error:
                print(res["message"])
            else:
                break

    async def __handle_authorization_state_wait_code(self):
        if self.authorization_state != "authorizationStateWaitCode":
            return

        code_type = self.__authorization["code_info"]["type"]["@type"]

        if code_type == "authenticationCodeTypeTelegramMessage":
            code_type = "Telegram app"
        elif code_type == "authenticationCodeTypeSms":
            code_type = "SMS"
        elif code_type == "authenticationCodeTypeCall":
            code_type = "phone call"
        elif code_type == "authenticationCodeTypeFlashCall":
            code_type = "phone flush call"
        elif code_type == "authenticationCodeTypeMissedCall":
            code_type = "phone missed call"
        elif code_type == "authenticationCodeTypeFragment":
            code_type = "fragment.com SMS"

        while self.is_running:
            code = await self.__ainput(
                f"Enter the login code received via {code_type}: "
            )

            res = await self.checkAuthenticationCode(code=code)
            if res.is_error:
                print(res["message"])
            else:
                break

    async def __handle_authorization_state_wait_registration(self):
        if self.authorization_state != "authorizationStateWaitRegistration":
            return

        while self.is_running:
            first_name = await self.__ainput("Enter your first name: ")
            last_name = await self.__ainput("Enter your last name: ")

            res = await self.registerUser(first_name=first_name, last_name=last_name)
            if res.is_error:
                print(res["message"])
            else:
                break

    async def __handle_authorization_state_wait_password(self):
        if self.authorization_state != "authorizationStateWaitPassword":
            return

        if self.__authorization["password_hint"]:
            print(f"Your 2FA password hint is: {self.__authorization['password_hint']}")

        while self.is_running:
            password = await asyncio.to_thread(
                getpass,
                "Enter your 2FA password {}: ".format(
                    "(empty to recover)"
                    if self.__authorization["has_recovery_email_address"]
                    else ""
                ),
            )

            if password == "":
                if self.__authorization["has_recovery_email_address"]:
                    y_n = await self.__ainput(
                        "Are you sure you want to recover your 2FA password? (y/n): ",
                    )

                    if y_n.lower() in {"y", "yes"}:
                        res = await self.requestAuthenticationPasswordRecovery()

                        if res.is_error:
                            raise AuthorizationError(res["message"])
                        else:
                            while True:
                                recovery_code = await self.__ainput(
                                    f"Enter your recovery code sent to {self.__authorization['recovery_email_address_pattern']}: "
                                )

                                res = (
                                    await self.checkAuthenticationPasswordRecoveryCode(
                                        recovery_code
                                    )
                                )

                                if res.is_error:
                                    print(res["message"])
                                else:
                                    recover_res = (
                                        await self.recoverAuthenticationPassword(
                                            recovery_code
                                        )
                                    )
                                    if recover_res.is_error:
                                        raise AuthorizationError(recover_res["message"])

                                    return
                else:
                    print(
                        "You can't recover your 2FA password because you don't set any recovery email address"
                    )
            else:
                res = await self.checkAuthenticationPassword(password)
                if res.is_error:
                    print(res["message"])
                else:
                    break

    def __stop_client(self) -> None:
        self.is_authenticated = False
        self.is_running = False

        if self.__is_queue_worker:
            for worker_task in self._workers_tasks:
                worker_task.cancel()

    def _register_signal_handlers(self):
        def _handle_signal():
            self.loop.create_task(self.stop())
            for sig in {
                signal.SIGINT,
                signal.SIGTERM,
                signal.SIGABRT,
                signal.SIGSEGV,
            }:
                self.loop.remove_signal_handler(sig)

        if current_thread() is main_thread():
            try:
                for sig in {
                    signal.SIGINT,
                    signal.SIGTERM,
                    signal.SIGABRT,
                    signal.SIGSEGV,
                }:
                    self.loop.add_signal_handler(sig, _handle_signal)
            except NotImplementedError:  # Windows dosen't support add_signal_handler
                pass

    def __ainput(self, prompt: str):
        return asyncio.to_thread(input, prompt)

    def _print_welcome(self):
        print(f"Welcome to Pytdbot (v{pytdbot.__version__}). {pytdbot.__copyright__}")
        print(
            f"Pytdbot is free software and comes with ABSOLUTELY NO WARRANTY. Licensed under the terms of {pytdbot.__license__}.\n\n"
        )


def deepdiff(d1, d2):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        return d1 == d2

    deep = DeepDiff(d1, d2, ignore_order=True, view="tree")

    for parent in deep.keys():
        for diff in deep[parent]:
            difflist = diff.path(output_format="list")
            key = ".".join(str(v) for v in difflist)

            if parent in {"dictionary_item_added", "values_changed"}:
                logger.info(f"{key} changed to {diff.t2}")
            elif parent == "dictionary_item_removed":
                logger.info(f"{key} removed")
