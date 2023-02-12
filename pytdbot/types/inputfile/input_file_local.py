from pathlib import Path, PosixPath
from typing import Union
from .base import InputFile


class InputFileLocal(InputFile):
    """A file defined by a local path

    Args:
        path (:py:class:`pathlib.PosixPath` | ``str``):
            The path to the file

    """

    def __init__(self, path: Union[str, PosixPath]) -> None:
        self.path = path
        if isinstance(self.path, PosixPath):
            self.path = str(self.path.resolve())
        else:
            self.path = str(Path(self.path).resolve())
        self.data = {"@type": "inputFileLocal", "path": self.path}
