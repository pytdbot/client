from typing import Callable
from ..filters import Filter


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

    def __str__(self) -> str:
        return f"Handler(func={self.func}, update_type={self.update_type}, filter={self.filter}, position={self.position})"

    def __repr__(self) -> str:
        return str(self)
