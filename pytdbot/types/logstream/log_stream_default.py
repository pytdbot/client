from .base import LogStream


class LogStreamDefault(LogStream):
    """The log is written to stderr or an OS specific log."""

    def __init__(self) -> None:
        self.data = {"@type": "logStreamDefault"}
