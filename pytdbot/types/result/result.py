from asyncio import Event
from json import dumps
import binascii, os

RETRY_AFTER_PREFEX = "Too Many Requests: retry after "


class Result:
    """Result object.

    Args:
        request (``dict``):
            The request object

    """

    def __init__(
        self,
        request: dict,
    ) -> None:
        self.id = binascii.hexlify(os.urandom(9)).decode()
        request["@extra"] = {"id": self.id}

        self.request = request
        self.is_processed = False
        self.is_error = False
        self.is_limited = False
        self.limited_seconds = 0
        self.result = {}
        self.type = None
        self._event = Event()

    def __str__(self):
        if not self.is_processed:
            return "result not processed yet"
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
        """Wait for the result"""
        return await self._event.wait()

    def set_result(self, result: dict) -> None:
        """Set the result

        Args:
            result (``dict``):
                The result object
        """

        self.result = result
        self.type = result["@type"]
        self.is_processed = True

        if self.type == "error":
            self.is_error = True

            if RETRY_AFTER_PREFEX in self.result["message"]:
                self.is_limited = True
                self.limited_seconds = int(
                    self.result["message"].removeprefix(RETRY_AFTER_PREFEX)
                )

        if "@extra" in result:
            del self.result["@extra"]

        self._event.set()

    def reset(self) -> bool:
        """Reset the current result flags

        Returns:
            :py:class:``bool``: ``True`` on success
        """

        self.is_error = False
        self.is_processed = False
        self.result = {}
        self.type = None
        self._event.clear()

        return True
