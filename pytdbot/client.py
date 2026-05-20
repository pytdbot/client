from __future__ import annotations

import asyncio
import signal
import sys
from collections.abc import Callable
from importlib import import_module
from importlib import reload as reload_module
from inspect import iscoroutinefunction
from json import dumps
from logging import DEBUG, getLogger
from os.path import join as join_path
from pathlib import Path
from platform import python_implementation, python_version
from threading import current_thread, main_thread

try:
    import nats
except ImportError:
    nats = None

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

        nats_url (``str``, *optional*):
            URL for NATS server connection

        instance_id (``str``, *optional*):
            Instance ID for NATS connections and queues. Default is ``None`` (random)

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

        options (``dict``, *optional*):
            Pass key-value dictionary to set TDLib options. Check the list of available options at https://core.telegram.org/tdlib/options

        workers (``int``, *optional*):
            Number of workers to handle updates. Default is ``5``. If set to ``None``, updates will be immediately handled instead of being queued, which can impact performance.

        default_handlers_timeout (``float``, *optional*):
            Default timeout for handlers. If set, each handler will be awaited with this timeout (ignored if ``timeout`` is set when registering handler). Default is ``None`` (no timeout)

        no_updates (``bool``, *optional*):
            Whether the client should handle updates or not. Applicable only when using [TDLib Server](https://github.com/pytdbot/tdlib-server). Default is ``False``

        td_verbosity (``int``, *optional*):
            Verbosity level of TDLib. Default is ``2``

        td_log (:class:`~pytdbot.types.LogStream`, *optional*):
            Log stream. Default is ``None`` (Log to ``stdout``)

        user_bot (``bool``, *optional*):
            Pass ``True`` if this is a user-bot. Default is ``False``
    """

    def __init__(
        self,
        token: str | None = None,
        api_id: int | None = None,
        api_hash: str | None = None,
        nats_url: str | None = None,
        instance_id: str | None = None,
        lib_path: str | None = None,
        plugins: Plugins | None = None,
        default_parse_mode: str | None = None,
        system_language_code: str = "en",
        device_model: str | None = None,
        files_directory: str | None = None,
        database_encryption_key: str | bytes | None = None,
        use_test_dc: bool = False,
        use_file_database: bool = True,
        use_chat_info_database: bool = True,
        use_message_database: bool = True,
        options: dict | None = None,
        workers: int = 5,
        queue_size: int = 1000,
        default_handlers_timeout: float | None = None,
        no_updates: bool = False,
        load_messages_before_reply: bool = False,
        td_verbosity: int = 2,
        td_log: LogStream | None = None,
        user_bot: bool = False,
    ) -> None:
        self.__api_id = api_id
        self.__api_hash = api_hash
        self.__nats_url = nats_url
        self._nats_instance_id = (
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
        self.queue_size = queue_size
        self.default_handlers_timeout = default_handlers_timeout
        self.no_updates = no_updates
        self.load_messages_before_reply = load_messages_before_reply
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
        self.is_reloading_plugins = False
        self.is_nats = True if nats_url else False
        self.options = {}
        self.allow_outgoing_message_types: tuple = (types.MessagePaymentRefunded,)
        self.get_message_methods = frozenset(
            {
                "getmessage",
                "getmessagelocally",
                "getrepliedmessage",
                "getcallbackquerymessage",
            }
        )

        self._check_init_args()

        self._handlers = {"initializer": [], "finalizer": []}
        self._current_handlers = {}
        self._results: dict[str, asyncio.Future] = {}
        self._workers_tasks = None
        self.__wait_login: asyncio.Event = None
        self.__authorization_state: str = None
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
        self.__idle_event: asyncio.Event = None
        self.__closed_event: asyncio.Event = None

        # NATS
        self.__nc = None
        self.__requests_subject = f"bot.{self.my_id}.requests"
        self.__updates_subject = f"bot.{self.my_id}.updates"
        self.__broadcast_subject = f"bot.{self.my_id}.broadcast"

        self.loop = None

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

    async def getServerStats(
        self,
    ) -> pytdbot.types.ServerStats | pytdbot.types.Error:
        """Returns TDLib Server stats"""

        self._check_nats()

        return await self.invoke({"@type": "getServerStats"})

    async def scheduleEvent(
        self, name: str, payload: str, send_at: int
    ) -> pytdbot.types.ScheduledEvent | pytdbot.types.Error:
        """Schedule an event

        Parameters:
            name (:class:`str`):
                Event name

            payload (:class:`str`):
                The event payload to be scheduled

            send_at (:class:`int`):
                Unix timestamp when the event should be sent
        """

        self._check_nats()

        if not isinstance(name, str):
            raise ValueError("name must be str")
        if not isinstance(payload, str):
            raise ValueError("payload must be str")
        if not isinstance(send_at, (int, float)):
            raise ValueError("send_at must be int")

        return await self.invoke(
            {
                "@type": "scheduleEvent",
                "name": name,
                "payload": payload,
                "send_at": send_at,
            }
        )

    async def cancelScheduledEvent(
        self, event_id: str
    ) -> pytdbot.types.Ok | pytdbot.types.Error:
        """Cancel a scheduled event

        Parameters:
            event_id (:class:`str`):
                Event ID to cancel
        """

        self._check_nats()

        if not isinstance(event_id, str):
            raise ValueError("event_id must be str")

        return await self.invoke(
            {"@type": "cancelScheduledEvent", "event_id": event_id}
        )

    async def start(self, wait_login: bool = True) -> None:
        r"""Start pytdbot client

        Parameters:
            wait_login (``bool``, *optional*):
                Whether to wait until the client is logged in. For bots only. Default is ``True``
        """

        if not self.is_running:
            self.logger.info("Starting pytdbot client...")

            self.loop = asyncio.get_running_loop()
            self.__idle_event = asyncio.Event()
            self.__closed_event = asyncio.Event()

            if self.is_nats:
                await self.__start_nats()
            elif not self.client_manager:
                self.__wait_login = asyncio.Event() if not self.user_bot else None

                self.client_manager = ClientManager(
                    self, self.lib_path, self.td_verbosity, loop=self.loop
                )
                await self.client_manager.start()
                self.is_running = True

            if isinstance(self.td_log, LogStream) and not self.is_nats:
                await self.__send(
                    {"@type": "setLogStream", "log_stream": obj_to_dict(self.td_log)}
                )

            if isinstance(self.workers, int) and not self.is_nats:
                self._workers_tasks = [
                    self.loop.create_task(self._queue_update_worker())
                    for _ in range(self.workers)
                ]
                self.__is_queue_worker = True

                self.logger.info(f"Started with {self.workers} workers")
            else:
                self.__is_queue_worker = False
                self.logger.info("Started with unlimited updates processes")

        self.loop.create_task(
            self.getOption(name="version")
        )  # Ping TDLib to start processing updates

        if wait_login and self.__wait_login:
            await self.__wait_login.wait()

    def add_handler(
        self,
        update_type: type[pytdbot.types.Update] | str,
        func: Callable,
        filters: pytdbot.filters.Filter | None = None,
        position: int | None = None,
        inner_object: bool = False,
        timeout: float | None = None,
        is_from_plugin: bool = False,
    ) -> None:
        r"""Add an update handler

        Parameters:
            update_type (``str`` || :class:`~pytdbot.types.Update`):
                An update type

            func (``Callable``):
                A callable function

            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                message filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            inner_object (``bool``, *optional*):
                Wether to pass an inner object of update or not; for example ``UpdateNewMessage.message``. Default is ``False``

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. If ``None``, ``Client.default_handlers_timeout`` is preferred. Default is ``None``

            is_from_plugin (``bool``, *optional*):
                Wether this handler is from a loaded plugin (this can help reloading plugin during runtime; for development only). Default is ``False``

        Raises:
            TypeError
        """

        if not isinstance(update_type, str):
            if issubclass(update_type, types.Update):
                update_type = update_type.getType()
            else:
                raise TypeError(
                    "update_type must be str or subclass of pytdbot.types.Update"
                )
        if not isinstance(func, Callable):
            raise TypeError("func must be callable")
        if filters is not None and not isinstance(filters, Filter):
            raise TypeError("filters must be instance of pytdbot.filters.Filter")

        handler = Handler(
            func=func,
            update_type=update_type,
            filter=filters,
            position=position,
            inner_object=inner_object,
            timeout=timeout,
            is_from_plugin=is_from_plugin,
        )

        if update_type not in self._handlers:
            self._handlers[update_type] = []

        handlers_list = self._handlers[update_type]
        _pos = (position is None, position)

        inserted = False
        for i, h in enumerate(handlers_list):
            if _pos < (h.position is None, h.position):
                handlers_list.insert(i, handler)
                inserted = True
                break
        if not inserted:
            handlers_list.append(handler)

        self._update_handlers()

    def reload_plugins(self):
        """Reload all plugins, non-plugin handlers are not ``reloaded``
        .. note::
            This is for ``development purposes only`` and should not be used
            in production environments
        """

        if self.is_reloading_plugins:
            return

        self.is_reloading_plugins = True
        for handlers in self._handlers.values():
            for handler in handlers.copy():
                if handler.is_from_plugin:
                    self.remove_handler(handler.func)

        self._load_plugins(reload_plugins=True)
        self.is_reloading_plugins = False

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

        removed = False
        for handlers in self._handlers.values():
            i = 0
            while i < len(handlers):
                if handlers[i].func == func:
                    del handlers[i]
                    removed = True
                else:
                    i += 1

        if removed:
            self._update_handlers()
        return removed

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
        request_method = request["@type"].lower()

        if (
            self.logger.root.level >= DEBUG or self.logger.level >= DEBUG
        ):  # dumping all requests may create performance issues
            self.logger.debug(f"Sending: {dumps(request, indent=4)}")

        is_chat_attempted_load = request_method == "getchat"
        is_message_attempted_load = request_method in self.get_message_methods

        while True:
            future = self._create_request_future(request)
            await self.__send(request)
            result = await future

            if not isinstance(result, types.Error):
                break

            error_code = result.code
            error_message = result.message

            if error_message.startswith(
                "Failed to parse JSON object as TDLib request:"
            ):
                raise ValueError(error_message)

            if error_code != 400:
                break

            chat_id = request.get("chat_id")
            message_id = request.get("message_id")

            if not is_message_attempted_load and (
                error_message == "Message not found" and (chat_id and message_id)
            ):
                is_message_attempted_load = True

                if self.logger.isEnabledFor(DEBUG):
                    self.logger.debug(
                        f"Attempt to load message {message_id} in {chat_id}"
                    )

                message = await self.getMessage(chat_id=chat_id, message_id=message_id)
                if message:
                    if self.logger.isEnabledFor(DEBUG):
                        self.logger.debug(
                            f"Message {message_id} in {chat_id} is loaded"
                        )
                    continue
                else:
                    self.logger.debug(
                        f"Failed to load message {message_id} in {chat_id}"
                    )

            if not is_chat_attempted_load and (
                error_message == "Chat not found" and chat_id
            ):
                is_chat_attempted_load = True

                if self.logger.isEnabledFor(DEBUG):
                    self.logger.debug(f"Attempt to load chat {chat_id}")

                chat = await self.getChat(chat_id=chat_id)
                if not isinstance(chat, types.Error):
                    if self.logger.isEnabledFor(DEBUG):
                        self.logger.debug(f"Chat {chat_id} is loaded")

                    reply_to_message_id = (request.get("reply_to") or {}).get(
                        "message_id", 0
                    )

                    # if the request is a reply to another message
                    # load the replied message to avoid "Message not found"
                    if reply_to_message_id > 0:
                        await self.getMessage(
                            chat_id=chat_id, message_id=reply_to_message_id
                        )

                    continue
                else:
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

    async def run(self) -> None:
        r"""Start the client and block until the client is stopped

        Example:
            .. code-block:: python

                import asyncio
                from pytdbot import Client

                client = Client(...)

                @client.on_updateNewMessage()
                async def new_message(c,update):
                    await update.reply_text('Hello!')

                asyncio.run(client.run())
        """

        await self.start()

        self._register_signal_handlers()

        await self.idle()

    async def idle(self):
        r"""Idle and wait until the client is stopped"""

        if not self.__idle_event:
            self.__idle_event = asyncio.Event()

        await self.__idle_event.wait()

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

        if self.is_nats:
            # fake closing because TDLib Server doesn't allow close() from workers
            await self.process_update(
                obj_to_dict(
                    types.UpdateAuthorizationState(
                        authorization_state=types.AuthorizationStateClosing()
                    )
                )
            )
            await self.process_update(
                obj_to_dict(
                    types.UpdateAuthorizationState(
                        authorization_state=types.AuthorizationStateClosed()
                    )
                )
            )

        await self.__closed_event.wait()

        if self.is_nats:
            await self.__nc.close()

        self.__stop_client()

        if self.client_manager and not self.client_manager.start_clients_on_add:
            await self.client_manager.close()

        self.logger.info("Instance closed")
        self.__idle_event.set()

        return True

    def _create_request_future(
        self, request: dict, result_id: str | None = None, handle_result: bool = True
    ) -> asyncio.Future:
        result = asyncio.Future()

        result.request = request

        if handle_result:
            self._results[
                result_id if result_id is not None else request["@extra"]["id"]
            ] = result
        return result

    async def __send(self, request: dict) -> None:
        if self.is_nats:
            await self.__on_update(
                await self.__nc.request(
                    self.__requests_subject,
                    json_dumps(request, encode=True),
                    timeout=None,
                )
            )
        else:
            self.client_manager.send(self.client_id, request)

    def _check_nats(self):
        assert self.is_nats, "This method is only available for TDLib Server"

    def _check_init_args(self):
        if self.user_bot:
            return

        if not self.is_nats:
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

    def _update_handlers(self):
        self._current_handlers = {
            k: tuple(sorted(v, key=lambda x: (x.position is None, x.position)))
            for k, v in self._handlers.items()
        }

    def _load_plugins(self, reload_plugins: bool = False):
        count = 0
        handlers = 0
        plugin_paths = sorted(Path(self.plugins.folder).rglob("*.py"))

        if self.plugins.include:
            plugin_paths = [
                path
                for path in plugin_paths
                if ".".join((*path.parent.parts, path.stem)) in self.plugins.include
            ]
        elif self.plugins.exclude:
            plugin_paths = [
                path
                for path in plugin_paths
                if ".".join((*path.parent.parts, path.stem)) not in self.plugins.exclude
            ]

        for path in plugin_paths:
            module_path = ".".join((*path.parent.parts, path.stem))

            try:
                module = import_module(module_path)
                if reload_plugins:
                    reload_module(module)
            except Exception:
                self.logger.exception(f"Failed to import plugin {module_path}")
                continue

            plugin_handlers_count = 0
            seen = set()
            handlers_to_load = []
            for obj in vars(module).values():
                if hasattr(obj, "_handler") and isinstance(obj._handler, Handler):
                    hid = id(obj._handler)
                    if hid not in seen:
                        seen.add(hid)
                        handlers_to_load.append(obj._handler)

            for handler in handlers_to_load:
                if iscoroutinefunction(handler.func):
                    self.add_handler(
                        update_type=handler.update_type,
                        func=handler.func,
                        filters=handler.filter,
                        position=handler.position,
                        inner_object=handler.inner_object,
                        timeout=handler.timeout,
                        is_from_plugin=True,
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
        cache = self.__cache["is_coro_filter"]
        result = cache.get(func)
        if result is None:
            result = iscoroutinefunction(func)
            cache[func] = result
        return result

    async def process_update(self, update: dict) -> None:
        if not update:
            self.logger.warning("Received None update")
            return

        is_debug = self.logger.isEnabledFor(DEBUG)

        if extra := update.get("@extra"):
            result_id = extra["id"]

            if is_debug:
                self.logger.debug(
                    f"Received result for {result_id}: {dumps(update, indent=4)}"
                )

            if result_id and (result := self._results.pop(result_id, None)):
                result.set_result(dict_to_obj(update, self))

            elif update["@type"] == "error" and "option" in extra:
                self.logger.error(f"{extra['option']}: {update['message']}")

            return

        if is_debug:
            self.logger.debug(f"Received: {dumps(update, indent=4)}")

        update_obj = dict_to_obj(update, self)

        if handler := self.__local_handlers.get(update.get("@type")):
            self.loop.create_task(handler(update_obj))

        if not self.is_nats and self.__is_queue_worker:
            self.queue.put_nowait(update_obj)
        else:
            await self._handle_update(update_obj)

    def get_inner_object(self, update: types.TlObject):
        if isinstance(update, types.UpdateNewMessage):
            return update.message
        return update

    async def __run_handler_group(self, update, handlers, label):
        inner_object = self.get_inner_object(update)

        for handler in handlers:
            try:
                handler_value = inner_object if handler.inner_object else update

                if handler.filter is not None:
                    filter_function = handler.filter.func

                    if self.is_coro_filter(filter_function):
                        if not await filter_function(self, handler_value):
                            continue
                    elif not filter_function(self, handler_value):
                        continue

                if self.default_handlers_timeout is None and handler.timeout is None:
                    await handler(self, handler_value)
                else:
                    timeout = handler.timeout or self.default_handlers_timeout
                    try:
                        await asyncio.wait_for(
                            handler(self, handler_value),
                            timeout=timeout,
                        )
                    except asyncio.TimeoutError:
                        self.logger.warning(
                            f"{label} {handler} timed out after {timeout} seconds"
                        )
            except StopHandlers as e:
                raise e
            except Exception:
                self.logger.exception(f"{label} {handler} failed")

    async def __run_initializers(self, update):
        await self.__run_handler_group(
            update, self._current_handlers["initializer"], "Initializer"
        )

    async def __run_handlers(self, update):
        await self.__run_handler_group(
            update, self._current_handlers[update.getType()], "Handler"
        )

    async def __run_finalizers(self, update):
        await self.__run_handler_group(
            update, self._current_handlers["finalizer"], "Finalizer"
        )

    async def _handle_update(self, update):
        if update.getType() in self._current_handlers:
            if (
                not self.user_bot
                and isinstance(update, types.UpdateNewMessage)
                and not isinstance(
                    update.message.content, self.allow_outgoing_message_types
                )
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

        if self.is_nats:
            return

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

            self.loop.create_task(
                self.__send(
                    {
                        "@type": "setOption",
                        "name": k,
                        "value": data,
                        "@extra": {"option": k, "value": v, "id": ""},
                    }
                )
            )
            if self.logger.isEnabledFor(DEBUG):
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
            self.__idle_event.clear()

            self.me = await self.getMe()
            if isinstance(self.me, types.Error):
                self.logger.error(f"Get me error: {self.me.message}")

            if self.__wait_login:
                self.__wait_login.set()

            self.logger.info(
                f"Logged in as {self.me.first_name} "
                f"{str(self.me.id) if not self.me.usernames else '@' + self.me.usernames.editable_username}"
            )

        if self.authorization_state == "authorizationStateClosing":
            self.__is_closing = True
        elif self.authorization_state == "authorizationStateClosed":
            self.__closed_event.set()
            if self.__is_closing is False:
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
            result.set_result(
                update.error if not update.message.media_album_id else update.message
            )

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

    async def __nc_error_handler(self, e):
        self.logger.error(f"NATS connection error: {e}")

    async def __nc_reconnect_handler(self):
        self.logger.info("Reconnected to NATS server")

    async def __nc_disconnect_handler(self):
        self.logger.info("Disconnected from NATS server")

    async def __nc_closed_handler(self):
        self.logger.info("Closed connection to NATS server")

    async def __start_nats(self):
        if not nats:
            raise ImportError(
                f"nats-py is not installed, please install it with `{sys.executable} -m pip install --upgrade nats-py`"
            )

        self.__nc = await nats.connect(
            self.__nats_url,
            name=f"Pytdbot instance {self._nats_instance_id}",
            error_cb=self.__nc_error_handler,
            reconnected_cb=self.__nc_reconnect_handler,
            closed_cb=self.__nc_closed_handler,
            disconnected_cb=self.__nc_disconnect_handler,
            max_reconnect_attempts=-1,
        )

        if self.__nc.is_connected:
            self.logger.info("Connected to TDLib server via NATS")
        else:
            raise AuthorizationError("Failed to connect to TDLib server via NATS")

        self.is_running = True

        if not self.no_updates:
            await self.__nc.subscribe(
                self.__updates_subject,
                queue="updates",
                cb=self.__on_update,
            )

        await self.__nc.subscribe(self.__broadcast_subject, cb=self.__on_update)

        await self._set_options()

        res = await self.getCurrentState()
        for update in res.updates:
            # when using obj_to_dict the key "@client_id" won't exists
            # since it's not part of the object
            await self.process_update(obj_to_dict(update))

    async def __on_update(self, update):
        self.loop.create_task(self.process_update(json_loads(update.data)))

    async def __handle_update_user(self, update: types.UpdateUser):
        if self.is_authenticated and self.me and update.user.id == self.me.id:
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
            self.is_nats
            or self.authorization_state != "authorizationStateWaitPhoneNumber"
            or not self.__token
        ):
            return

        res = await self.checkAuthenticationBotToken(token=self.__token)

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
    if not isinstance(d1, dict):
        d1 = obj_to_dict(d1)
    if not isinstance(d2, dict):
        d2 = obj_to_dict(d2)

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
