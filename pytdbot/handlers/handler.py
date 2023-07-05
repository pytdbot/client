from typing import Callable
from ..filters import Filter
import pytdbot


class Handler:
    """A handler class."""

    def __init__(
        self,
        func: Callable,
        update_type: str,
        filter: Filter = None,
        position: int = None,
    ) -> None:
        self.func = func
        self.update_type = update_type
        self.filter = filter
        self.position = position

    def __call__(self, client: "pytdbot.Client", update: "pytdbot.types.Update"):
        return self.func(client, update)

    def __str__(self) -> str:
        return f"Handler(func={self.func}, update_type={self.update_type}, filter={self.filter}, position={self.position})"

    def __repr__(self) -> str:
        return str(self)
