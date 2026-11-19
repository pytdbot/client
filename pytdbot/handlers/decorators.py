from __future__ import annotations

import logging
from asyncio import iscoroutinefunction
from collections.abc import Callable

import pytdbot

from .handler import Handler
from .td_updates import Updates

logger = logging.getLogger(__name__)

HandlerDecorator = Callable[[Callable], Callable]


class Decorators(Updates):
    """Decorators class."""

    def initializer(
        self: pytdbot.Client | None = None,
        filters: pytdbot.filters.Filter | None = None,
        position: int | None = None,
        inner_object: bool = False,
        timeout: float | None = None,
    ) -> HandlerDecorator:
        r"""A decorator to initialize an event object before running other handlers

        Parameters:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in initializers list. Default is ``None`` (append)

            inner_object (``bool``, *optional*):
                Wether to pass an inner object of update or not; for example ``UpdateNewMessage.message``. Default is ``False``

            timeout (``float``, *optional*):
                Max execution time for the initializer before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="initializer",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=inner_object,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="initializer",
                    filter=self,
                    position=position,
                    inner_object=inner_object,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="initializer",
                    filter=filters,
                    position=position,
                    inner_object=inner_object,
                    timeout=timeout,
                )

            return func

        return decorator

    def finalizer(
        self: pytdbot.Client | None = None,
        filters: pytdbot.filters.Filter | None = None,
        position: int | None = None,
        inner_object: bool = False,
        timeout: float | None = None,
    ) -> HandlerDecorator:
        r"""A decorator to finalize an event object after running all handlers

        Parameters:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in finalizers list. Default is ``None`` (append)

            inner_object (``bool``, *optional*):
                Wether to pass an inner object of update or not; for example ``UpdateNewMessage.message``. Default is ``False``

            timeout (``float``, *optional*):
                Max execution time for the finalizer before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="finalizer",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=inner_object,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="finalizer",
                    filter=self,
                    position=position,
                    inner_object=inner_object,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="finalizer",
                    filter=filters,
                    position=position,
                    inner_object=inner_object,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_message(
        self: pytdbot.Client | None = None,
        filters: pytdbot.filters.Filter | None = None,
        position: int | None = None,
        timeout: float | None = None,
    ) -> HandlerDecorator:
        r"""A decorator to handle ``updateNewMessage`` but with ``Message`` object.

        Parameters:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewMessage",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=True,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewMessage",
                    filter=self,
                    position=position,
                    inner_object=True,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewMessage",
                    filter=filters,
                    position=position,
                    inner_object=True,
                    timeout=timeout,
                )

            return func

        return decorator

    def on_command(
        self: "pytdbot.Client | str | None" = None,
        *commands: str,
        filters: "pytdbot.filters.Filter | None" = None,
        position: int | None = None,
        timeout: float | None = None,
        prefix: bool = False,
    ) -> HandlerDecorator:
        r"""A decorator to handle ``updateNewMessage`` by routing on the message text,
        instead of scanning every ``on_message`` handler.

        Commands are matched against ``message.text``: exact match by default, or
        ``startswith`` when ``prefix=True`` (for commands that take arguments).
        An exact match always takes precedence and prefix handlers are not checked.

        Internally a single dispatcher handler is inserted into the
        ``updateNewMessage`` handlers list (at the smallest ``position`` seen
        across ``on_command`` registrations; appended at the end when no
        position is given), so ordering with regular handlers is preserved.

        Parameters:
            commands (``str``):
                One or more command strings. Required.

            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                A filter applied to the matched message before the handler runs

            position (``int``, *optional*):
                The dispatcher position in the handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

            prefix (``bool``, *optional*):
                Match with ``startswith`` instead of exact equality.
                Default is ``False``

        Raises:
            :py:class:`TypeError`
        """

        if isinstance(self, str):
            commands = (self, *commands)
            self = None

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_command(
                        func,
                        *commands,
                        filters=filters,
                        position=position,
                        timeout=timeout,
                        prefix=prefix,
                    )
                else:
                    raise TypeError("Handler must be async")
            else:
                handler = Handler(
                    func=func,
                    update_type="updateNewMessage",
                    filter=filters,
                    position=position,
                    inner_object=True,
                    timeout=timeout,
                )
                handler.commands = commands
                handler.prefix = prefix
                func._handler = handler
            return func

        return decorator

    def on_updateScheduledEvent(
        self: pytdbot.Client | None = None,
        filters: pytdbot.filters.Filter | None = None,
        position: int | None = None,
        timeout: float | None = None,
    ) -> HandlerDecorator:
        r"""A scheduled event has been triggered

        Parameters:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateScheduledEvent",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateScheduledEvent",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateScheduledEvent",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )

            return func

        return decorator
