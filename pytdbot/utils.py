from html import escape as _html_escape
from re import escape as _re_escape, compile as _re_compile


def escape_html(text: str, quote: bool = True) -> str:
    """Escape HTML characters in the given text.

    Args:
        text (``str``):
            The text to escape.

        quote (``bool``, optional):
            Whether to escape double quotes. Defaults to True.

    Returns:
        ``str``: The escaped text.
    """
    assert isinstance(text, str), "text must be a string"
    assert isinstance(quote, bool), "quote must be a boolean"

    return _html_escape(text, quote=quote)


special_chars_v1 = _re_compile("([{}])".format(_re_escape(r"_\*`\[")))
special_chars_v2 = _re_compile("([{}])".format(_re_escape(r"\_*[]()~`>#+-=|{}.!")))


def escape_markdown(text: str, version: int = 1) -> str:
    """Escape Markdown characters in the given text.

    Args:
        text (``str``):
            The text to escape.

        version (``int``, optional):
            The Markdown version to escape. Defaults to 1.

    Returns:
        ``str``: The escaped text.

    Raises:
        ``ValueError``: If the given markdown version is not supported.
    """
    assert isinstance(text, str), "text must be a string"

    if version == 1:
        chars = special_chars_v1
    elif version == 2:
        chars = special_chars_v2
    else:
        raise ValueError("Invalid version. Must be 1 or 2.")

    return chars.sub(r"\\\1", text)
