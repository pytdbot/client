from html import escape as _html_escape


def escape_html(text: str, quote: bool = True) -> str:
    r"""Escape HTML characters in the given text

    Parameters:
        text (``str``):
            The text to escape

        quote (``bool``, *optional*):
            Whether to escape double quotes. Default is ``True``

    Returns:
        :py:class:`str`: The escaped text
    """

    return _html_escape(text, quote=quote)


special_chars_v1 = r"_\*`\["
special_chars_v2 = r"\_*[]()~`>#+-=|{}.!"


def escape_markdown(text: str, version: int = 2) -> str:
    r"""Escape Markdown characters in the given text

    Parameters:
        text (``str``):
            The text to escape

        version (``int``, *optional*):
            The Markdown version to escape. Default is ``2``

    Returns:
        :py:class:`str`: The escaped text

    Raises:
        :py:class:`ValueError`: If the given markdown version is not supported
    """

    if version == 1:
        chars = special_chars_v1
    elif version == 2:
        chars = special_chars_v2
    else:
        raise ValueError("Invalid version. Must be 1 or 2.")

    return "".join("\\" + c if c in chars else c for c in text)
