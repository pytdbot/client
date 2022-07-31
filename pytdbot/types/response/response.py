from uuid import uuid4
from asyncio import Event, wait_for
from typing import Union
from ujson import dumps


class Response:
    """Generate a response object.

    Args:
        request (``dict``):
            The request object.

        request_id (``str`` | ``int`` | ``dict``, optional):
            The request_id for the object.

        remove_extra (``bool``, optional):
            Remove @extra from the response. Default is True.

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
        self.response = {}
        self.type_ = None
        self._event = Event()

    def __str__(self):
        if self.response == {}:
            return "Response not processed yet."
        else:
            return dumps(self.response, indent=4)

    def __getitem__(self, key):
        return self.response[key]

    def __setitem__(self, key, value):
        self.response[key] = value

    def __delitem__(self, key):
        del self.response[key]

    def __contains__(self, item):
        return item in self.response

    def __iter__(self):
        return iter(self.response.items())

    async def wait(self, timeout: float = None) -> None:
        """Wait for the response.

        Args:
            timeout (``float``, optional): Number of seconds to wait.

        Raises:
            TimeoutError: No response received.
        """
        if timeout is not None:
            await wait_for(self._event.wait(), timeout=timeout)
        else:
            await self._event.wait()

    def set_response(self, response: dict) -> None:
        """Set the response.

        Args:
            response (``dict``): The response object.
        """
        self.response = response
        self.is_processed = True
        self.type_ = response["@type"]

        if self.type_ == "error":
            self.is_error = True

        if self.remove_extra and "@extra" in self.response:
            del self.response["@extra"]

        self._event.set()
