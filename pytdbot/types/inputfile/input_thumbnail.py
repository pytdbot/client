from .input_file_local import InputFileLocal


class InputThumbnail:
    """A thumbnail to be sent along with a file; must be in JPEG or WEBP format for stickers, and less than 200 KB in size

    Args:
        f (:class:`~pytdbot.types.InputFileLocal`):
            Thumbnail file to send

        width (``int``, *optional*):
            Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown. Default is ``0``

        height (``int``, *optional*):
            Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown. Default is ``0``
    """

    def __init__(self, f: InputFileLocal, width: int = 0, height: int = 0) -> None:
        self.f = f
        self.width = width
        self.height = height

    def to_dict(self):
        """Convert this object to a dict."""
        return {
            "thumbnail": self.f.to_dict(),
            "width": self.width,
            "height": self.height,
        }
