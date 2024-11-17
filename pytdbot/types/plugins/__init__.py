__all__ = ("Plugins",)


class Plugins:
    """Load and filter plugins from a folder"""

    def __init__(self, folder: str, include: list = None, exclude: list = None) -> None:
        """
        Parameters:
            folder (``str``):
                The folder to load plugins from

            include (``list``, *optional*):
                Only load plugins with names in this list

            exclude (``list``, *optional*):
                Exclude plugins with names in this list

        Example:
            To load only the plugins with path "plugins/rules.py" and "plugins/subfolder1/commands.py",
            you should create the ``Plugins`` object like this:

            >>> plugins = Plugins(
                    folder="plugins/",
                    include=[
                        "rules" # will be translated to "plugins.rules"
                        "subfolder1.commands" # -> plugins.subfolder1.commands
                    ]
                )
        Raises:
            TypeError
        """

        if not isinstance(folder, str):
            raise TypeError("folder must be str")
        elif include is not None and not isinstance(include, list):
            raise TypeError("include must be list or None")
        elif exclude is not None and not isinstance(exclude, list):
            raise TypeError("include must be list or None")

        self.folder = folder
        self.include = include
        self.exclude = exclude
