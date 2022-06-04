class Plugins:
    """Load the plugins folder and load the plugins.

    Args:
        folder (``str``):
            The folder to load the plugins from.

    Raises:
        TypeError
    """

    def __init__(self, folder: str) -> None:
        if not isinstance(folder, str):
            raise TypeError("folder must be a str")
        self.folder = folder
