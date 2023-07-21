from pathlib import Path, PosixPath
from typing import Union
from .base import LogStream


class LogStreamFile(LogStream):
    """The log is written to a file

    Args:
        path (:py:class:`pathlib.PosixPath` | ``str``):
            Path to the file to where the internal TDLib log will be written

        max_file_size (``int``, *optional*):
            The maximum size of the file to where the internal TDLib log is written before the file will automatically be rotated, in bytes. Default is ``104857600`` (100MB)

        redirect_stderr (``bool``, *optional*):
            Pass true to additionally redirect stderr to the log file. Ignored on Windows. Default is ``False``
    """

    def __init__(
        self,
        path: Union[str, PosixPath],
        max_file_size: int = 104857600,
        redirect_stderr: bool = False,
    ) -> None:
        self.path = path
        self.max_file_size = max_file_size
        self.redirect_stderr = redirect_stderr

        if isinstance(self.path, PosixPath):
            self.path = str(self.path.resolve())
        else:
            self.path = str(Path(self.path).resolve())

        self.data = {
            "@type": "logStreamFile",
            "path": self.path,
            "max_file_size": self.max_file_size,
            "redirect_stderr": self.redirect_stderr,
        }
