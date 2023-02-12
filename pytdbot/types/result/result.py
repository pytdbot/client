from uuid import uuid4
from asyncio import Event
from typing import Union
from ujson import dumps


class Result:
    """Result object.

    Args:
        request (``dict``):
            The request object.

        request_id (``str`` | ``int`` | ``dict``, *optional*):
            The request_id for the object.

        remove_extra (``bool``, *optional*):
            Remove @extra from the result. Defaults to ``True``.

    """

    def __init__(
        self,
        request: dict,
        request_id: Union[str, int, dict] = None,
        remove_extra: bool = True,
    ) -> None:
        self.id = uuid4().hex if request_id is None else request_id
        request["@extra"] = {"request_id": self.id}
        self.request = request
        self.remove_extra = remove_extra
        self.is_error = False
        self.is_processed = False
        self.result = {}
        self.type = None
        self._event = Event()

    def __str__(self):
        if self.result == {}:
            return "result not processed yet."
        else:
            return dumps(self.result, indent=4)

    def __getitem__(self, key):
        return self.result[key]

    def __setitem__(self, key, value):
        self.result[key] = value

    def __delitem__(self, key):
        del self.result[key]

    def __contains__(self, item):
        return item in self.result

    def __iter__(self):
        return iter(self.result.items())

    def __await__(self):
        return self.wait().__await__()

    async def wait(self) -> bool:
        """Wait for the result."""
        return await self._event.wait()

    def set_result(self, result: dict) -> None:
        """Set the result.

        Args:
            result (``dict``): The result object.
        """
        self.result = result
        self.is_processed = True
        self.type = result["@type"]

        if self.type == "error":
            self.is_error = True

        if self.remove_extra and "@extra" in self.result:
            del self.result["@extra"]

        self._event.set()

    def reset(self) -> bool:
        """Reset the current result flags

        Returns:
            :py:class:``bool``: ``True`` on success.
        """
        self.is_error = False
        self.is_processed = False
        self.result = {}
        self.type = None
        self._event.clear()

        return True
