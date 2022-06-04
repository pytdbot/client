from .tdjson import TDjson
from .handlers import Decorators, Handler
from .methods import Methods
from .types import Plugins, Response, LogStream, Update
from .filters import Filter
from .exception import StopHandlers, AuthorizationError
from . import VERSION

from platform import python_implementation, python_version
from os.path import join as join_path
from pathlib import Path
from importlib import import_module

from typing import Callable, Union
from logging import getLogger, DEBUG
from base64 import b64encode
import signal, pytdbot, asyncio

try:
    from ujson import dumps
except ImportError:
    from json import dumps


logger = getLogger(__name__)


class Client(Decorators, Methods):
    """Pytdbot, a TDLib client.

    Args:
        api_id (``int``):
            Identifier for Telegram API access, which can be obtained at https://my.telegram.org.

        api_hash (``str``):
            Identifier hash for Telegram API access, which can be obtained at https://my.telegram.org.

        token (``str``):
            Bot token.

        database_encryption_key (``str``):
            Encryption key for database encryption.

        files_directory (``str``):
            Directory for storing files and database.

        lib_path (``str``, optional):
            Path to TDLib library. Defaults to None (auto-detect).

        plugins (:class:`~pytdbot.types.Plugins`, optional):
            Plugins to load.

        system_language_code (``str``, optional):
            System language code. Defaults to "en".

        device_model (``str``, optional):
            Device model. Defaults to None (auto-detect).

        use_test_dc (``bool``, optional):
            If set to true, the Telegram test environment will be used instead of the production environment. Defaults to False.

        use_file_database (``bool``, optional):
            If set to true, information about downloaded and uploaded files will be saved between application restarts. Defaults to True.

        use_chat_info_database (``bool``, optional):
            If set to true, the library will maintain a cache of users, basic groups, supergroups, channels and secret chats. Implies use_file_database. Defaults to True.

        use_message_database (``bool``, optional):
            If set to true, the library will maintain a cache of chats and messages. Implies use_chat_info_database. Defaults to True.

        enable_storage_optimizer (``bool``, optional):
            If set to true, old files will automatically be deleted. Defaults to True.

        ignore_file_names (``bool``, optional):
            If set to true, original file names will be ignored. Otherwise, downloaded files will be saved under names as close as possible to the original name. Defaults to False.

        workers (``int``, optional):
            Number of workers for handling updates. Defaults to 5.

        loop (:py:class:`asyncio.AbstractEventLoop`, optional):
            Event loop. Defaults to None (auto-detect).

        td_verbosity (``int``, optional):
            Verbosity level of TDLib. Defaults to 2.

        td_log (:class:`~pytdbot.types.LogStream`, optional):
            Log stream. Defaults to None (Log to stdout).
    """

    def __init__(
        self,
        api_id: int,
        api_hash: str,
        token: str,
        database_encryption_key: Union[str, bytes],
        files_directory: str,
        lib_path: str = None,
        plugins: Plugins = None,
        system_language_code: str = "en",
        device_model: str = None,
        use_test_dc: bool = False,
        use_file_database: bool = True,
        use_chat_info_database: bool = True,
        use_message_database: bool = True,
        enable_storage_optimizer: bool = True,
        ignore_file_names: bool = False,
        workers: int = 5,
        loop: asyncio.AbstractEventLoop = None,
        td_verbosity: int = 2,
        td_log: LogStream = None,
    ) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.database_encryption_key = database_encryption_key
        self.token = token
        self.files_directory = files_directory
        self.lib_path = lib_path
        self.plugins = plugins
        self.system_language_code = system_language_code
        self.device_model = device_model
        self.use_test_dc = use_test_dc
        self.use_file_database = use_file_database
        self.use_chat_info_database = use_chat_info_database
        self.use_message_database = use_message_database
        self.enable_storage_optimizer = enable_storage_optimizer
        self.ignore_file_names = ignore_file_names
        self.workers = workers
        self.queue = asyncio.Queue()
        self.td_verbosity = td_verbosity
        self.authorization_state = None
        self.connection_state = None
        self.is_running = None
        self.is_logged_in = False
        self.update_count = 0
        self.options = {}

        self._check_init_args()

        self._handlers = {"initializer": [], "finalizer": []}
        self._results = {}
        self._tdjson = TDjson(lib_path, td_verbosity)

        if isinstance(loop, asyncio.AbstractEventLoop):
            asyncio.set_event_loop(loop)
        self.loop = asyncio.get_event_loop()

        if plugins is not None:
            self._load_plugins()

        if isinstance(td_log, LogStream):
            self._tdjson.execute(
                {"@type": "setLogStream", "log_stream": td_log.to_dict()}
            )

    async def __aenter__(self):
        await self.start()
        await self.login()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.stop()
        except Exception:
            pass

    async def start(self, login: bool = True) -> None:
        """Start pytdbot client.

        Args:
            login (``bool``, optional): Login after start. Defaults to True.
        """

        self.loop.create_task(self._listen_loop())

        for _ in range(self.workers):
            self._workers_tasks = []
            self._workers_tasks.append(self.loop.create_task(self._updates_worker()))
        logger.info("Started with %s workers", self.workers)

        if login:
            await self.login()

    async def login(self) -> None:
        """Login to Telegram."""
        if self.is_logged_in:
            return
        else:
            while self.authorization_state != "authorizationStateReady":
                if self.authorization_state == "authorizationStateWaitTdlibParameters":
                    await self._set_td_paramaters()
                elif self.authorization_state == "authorizationStateWaitEncryptionKey":
                    await self._set_encryption_key()
                elif self.authorization_state == "authorizationStateWaitPhoneNumber":
                    await self._set_bot_token()
                authorization = await self.getAuthorizationState()
                self.authorization_state = authorization.type_

        self.me = await self.getMe()
        self.is_logged_in = True
        logger.info(f"Logged in as {self.me['first_name']} @{self.me['username']}")

    def add_handler(
        self,
        update_type: str,
        func: Callable,
        filters: pytdbot.filters.Filter = None,
        position: int = None,
    ) -> None:
        """Add an update handler.

        Args:
            update_type (``str``):
                An update type. [See available updates type](https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_update.html).

            func (`Callable`):
                A callable function.

            filters (:class:`~pytdbot.filters.Filter`, optional):
                message filter.

            position (``int``, optional):
                The function position in handlers list. Defaults to None (append).

        Raises:
            TypeError
        """
        if not isinstance(update_type, str):
            raise TypeError("Argument update_type must be str")
        elif not isinstance(func, Callable):
            raise TypeError("Argument func must be callable")
        elif filters is not None and not isinstance(filters, Filter):
            raise TypeError(
                "Argument filters must be instance of pytdbot.filters.Filter"
            )
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
        """Remove an update handler.

        Args:
            func (`Callable`): A callable function.

        Raises:
            TypeError

        Returns:
            ``bool``: True if handler was removed, False otherwise.
        """
        if not isinstance(func, Callable):
            raise TypeError("Argument func must be callable")
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
        data: dict,
        timeout: float = None,
        request_id: Union[str, int, dict] = None,
    ) -> Response:
        """Invoke a new TDLib request.

        Example:
            .. code-block:: python

                from pytdbot import Client

                async with Client(...) as client:
                    res = await client.invoke({"@type": "getAuthorizationState"})
                    if not res.is_error:
                        print(res)

        Args:
            data (``dict``):
                A request data.

            timeout (``float``, optional):
                Timeout in seconds. Defaults to None (no timeout).

            request_id (``str`` | ``int`` | ``dict``, optional):
                Request id. Defaults to None (random).

        Returns:
            :class:`~pytdbot.types.Response`
        """
        response = Response(data, request_id)
        self._results[response.id] = response
        if (
            logger.root.level >= DEBUG
        ):  # dumping all requests may create performance issues.
            logger.debug("Sending: %s", dumps(response.request, indent=4))

        await self.send(response.request)
        await response.wait(timeout=timeout)
        return response

    def run(self, login: bool = True) -> None:
        """Start the client and block until the client is stopped.

        Example:
            .. code-block:: python

                from pytdbot import Client

                client = Client(...)

                @client.on_updateNewMessage()
                async def new_message(c,update):
                    await update.reply_text('Hello!')

                client.run()

        Args:
            login (``bool``, optional): Login after start. Defaults to True.
        """

        self.loop.run_until_complete(self.start(login))
        self.loop.run_until_complete(self.idle())

    async def idle(self):
        """Idle and wait until the client is stopped."""

        def _handle_signal():
            self.loop.create_task(self.stop())

        for sig in (
            signal.SIGINT,
            signal.SIGTERM,
            signal.SIGABRT,
            signal.SIGQUIT,
            signal.SIGSEGV,
        ):
            self.loop.add_signal_handler(sig, _handle_signal)
        while self.is_running:
            await asyncio.sleep(1)

    async def stop(self):
        """Stop the client."""
        logger.info("Waiting for TDLib to close...")
        await self.close()
        while self.authorization_state != "authorizationStateClosed":
            await asyncio.sleep(0.1)
        self.is_logged_in = False
        self.is_running = False
        logger.info("Closing workers...")
        for x in self._workers_tasks:
            x.cancel()
        logger.info("Instance closed with %s updates served", self.update_count)

    async def send(self, data: dict) -> None:
        return await self.loop.run_in_executor(None, self._tdjson.send, data)

    async def receive(self, timeout: float = 2.0) -> dict:
        return await self.loop.run_in_executor(None, self._tdjson.receive, timeout)

    def _check_init_args(self):
        if not isinstance(self.api_id, int):
            raise TypeError("Argument api_id must be int")
        elif not isinstance(self.api_hash, str):
            raise TypeError("Argument api_hash must be str")
        elif not isinstance(self.database_encryption_key, str) and not isinstance(
            self.database_encryption_key, bytes
        ):
            raise TypeError("Argument database_encryption_key must be str or bytes")
        elif not isinstance(self.files_directory, str):
            raise TypeError("Argument files_directory must be str")
        elif not isinstance(self.token, str):
            raise TypeError("Argument token must be str")
        elif not isinstance(self.td_verbosity, int):
            raise TypeError("Argument td_verbosity must be int")
        elif not isinstance(self.workers, int):
            raise TypeError("Argument workers must be int")
        if self.workers < 1:
            raise ValueError("Argument workers must be greater than 0")
        try:
            self.bot_id, _ = self.token.split(":")
        except Exception:
            raise ValueError("Argument token must be in format bot_id:bot_hash")

    def _load_plugins(self):
        count = 0
        handlers = 0
        for path in sorted(Path(self.plugins.folder).rglob("*.py")):
            module_path = ".".join(path.parent.parts + (path.stem,))
            try:
                module = import_module(module_path)
            except Exception:
                logger.exception("Failed to load plugin %s", module_path)
            else:
                logger.debug("Plugin %s loaded", module_path)
                for name in dir(module):
                    obj = getattr(module, name)
                    if hasattr(obj, "_handler"):
                        if isinstance(obj._handler, Handler):
                            if asyncio.iscoroutinefunction(obj._handler.func):
                                self.add_handler(
                                    obj._handler.update_type,
                                    obj._handler.func,
                                    obj._handler.filter,
                                    obj._handler.position,
                                )
                                logger.debug(
                                    "Handler %s added from %s",
                                    obj._handler.func,
                                    module_path,
                                )
                                handlers += 1
                            else:
                                logger.warn(
                                    'Handler " %s " is not coroutine from " %s "',
                                    obj._handler.func,
                                    module_path,
                                )
                count += 1
        logger.info("From %s plugins got %s handlers", count, handlers)

    async def _listen_loop(self):
        self.is_running = True
        logger.info("Listening for updates...")
        try:
            while self.is_running:
                data = await self.receive()
                if data is None:
                    continue
                self.loop.create_task(self._process_data(data))
        except Exception:
            self.is_running = False
            logger.exception("Exception in _listen_loop")

    async def _process_data(self, data):
        if "@type" not in data:
            return
        elif "@extra" in data:
            if data["@extra"]["request_id"] in self._results:
                response: Response = self._results.pop(data["@extra"]["request_id"])
                response.set_response(data)
        else:
            if data["@type"] == "updateAuthorizationState":
                self.loop.create_task(self._handle_authorization_state(data))
            elif data["@type"] == "updateMessageSendSucceeded":
                self.loop.create_task(self._handle_update_message_succeeded(data))
            elif data["@type"] == "updateMessageSendFailed":
                self.loop.create_task(self._handle_update_message_failed(data))
            elif data["@type"] == "updateConnectionState":
                self.loop.create_task(self._handle_connection_state(data))
            elif data["@type"] == "updateOption":
                self.loop.create_task(self._handle_update_option(data))
            self.queue.put_nowait(data)

    async def _updates_worker(self):
        while self.is_running:
            try:
                data = await self.queue.get()
                if "@type" not in data:
                    continue

                if (
                    logger.root.level >= DEBUG
                ):  # dumping all updates may create performance issues.
                    logger.debug(
                        "Received: %s",
                        dumps(data, indent=4),
                    )
                update_type = data["@type"]

                if update_type in self._handlers:
                    data = Update(self, data)

                    if update_type == "updateNewMessage":
                        if data["message"]["is_outgoing"]:
                            continue
                    self.update_count += 1

                    for initializer in self._handlers["initializer"]:
                        try:
                            if isinstance(initializer.filter, Filter):
                                if asyncio.iscoroutinefunction(initializer.filter.func):
                                    if not await initializer.filter.func(self, data):
                                        continue
                                else:
                                    if not await self.loop.run_in_executor(
                                        None, initializer.filter.func, self, data
                                    ):
                                        continue
                            await initializer.func(self, data)
                        except StopHandlers:
                            break
                        except Exception:
                            logger.exception("Initializer %s failed", initializer)

                    try:
                        for handler in self._handlers[update_type]:
                            try:
                                if isinstance(handler.filter, Filter):
                                    if asyncio.iscoroutinefunction(handler.filter.func):
                                        if not await handler.filter.func(self, data):
                                            continue
                                    else:
                                        if not await self.loop.run_in_executor(
                                            None, handler.filter.func, self, data
                                        ):
                                            continue
                                await handler.func(self, data)
                            except StopHandlers:
                                break
                            except Exception:
                                logger.exception("Exception in handler %s", handler)
                    finally:
                        for finalizer in self._handlers["finalizer"]:
                            try:
                                if isinstance(finalizer.filter, Filter):
                                    if asyncio.iscoroutinefunction(
                                        finalizer.filter.func
                                    ):
                                        if not await finalizer.filter.func(self, data):
                                            continue
                                    else:
                                        if not await self.loop.run_in_executor(
                                            None, finalizer.filter.func, self, data
                                        ):
                                            continue
                                await finalizer.func(data)
                            except Exception:
                                logger.exception("Finalizer %s failed", finalizer)

            except Exception:
                logger.exception("Exception in _updates_worker")

    async def _set_td_paramaters(self):
        prams = {
            "use_test_dc": self.use_test_dc,
            "api_id": self.api_id,
            "api_hash": self.api_hash,
            "system_language_code": self.system_language_code,
            "device_model": python_implementation() + " " + python_version(),
            "use_file_database": self.use_file_database,
            "use_chat_info_database": self.use_chat_info_database,
            "use_message_database": self.use_message_database,
            "enable_storage_optimizer": self.enable_storage_optimizer,
            "ignore_file_names": self.ignore_file_names,
            "files_directory": self.files_directory,
            "database_directory": join_path(self.files_directory, "database"),
            "application_version": "Pytdbot " + VERSION,
        }
        res = await self.setTdlibParameters(prams)
        if res.is_error:
            raise AuthorizationError(res.response["message"])

    async def _set_encryption_key(self):
        if isinstance(self.database_encryption_key, str):
            self.database_encryption_key = self.database_encryption_key.encode("utf-8")

        res = await self.checkDatabaseEncryptionKey(
            b64encode(self.database_encryption_key).decode("utf-8")
        )
        if res.is_error:
            raise AuthorizationError(res.response["message"])

    async def _set_bot_token(self):
        res = await self.checkAuthenticationBotToken(self.token)
        if res.is_error:
            raise AuthorizationError(res.response["message"])

    async def _handle_authorization_state(self, update):
        if self.is_logged_in == True:
            if update["@type"] == "updateAuthorizationState":
                self.authorization_state = update["authorization_state"]["@type"]
                logger.info(
                    "Authorization state changed to %s",
                    self.authorization_state.replace("authorizationState", ""),
                )

    async def _handle_connection_state(self, update):
        if update["@type"] == "updateConnectionState":
            self.connection_state = update["state"]["@type"]
            logger.info(
                "Connection state changed to %s",
                self.connection_state.replace("connectionState", ""),
            )

    async def _handle_update_message_succeeded(self, update):
        if update["old_message_id"] in self._results:
            response: Response = self._results.pop(update["old_message_id"])
            response.set_response(update["message"])

    async def _handle_update_message_failed(self, update):
        if update["old_message_id"] in self._results:
            response: Response = self._results.pop(update["old_message_id"])
            response.set_response(
                {
                    "@type": "error",
                    "code": update["error_code"],
                    "message": update["error_message"],
                }
            )

    async def _handle_update_option(self, update):

        if update["value"]["@type"] == "optionValueBoolean":
            self.options[update["name"]] = bool(update["value"]["value"])
        elif update["value"]["@type"] == "optionValueEmpty":
            self.options[update["name"]] = None
        elif update["value"]["@type"] == "optionValueInteger":
            self.options[update["name"]] = int(update["value"]["value"])
        else:
            self.options[update["name"]] = update["value"]["value"]

        if self.is_logged_in:
            logger.info(
                "Option %s changed to %s",
                update["name"],
                self.options[update["name"]],
            )
