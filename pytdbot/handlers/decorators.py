from .handler import Handler
from .updates import Updates
from typing import Callable
from asyncio import iscoroutinefunction
import pytdbot, logging

logger = logging.getLogger(__name__)


class Decorators(Updates):
    """Decorators class."""

    def initializer(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> None:
        """A decorator to initialize an event object before running other handlers.

        Args:
            filters (`~pytdbot.filters.Filter`, optional): An update filter.
            position (``int``, optional): The function position in initializers list. Defaults to None (append).

        Raises:
            TypeError
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("initializer", func, filters, position)
                else:
                    logger.warn(
                        'Function "{}" is not a coroutine function'.format(func)
                    )
            else:
                func._handler = Handler(func, "initializer", filters, position)

            return func

        return decorator

    def finalizer(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> None:
        """A decorator to finalize an event object after running all handlers.

        Args:
            filters (`~pytdbot.filters.Filter`, optional): An update filter.
            position (``int``, optional): The function position in initializers list. Defaults to None (append).

        Raises:
            TypeError
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("finalizer", func, filters, position)
                else:
                    logger.warn(
                        'Function "{}" is not a coroutine function'.format(func)
                    )
            else:
                func._handler = Handler(func, "finalizer", filters, position)
            return func

        return decorator
