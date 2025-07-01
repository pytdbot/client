import pytdbot
from typing import Literal, Union


class ServerStats:
    r"""Describes TDLib Server stats

    Parameters:
        my_id (:class:`int`):
            Identifier of the current user

        uptime (:class:`int`):
            Server uptime in seconds

        updates_count (:class:`int`):
            Total number of received updates

        requests_count (:class:`int`):
            Total number of sent requests
    """

    def __init__(
        self,
        my_id: int = 0,
        uptime: int = 0,
        updates_count: int = 0,
        requests_count: int = 0,
    ) -> None:
        self.my_id = my_id
        r"""Identifier of the current user"""
        self.uptime = uptime
        r"""Server uptime in seconds"""
        self.updates_count = updates_count
        r"""Total number of received updates"""
        self.requests_count = requests_count
        r"""Total number of sent requests"""

    def __str__(self):
        return str(pytdbot.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["serverStats"]:
        return "serverStats"

    def getClass(self) -> Literal["ServerStats"]:
        return "ServerStats"

    def to_dict(self) -> dict:
        return {
            "@type": self.getType(),
            "my_id": self.my_id,
            "uptime": self.uptime,
            "updates_count": self.updates_count,
            "requests_count": self.requests_count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Union["ServerStats", None]:
        if data:
            data_class = cls()
            data_class.my_id = data.get("my_id", None)
            data_class.uptime = data.get("uptime", None)
            data_class.updates_count = data.get("updates_count", None)
            data_class.requests_count = data.get("requests_count", None)

        return data_class
