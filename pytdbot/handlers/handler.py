from typing import Callable

import pytdbot

from ..filters import Filter


class Handler:
    r"""A handler class."""

    def __init__(
        self,
        func: Callable,
        update_type: str,
        filter: Filter = None,
        position: int = None,
        inner_object: bool = False,
        is_from_plugin: bool = False,
    ) -> None:
        self.func = func
        self.update_type = update_type
        self.filter = filter
        self.position = position
        self.inner_object = inner_object
        self.is_from_plugin = is_from_plugin

    def __call__(self, client: "pytdbot.Client", update: "pytdbot.types.Update"):
        return self.func(client, update)

    def __str__(self) -> str:
        return f"Handler(func={self.func}, update_type={self.update_type}, filter={self.filter}, position={self.position}, inner_object={self.inner_object}, is_from_plugin={self.is_from_plugin})"

    def __repr__(self) -> str:
        return str(self)
