import asyncio
import signal
from importlib import import_module
from json import dumps
from logging import DEBUG, getLogger
from os.path import join as join_path
from pathlib import Path
from platform import python_implementation, python_version
from threading import current_thread, main_thread
from typing import Callable, Dict, Union

import aio_pika
from deepdiff import DeepDiff

import pytdbot

from . import types
from .client_manager import ClientManager
from .exception import AuthorizationError, StopHandlers
from .filters import Filter
from .handlers import Decorators, Handler
from .methods import Methods
from .types import LogStream, Plugins
from .utils import (
    create_extra_id,
    dict_to_obj,
    get_bot_id_from_token,
    get_running_loop,
    json_dumps,
    json_loads,
    obj_to_dict,
)


class Client(Decorators, Methods):
    r"""Pytdbot, a TDLib client

    Parameters:
        token (``str``, *optional*):
            Bot token

        api_id (``int``, *optional*):
            Identifier for Telegram API access, which can be obtained at https://my.telegram.org

        api_hash (``str``, *optional*):
            Identifier hash for Telegram API access, which can be obtained at https://my.telegram.org

        rabbitmq_url (``str``, *optional*):
            URL for RabbitMQ server connection

        instance_id (``str``, *optional*):
            Instance ID for RabbitMQ connections and queues. Default is ``None`` (random)

        lib_path (``str``, *optional*):
            Path to TDLib library. Default is ``None`` (auto-detect)

        plugins (:class:`~pytdbot.types.Plugins`, *optional*):
            Plugins to load

        default_parse_mode (``str``, *optional*):
            The default ``parse_mode`` for methods: :meth:`~pytdbot.Client.sendTextMessage`, :meth:`~pytdbot.Client.sendPhoto`, :meth:`~pytdbot.Client.sendAudio`, :meth:`~pytdbot.Client.sendVideo`, :meth:`~pytdbot.Client.sendDocument`, :meth:`~pytdbot.Client.sendAnimation`, :meth:`~pytdbot.Client.sendVoice`, :meth:`~pytdbot.Client.sendCopy`, :meth:`~pytdbot.Client.editTextMessage`; Default is ``None`` (Don\'t parse)
            Supported values: ``markdown``, ``markdownv2``, ``html``

        system_language_code (``str``, *optional*):
            System language code. Default is ``en``

        device_model (``str``, *optional*):
            Device model. Default is ``None`` (auto-detect)

        files_directory (``str``, *optional*):
            Directory for storing files and database

        database_encryption_key (``str`` | ``bytes``):
            Encryption key for database encryption

        use_test_dc (``bool``, *optional*):
            If set to true, the Telegram test environment will be used instead of the production environment. Default is ``False``

        use_file_database (``bool``, *optional*):
            If set to true, information about downloaded and uploaded files will be saved between application restarts. Default is ``True``

        use_chat_info_database (``bool``, *optional*):
            If set to true, the library will maintain a cache of users, basic groups, supergroups, channels and secret chats. Implies ``use_file_database``. Default is ``True``

        use_message_database (``bool``, *optional*):
            If set to true, the library will maintain a cache of chats and messages. Implies use_chat_info_database. Default is ``True``

        loop (:py:class:`asyncio.AbstractEventLoop`, *optional*):
            Event loop. Default is ``None`` (auto-detect)

        options (``dict``, *optional*):
            Pass key-value dictionary to set TDLib options. Check the list of available options at https://core.telegram.org/tdlib/options

        workers (``int``, *optional*):
            Number of workers to handle updates. Default is ``5``. If set to ``None``, updates will be immediately handled instead of being queued, which can impact performance.

        no_updates (``bool``, *optional*):
            Whether the client should handle updates or not. Applicable only when using [TDLib Server](https://github.com/pytdbot/tdlib-server). Default is ``False``

        td_verbosity (``int``, *optional*):
            Verbosity level of TDLib. Default is ``2``

        td_log (:class:`~pytdbot.types.LogStream`, *optional*):
            Log stream. Default is ``None`` (Log to ``stdout``)
    """

    def __init__(
        self,
        token: str = None,
        api_id: int = None,
        api_hash: str = None,
        rabbitmq_url: str = None,
        instance_id: str = None,
        lib_path: str = None,
        plugins: Plugins = None,
        default_parse_mode: str = None,
        system_language_code: str = "en",
        device_model: str = None,
        files_directory: str = None,
        database_encryption_key: Union[str, bytes] = None,
        use_test_dc: bool = False,
        use_file_database: bool = True,
        use_chat_info_database: bool = True,
        use_message_database: bool = True,
        loop: asyncio.AbstractEventLoop = None,
        options: dict = None,
        workers: int = 5,
        no_updates: bool = False,
        td_verbosity: int = 2,
        td_log: LogStream = None,
        user_bot: bool = False,
    ) -> None:
        self.__api_id = api_id
        self.__api_hash = api_hash
        self.__rabbitmq_url = rabbitmq_url
        self._rabbitmq_instance_id = (
            instance_id if isinstance(instance_id, str) else create_extra_id(4)
        )
        self.__token = token
        self.__database_encryption_key = database_encryption_key
        self.files_directory = files_directory
        self.lib_path = lib_path
        self.plugins = plugins
        self.default_parse_mode = (
            default_parse_mode
            if isinstance(default_parse_mode, str)
            and default_parse_mode.lower() in {"markdown", "markdownv2", "html"}
            else None
        )
        self.system_language_code = system_language_code
        self.device_model = device_model
        self.use_test_dc = use_test_dc
        self.use_file_database = use_file_database
        self.use_chat_info_database = use_chat_info_database
        self.use_message_database = use_message_database
        self.td_options = options
        self.workers = workers
        self.no_updates = no_updates
        self.queue = asyncio.Queue()
        self.user_bot = user_bot
        self.my_id = (
            get_bot_id_from_token(self.__token)
            if isinstance(self.__token, str)
            else None
        )
        self.client_id = None
        self.client_manager = None
        self.logger = getLogger(f"{__name__}:{self.my_id or 0}")
        self.td_verbosity = td_verbosity
        self.td_log = td_log
        self.connection_state: str = None
        self.is_running = None
        self.me: types.User = None
        self.is_authenticated = False
        self.is_rabbitmq = True if rabbitmq_url else False
        self.options = {}

        self._check_init_args()

        self._handlers = {"initializer": [], "finalizer": []}
        self._results: Dict[str, asyncio.Future] = {}
        self._workers_tasks = None
        self.__authorization_state = None
        self.__cache = {"is_coro_filter": {}}
        self.__local_handlers = {
            "updateAuthorizationState": self.__handle_authorization_state,
            "updateMessageSendSucceeded": self.__handle_update_message_succeeded,
            "updateMessageSendFailed": self.__handle_update_message_failed,
            "updateConnectionState": self.__handle_connection_state,
            "updateOption": self.__handle_update_option,
            "updateUser": self.__handle_update_user,
        }
        self.__is_queue_worker = False
        self.__is_closing = False

        # RabbitMQ
        self.__rqueues = None
        self.__rconnection = None
        self.__rchannel = None

        self.loop = (
            loop if isinstance(loop, asyncio.AbstractEventLoop) else get_running_loop()
        )

        if plugins is not None:
            self._load_plugins()

        self.logger.info(f"Pytdbot v{pytdbot.VERSION}")

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.stop()
        except Exception:
            pass

    @property
    def authorization_state(self) -> str:
        r"""Current authorization state"""

        return self.__authorization_state

    async def start(self) -> None:
        r"""Start pytdbot client"""

        if not self.is_running:
            self.logger.info("Starting pytdbot client...")

            if not self.client_manager:
                self.client_manager = ClientManager(
                    self, self.lib_path, self.td_verbosity, loop=self.loop
                )
                await self.client_manager.start()

            if isinstance(self.td_log, LogStream) and not self.is_rabbitmq:
                await self.__send(
                    {"@type": "setLogStream", "log_stream": obj_to_dict(self.td_log)}
                )

            if isinstance(self.workers, int):
                self._workers_tasks = [
                    self.loop.create_task(self._queue_update_worker())
                    for _ in range(self.workers)
                ]
                self.__is_queue_worker = True

                self.logger.info(f"Started with {self.workers} workers")
            else:
                self.__is_queue_worker = False
                self.logger.info("Started with unlimited updates processes")

            if self.is_rabbitmq:
                await self.__start_rabbitmq()
            else:  # client_manager
                self.is_running = True

        self.loop.create_task(
            self.getOption("version")
        )  # Ping TDLib to start processing updates

    def add_handler(
        self,
        update_type: str,
        func: Callable,
        filters: pytdbot.filters.Filter = None,
        position: int = None,
        inner_object: bool = False,
    ) -> None:
        r"""Add an update handler

        Parameters:
            update_type (``str``):
                An update type

            func (``Callable``):
                A callable function

            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                message filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            inner_object (``bool``, *optional*):
                Wether to pass an inner object of update or not; for example ``UpdateNewMessage.message``. Default is ``False``

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
            func = Handler(func, update_type, filters, position, inner_object)
            if update_type not in self._handlers:
                self._handlers[update_type] = []
            if isinstance(position, int):
                self._handlers[update_type].insert(position, func)
            else:
                self._handlers[update_type].append(func)
        self._handlers[update_type].sort(key=lambda x: (x.position is None, x.position))

    def remove_handler(self, func: Callable) -> bool:
        r"""Remove an update handler

        Parameters:
            func (``Callable``):
                A callable function

        Raises:
            TypeError

        Returns:
            :py:class:`bool`: True if handler was removed, False otherwise
        """

        if not isinstance(func, Callable):
            raise TypeError("func must be callable")
        for _, handlers in self._handlers.items():
            for handler in handlers.copy():
                if handler.func == func:
                    handlers.remove(handler)
                    handlers.sort(key=lambda x: (x.position is None, x.position))
                    return True
        return False

    async def invoke(
        self,
        request: dict,
    ) -> types.TlObject:
        r"""Invoke a new TDLib request

        Example:
            .. code-block:: python

                from pytdbot import Client

                async with Client(...) as client:
                    res = await client.invoke({"@type": "getOption", "name": "version"})
                    if not isinstance(res, types.Error):
                        print(res)

        Parameters:
            request (``dict``):
                The request to be sent

        Returns:
            :class:`~pytdbot.types.Result`
        """

        request = obj_to_dict(request)

        request["@extra"] = {"id": create_extra_id()}

        future = self._create_request_future(request)

        if (
            self.logger.root.level >= DEBUG or self.logger.level >= DEBUG
        ):  # dumping all requests may create performance issues
            self.logger.debug(f"Sending: {dumps(request, indent=4)}")

        is_chat_attempted_load = request["@type"].lower() == "getchat"

        while True:
            future = self._create_request_future(request)
            await self.__send(request)
            result = await future

            if isinstance(result, types.Error):
                if result.code == 400:
                    if result.message.startswith(
                        "Failed to parse JSON object as TDLib request:"
                    ):
                        raise ValueError(result.message)

                    if not is_chat_attempted_load and (
                        result.message == "Chat not found" and "chat_id" in request
                    ):
                        is_chat_attempted_load = True

                        chat_id = request["chat_id"]

                        self.logger.debug(f"Attempt to load chat {chat_id}")

                        load_chat = await self.getChat(chat_id)

                        if not isinstance(load_chat, types.Error):
                            self.logger.debug(f"Chat {chat_id} is loaded")

                            reply_to_message_id = (request.get("reply_to") or {}).get(
                                "message_id", 0
                            )

                            # if the request is a reply to another message
                            # load the replied message to avoid "Message not found"
                            if reply_to_message_id > 0:
                                await self.getMessage(chat_id, reply_to_message_id)

                            continue

                        self.logger.error(f"Couldn't load chat {chat_id}")

            break

        return result

    async def call_method(self, method: str, **kwargs) -> types.TlObject:
        r"""Call a method. with keyword arguments (``kwargs``) support

        Example:
            .. code-block:: python

                from pytdbot import Client

                async with Client(...) as client:
                    res = await client.call_method("getOption", name="version"})
                    if not isinstance(res, types.Error):
                        print(res)

        Parameters:
            method (``str``):
                TDLib method name

        Returns:
            Any :class:`~pytdbot.types.TlObject`
        """

        kwargs["@type"] = method

        return await self.invoke(kwargs)

    def run(self) -> None:
        r"""Start the client and block until the client is stopped

        Example:
            .. code-block:: python

                from pytdbot import Client

                client = Client(...)

                @client.on_updateNewMessage()
                async def new_message(c,update):
                    await update.reply_text('Hello!')

                client.run()
        """

        self._register_signal_handlers()

        self.loop.run_until_complete(self.start())
        self.loop.run_until_complete(self.idle())

    async def idle(self):
        r"""Idle and wait until the client is stopped."""

        while self.is_running:
            await asyncio.sleep(1)

    async def stop(self) -> bool:
        r"""Stop the client

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

        self.logger.info("Waiting for TDLib to close...")

        self.__is_closing = True

        if self.authorization_state not in {
            "authorizationStateClosing",
            "authorizationStateClosed",
        }:
            await self.close()

        while self.authorization_state != "authorizationStateClosed":
            await asyncio.sleep(0.1)

        if self.is_rabbitmq:
            await self.__rchannel.close()
            await self.__rconnection.close()

        self.__stop_client()

        if not self.client_manager.start_clients_on_add:
            await self.client_manager.close()

        self.logger.info("Instance closed")

        return True

    def _create_request_future(
        self, request: dict, result_id: str = None, handle_result: bool = True
    ) -> asyncio.Future:
        result = asyncio.Future()

        result.request = request

        if handle_result:
            self._results[
                result_id if result_id is not None else request["@extra"]["id"]
            ] = result
        return result

    async def __send(self, request: dict) -> None:
        if self.is_rabbitmq:
            await self.__rchannel.default_exchange.publish(
                aio_pika.Message(
                    json_dumps(request, encode=True),
                    reply_to=self.__rqueues["responses"].name,
                ),
                routing_key=self.__rqueues["requests"].name,
            )
        else:
            self.client_manager.send(self.client_id, request)

    def _check_init_args(self):
        if self.user_bot:
            return

        if not self.is_rabbitmq:
            if not isinstance(self.__api_id, int):
                raise TypeError("api_id must be an int")
            if not isinstance(self.__api_hash, str):
                raise TypeError("api_hash must be a str")
            if not isinstance(self.__database_encryption_key, (str, bytes)):
                raise TypeError("database_encryption_key must be str or bytes")
            if not isinstance(self.files_directory, str):
                raise TypeError("files_directory must be a str")
            if not isinstance(self.td_verbosity, int):
                raise TypeError("td_verbosity must be an int")

        if self.__token and not self.my_id:
            raise ValueError("Invalid bot token")

        if isinstance(self.workers, int) and self.workers < 1:
            raise ValueError("workers must be greater than 0")

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
                self.logger.exception(f"Failed to import plugin {module_path}")
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
                        handler.inner_object,
                    )
                    handlers += 1
                    plugin_handlers_count += 1

                    self.logger.debug(
                        f"Handler {handler.func} added from {module_path}"
                    )
                else:
                    self.logger.warning(
                        f"Handler {handler.func} is not an async function from module {module_path}"
                    )
            count += 1

            self.logger.debug(
                f"Plugin {module_path} is fully imported with {plugin_handlers_count} handlers"
            )

        self.logger.info(f"From {count} plugins got {handlers} handlers")

    def is_coro_filter(self, func: Callable) -> bool:
        if func in self.__cache["is_coro_filter"]:
            return self.__cache["is_coro_filter"][func]
        else:
            is_coro = asyncio.iscoroutinefunction(func)
            self.__cache["is_coro_filter"][func] = is_coro
            return is_coro

    async def process_update(self, update):
        if not update:
            self.logger.warning("Received None update")
            return

        if (
            self.logger.root.level >= DEBUG or self.logger.level >= DEBUG
        ):  # dumping all results may create performance issues
            self.logger.debug(f"Received: {dumps(update, indent=4)}")

        if "@extra" in update:
            if result := self._results.pop(update["@extra"]["id"], None):
                obj = dict_to_obj(update, self)

                result.set_result(obj)
            elif update["@type"] == "error" and "option" in update["@extra"]:
                self.logger.error(f"{update['@extra']['option']}: {update['message']}")

        else:
            update_handler = self.__local_handlers.get(update["@type"])
            update = dict_to_obj(update, self)

            if update_handler:
                self.loop.create_task(update_handler(update))

            if self.__is_queue_worker:
                self.queue.put_nowait(update)
            else:
                await self._handle_update(update)

    def get_inner_object(self, update: types.TlObject):
        if isinstance(update, types.UpdateNewMessage):
            return update.message
        return update

    async def __run_initializers(self, update):
        inner_object = self.get_inner_object(update)

        for initializer in self._handlers["initializer"]:
            try:
                handler_value = inner_object if initializer.inner_object else update

                if initializer.filter is not None:
                    filter_function = initializer.filter.func

                    if self.is_coro_filter(filter_function):
                        if not await filter_function(self, handler_value):
                            continue
                    elif not filter_function(self, handler_value):
                        continue

                await initializer(self, handler_value)
            except StopHandlers as e:
                raise e
            except Exception:
                self.logger.exception(f"Initializer {initializer} failed")

    async def __run_handlers(self, update):
        inner_object = self.get_inner_object(update)

        for handler in self._handlers[update.getType()]:
            try:
                handler_value = inner_object if handler.inner_object else update

                if handler.filter is not None:
                    filter_function = handler.filter.func
                    if self.is_coro_filter(filter_function):
                        if not await filter_function(self, handler_value):
                            continue
                    elif not filter_function(self, handler_value):
                        continue

                await handler(self, handler_value)
            except StopHandlers as e:
                raise e
            except Exception:
                self.logger.exception(f"Exception in {handler}")

    async def __run_finalizers(self, update):
        inner_object = self.get_inner_object(update)

        for finalizer in self._handlers["finalizer"]:
            try:
                handler_value = inner_object if finalizer.inner_object else update

                if finalizer.filter is not None:
                    filter_function = finalizer.filter.func

                    if self.is_coro_filter(filter_function):
                        if not await filter_function(self, handler_value):
                            continue
                    elif not filter_function(self, handler_value):
                        continue

                await finalizer(self, handler_value)
            except StopHandlers as e:
                raise e
            except Exception:
                self.logger.exception(f"Finalizer {finalizer} failed")

    async def _handle_update(self, update):
        if update.getType() in self._handlers:
            if (
                not self.user_bot
                and isinstance(update, types.UpdateNewMessage)
                and update.message.is_outgoing
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
                self.logger.exception("Got worker exception")

    async def set_td_parameters(self):
        r"""Make a call to :meth:`~pytdbot.Client.setTdlibParameters` with the current client init parameters

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
            files_directory=self.files_directory,
            database_encryption_key=self.__database_encryption_key,
            database_directory=join_path(self.files_directory, "database"),
            application_version=f"Pytdbot {pytdbot.__version__}",
        )
        if isinstance(res, types.Error):
            await self.stop()
            raise AuthorizationError(res.message)

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

            await self.__send(
                {
                    "@type": "setOption",
                    "name": k,
                    "value": data,
                    "@extra": {"option": k, "value": v, "id": ""},
                }
            )
            self.logger.debug(f"Option {k} sent with value {v}")

    async def __handle_authorization_state(
        self, update: types.UpdateAuthorizationState
    ):
        self.__authorization_state = update.authorization_state.getType()

        self.logger.info(
            f"Authorization state changed to {self.authorization_state.removeprefix('authorizationState')}"
        )

        if self.authorization_state == "authorizationStateWaitTdlibParameters":
            await self._set_options()
            await self.set_td_parameters()
        elif self.authorization_state == "authorizationStateWaitPhoneNumber":
            self._print_welcome()
            await self.__handle_authorization_state_wait_phone_number()
        elif self.authorization_state == "authorizationStateReady":
            self.is_authenticated = True

            self.me = await self.getMe()
            if isinstance(self.me, types.Error):
                self.logger.error(f"Get me error: {self.me.message}")

            self.logger.info(
                f"Logged in as {self.me.first_name} "
                f"{str(self.me.id) if not self.me.usernames else '@' + self.me.usernames.editable_username}"
            )

        if (
            self.authorization_state == "authorizationStateClosed"
            and self.__is_closing is False
        ):
            await self.stop()

    async def __handle_connection_state(self, update: types.UpdateConnectionState):
        self.connection_state: str = update.state.getType()
        self.logger.info(
            f"Connection state changed to {self.connection_state.removeprefix('connectionState')}"
        )

    async def __handle_update_message_succeeded(
        self, update: types.UpdateMessageSendSucceeded
    ):
        m_id = f"{update.message.chat_id}:{update.old_message_id}"

        if result := self._results.pop(m_id, None):
            result.set_result(update.message)

    async def __handle_update_message_failed(
        self, update: types.UpdateMessageSendFailed
    ):
        m_id = f"{update.message.chat_id}:{update.old_message_id}"

        if result := self._results.pop(m_id, None):
            result.set_result(update.error)

    async def __handle_update_option(self, update: types.UpdateOption):
        if isinstance(update.value, types.OptionValueBoolean):
            self.options[update.name] = bool(update.value.value)
        elif isinstance(update.value, types.OptionValueEmpty):
            self.options[update.name] = None
        elif isinstance(update.value, types.OptionValueInteger):
            self.options[update.name] = int(update.value.value)
        else:
            self.options[update.name] = update.value.value

        if update.name == "my_id":
            self.my_id = str(update.value.value)

        if self.is_authenticated:
            self.logger.info(
                f"Option {update.name} changed to {self.options[update.name]}"
            )

    async def __get_updates_queue(self, retries=10, delay=2):
        for attempt in range(retries):
            try:
                return await self.__rchannel.get_queue(self.my_id + "_updates")
            except aio_pika.exceptions.ChannelNotFoundEntity:
                self.logger.warning(
                    f"Attempt {attempt + 1}: TDLib Server is not running. Retrying in {delay} seconds..."
                )
                await asyncio.sleep(delay)
        self.logger.error(
            f"Could not connect to TDLib Server after {retries} attempts."
        )
        raise AuthorizationError(
            f"Could not connect to TDLib Server after {delay * retries} seconds timeout"
        )

    async def __start_rabbitmq(self):
        self.__rconnection = await aio_pika.connect_robust(
            self.__rabbitmq_url,
            client_properties={
                "connection_name": f"Pytdbot instance {self._rabbitmq_instance_id}"
            },
        )
        self.__rchannel = await self.__rconnection.channel()

        updates_queue = await self.__get_updates_queue()

        notify_queue = await self.__rchannel.declare_queue(
            f"notify_{self._rabbitmq_instance_id}", exclusive=True
        )
        await notify_queue.bind(await self.__rchannel.get_exchange("broadcast"))

        responses_queue = await self.__rchannel.declare_queue(
            f"res_{self._rabbitmq_instance_id}", exclusive=True
        )

        self.__rqueues = {
            "updates": updates_queue,
            "requests": await self.__rchannel.get_queue(self.my_id + "_requests"),
            "notify": notify_queue,
            "responses": responses_queue,
        }

        self.is_running = True

        await self.__rqueues["responses"].consume(self.__on_update, no_ack=True)

        await self._set_options()

        res = await self.getCurrentState()
        for update in res.updates:
            # when using obj_to_dict the key "@client_id" won't exists
            # since it's not part of the object
            await self.process_update(obj_to_dict(update))

        if not self.no_updates:
            await self.__rqueues["updates"].consume(self.__on_update, no_ack=True)

        await self.__rqueues["notify"].consume(self.__on_update, no_ack=True)

    async def __handle_rabbitmq_message(self, message: aio_pika.IncomingMessage):
        await self.process_update(json_loads(message.body))

    async def __on_update(self, update):
        self.loop.create_task(self.__handle_rabbitmq_message(update))

    async def __handle_update_user(self, update: types.UpdateUser):
        if self.is_authenticated and update.user.id == self.me.id:
            self.logger.info(
                f"Updating {self.me.first_name} "
                f"({str(self.me.id) if not self.me.usernames else '@' + self.me.usernames.editable_username}) info"
            )

            try:
                deepdiff(self, obj_to_dict(self.me), obj_to_dict(update.user))
            except Exception:
                self.logger.exception("deepdiff failed")
            self.me = update.user

    async def __handle_authorization_state_wait_phone_number(self):
        if (
            self.authorization_state != "authorizationStateWaitPhoneNumber"
            or not self.__token
        ):
            return

        res = await self.checkAuthenticationBotToken(self.__token)

        if isinstance(res, types.Error):
            await self.stop()
            raise AuthorizationError(res.message)

    def __stop_client(self) -> None:
        self.is_authenticated = False
        self.is_running = False

        if self.__is_queue_worker:
            for worker_task in self._workers_tasks:
                worker_task.cancel()

    def _register_signal_handlers(self):
        def _handle_signal():
            self.loop.create_task(self.stop())
            for sig in (
                signal.SIGINT,
                signal.SIGTERM,
                signal.SIGABRT,
                signal.SIGSEGV,
            ):
                self.loop.remove_signal_handler(sig)

        if current_thread() is main_thread():
            try:
                for sig in (
                    signal.SIGINT,
                    signal.SIGTERM,
                    signal.SIGABRT,
                    signal.SIGSEGV,
                ):
                    self.loop.add_signal_handler(sig, _handle_signal)
            except NotImplementedError:  # Windows dosen't support add_signal_handler
                pass

    def _print_welcome(self):
        print(f"Welcome to Pytdbot (v{pytdbot.__version__}). {pytdbot.__copyright__}")
        print(
            f"Pytdbot is free software and comes with ABSOLUTELY NO WARRANTY. Licensed under the terms of {pytdbot.__license__}.\n\n"
        )


def deepdiff(self, d1, d2):
    d1 = obj_to_dict(d1)
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        return d1 == d2

    deep = DeepDiff(d1, d2, ignore_order=True, view="tree")

    for parent, diffs in deep.items():
        for diff in diffs:
            difflist = diff.path(output_format="list")
            key = ".".join(map(str, difflist))

            if parent in ("dictionary_item_added", "values_changed"):
                self.logger.info(f"{key} changed to {diff.t2}")
            elif parent == "dictionary_item_removed":
                self.logger.info(f"{key} removed")
