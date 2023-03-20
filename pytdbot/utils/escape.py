from html import escape as _html_escape
from re import escape as _re_escape, compile as _re_compile


def escape_html(text: str, quote: bool = True) -> str:
    """Escape HTML characters in the given text

    Args:
        text (``str``):
            The text to escape

        quote (``bool``, *optional*):
            Whether to escape double quotes. Defaults to ``True``

    Returns:
        :py:class:`str`: The escaped text
    """

    return _html_escape(text, quote=quote)


special_chars_v1 = _re_compile("([{}])".format(_re_escape(r"_\*`\[")))
special_chars_v2 = _re_compile("([{}])".format(_re_escape(r"\_*[]()~`>#+-=|{}.!")))


def escape_markdown(text: str, version: int = 2) -> str:
    """Escape Markdown characters in the given text

    Args:
        text (``str``):
            The text to escape

        version (``int``, *optional*):
            The Markdown version to escape. Defaults to ``2``

    Returns:
        :py:class:`str`: The escaped text

    Raises:
        :py:class:`ValueError`: If the given markdown version is not supported.
    """

    if version == 1:
        chars = special_chars_v1
    elif version == 2:
        chars = special_chars_v2
    else:
        raise ValueError("Invalid version. Must be 1 or 2.")

    return chars.sub(r"\\\1", text)
