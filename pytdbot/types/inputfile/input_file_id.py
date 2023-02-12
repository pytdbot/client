from .base import InputFile


class InputFileId(InputFile):
    """A file defined by its unique ID

    Args:
        id (``int``):
            The unique ID of the file
    """

    def __init__(self, id: str) -> None:
        self.id = id
        self.data = {"@type": "inputFileId", "id": self.id}
