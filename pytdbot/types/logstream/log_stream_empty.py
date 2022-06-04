from .base import LogStream


class LogStreamEmpty(LogStream):
    """The log is written nowhere."""

    def __init__(self) -> None:
        self.data = {"@type": "logStreamEmpty"}
