import logging
import pytdbot

from typing import Callable
from asyncio import iscoroutinefunction
from .handler import Handler
from .td_updates import Updates

logger = logging.getLogger(__name__)


class Decorators(Updates):
    """Decorators class."""

    def initializer(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        inner_object: bool = False,
    ) -> None:
        r"""A decorator to initialize an event object before running other handlers

        Parameters:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in initializers list. Default is ``None`` (append)

            inner_object (``bool``, *optional*):
                Wether to pass an inner object of update or not; for example ``UpdateNewMessage.message``. Default is ``False``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "initializer", func, filters, position, inner_object
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "initializer", self, position, inner_object
                )
            else:
                func._handler = Handler(
                    func, "initializer", filters, position, inner_object
                )

            return func

        return decorator

    def finalizer(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        inner_object: bool = False,
    ) -> None:
        r"""A decorator to finalize an event object after running all handlers

        Parameters:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in finalizers list. Default is ``None`` (append)

            inner_object (``bool``, *optional*):
                Wether to pass an inner object of update or not; for example ``UpdateNewMessage.message``. Default is ``False``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("finalizer", func, filters, position, inner_object)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "finalizer", self, position, inner_object)
            else:
                func._handler = Handler(
                    func, "finalizer", filters, position, inner_object
                )
            return func

        return decorator

    def on_message(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> None:
        r"""A decorator to handle ``updateNewMessage`` but with ``Message`` object.

        Parameters:
            filters (:class:`~pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNewMessage", func, filters, position, True)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNewMessage", self, position, True)
            else:
                func._handler = Handler(
                    func, "updateNewMessage", filters, position, True
                )

            return func

        return decorator
