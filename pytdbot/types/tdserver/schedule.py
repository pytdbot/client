import pytdbot
from typing import Literal, Union


class ScheduledEvent:
    r"""Describes a scheduled event

    Parameters:
        event_id (:class:`int`):
            Unique identifier of the scheduled event

        send_at (:class:`int`):
            Point in time \(Unix timestamp\) when the scheduled event will be sent
    """

    def __init__(
        self,
        event_id: int = 0,
        send_at: int = 0,
    ) -> None:
        self.event_id = event_id
        r"""Unique identifier of the scheduled event"""
        self.send_at = send_at
        r"""Point in time \(Unix timestamp\) when the scheduled event will be sent"""

    def __str__(self):
        return str(pytdbot.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["scheduledEvent"]:
        return "scheduledEvent"

    def getClass(self) -> Literal["ScheduledEvent"]:
        return "ScheduledEvent"

    def to_dict(self) -> dict:
        return {
            "@type": self.getType(),
            "event_id": self.event_id,
            "send_at": self.send_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Union["ScheduledEvent", None]:
        if data:
            data_class = cls()
            data_class.event_id = data.get("event_id", None)
            data_class.send_at = data.get("send_at", None)

        return data_class


class UpdateScheduledEvent:
    r"""A scheduled event

    Parameters:
        event_id (:class:`int`):
            Unique identifier of the scheduled event

        payload (:class:`str`):
            Event payload
    """

    def __init__(
        self,
        event_id: int = 0,
        payload: str = "",
    ) -> None:
        self.event_id = event_id
        r"""Unique identifier of the scheduled event"""
        self.payload = payload
        r"""Event payload"""

    def __str__(self):
        return str(pytdbot.utils.obj_to_json(self, indent=4))

    def getType(self) -> Literal["updateScheduledEvent"]:
        return "updateScheduledEvent"

    def getClass(self) -> Literal["UpdateScheduledEvent"]:
        return "UpdateScheduledEvent"

    def to_dict(self) -> dict:
        return {
            "@type": self.getType(),
            "event_id": self.event_id,
            "payload": self.payload,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Union["UpdateScheduledEvent", None]:
        if data:
            data_class = cls()
            data_class.event_id = data.get("event_id", None)
            data_class.payload = data.get("payload", None)

        return data_class
