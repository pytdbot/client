from html import escape as _h_escape
from re import escape as _re_escape, sub


def escape_html(text: str, quote: bool = True) -> str:
    """Escape HTML characters in the given text.

    Args:
        text (``str``): The text to escape.
        quote (``bool``, optional): Whether to escape double quotes. Defaults to True.

    Returns:
        ``str``: The escaped text.
    """
    return _h_escape(text, quote=quote)


def escape_markdown(text: str, version: int = 1) -> str:
    """Escape Markdown characters in the given text.

    Args:
        text (``str``): The text to escape.
        version (``int``, optional): The Markdown version to escape. Defaults to 1.

    Returns:
        ``str``: The escaped text.

    Raises:
        ``ValueError``: If the given markdown version is not supported.
    """
    if version == 1:
        chars = _re_escape(r"_\*`\[")
    elif version == 2:
        chars = _re_escape(r"\_*[]()~`>#+-=|{}.!")
    else:
        raise ValueError("Invalid version. Must be 1 or 2.")

    return sub("([{}])".format(chars), r"\\\1", text)
