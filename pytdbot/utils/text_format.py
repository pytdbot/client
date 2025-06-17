from . import escape_html, escape_markdown


def bold(text: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to bold format

    Parameters:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f"<b>{text if escape is False else escape_html(str(text))}</b>"

    return f"*{text if escape is False else escape_markdown(str(text))}*"


def italic(text: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to italic format

    Parameters:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f"<i>{text if escape is False else escape_html(str(text))}</i>"

    return f"_{text if escape is False else escape_markdown(str(text))}_"


def underline(text: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to underline format

    Parameters:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f"<u>{text if escape is False else escape_html(str(text))}</u>"

    return f"__{text if escape is False else escape_markdown(str(text))}__"


def strikethrough(text: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to strikethrough format

    Parameters:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f"<s>{text if escape is False else escape_html(str(text))}</s>"

    return f"~{text if escape is False else escape_markdown(str(text))}~"


def spoiler(text: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to spoiler format

    Parameters:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f'<span class="tg-spoiler">{text if escape is False else escape_html(f"{text}")}</span>'

    return f"||{text if escape is False else escape_markdown(str(text))}||"


def hyperlink(text: str, url: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to hyperlink format

    Parameters:
        text (``str``):
            The hyperlink text

        url (``str``):
            The hyperlink url

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    assert isinstance(url, str), "url must be str"

    if html:
        return (
            f'<a href="{url}">{text if escape is False else escape_html(f"{text}")}</a>'
        )

    return f"[{text if escape is False else escape_markdown(str(text))}]({url})"


def mention(text: str, user_id: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to inline mention format

    Parameters:
        text (``str``):
            The text of inline mention

        user_id (``str``):
            The inline user id to mention

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f'<a href="tg://user?id={user_id}">{text if escape is False else escape_html(f"{text}")}</a>'

    return f"[{text if escape is False else escape_markdown(str(text))}](tg://user?id={user_id})"


def custom_emoji(emoji: str, custom_emoji_id: int, html: bool = True) -> str:
    r"""Convert the given emoji to custom emoji format

    Parameters:
        emoji (``str``):
            The emoji of the custom emoji

        custom_emoji_id (``str``):
            Identifier of the custom emoji

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f'<tg-emoji emoji-id="{custom_emoji_id}">{emoji}</tg-emoji>'

    return f"![{emoji}](tg://emoji?id={custom_emoji_id})"


def code(text: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to code format

    Parameters:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f"<code>{text if escape is False else escape_html(str(text))}</code>"

    return f"`{text if escape is False else escape_markdown(str(text))}`"


def pre(text: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to pre format

    Parameters:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f"<pre>{text if escape is False else escape_html(str(text))}</pre>"

    return f"```\n{text if escape is False else escape_markdown(str(text))}\n```"


def pre_code(text: str, language: str, html: bool = True, escape: bool = True) -> str:
    r"""Convert the given text to pre-formatted fixed-width code block

    Parameters:
        text (``str``):
            The text to convert

        language (``str``):
            The name of the programming language written in the given code block

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    assert isinstance(language, str), "text must be str"

    if html:
        return f'<pre><code class="language-{language}">{text if escape is False else escape_html(f"{text}")}</code></pre>'

    return (
        f"```{language}\n{text if escape is False else escape_markdown(str(text))}\n```"
    )


def quote(text: str, expandable: bool = False, html: bool = True, escape: bool = True):
    r"""Convert the given text to quote block

    Parameters:
        text (``str``):
            The text to convert

        expandable (``bool``, *optional*):
            Wether the quote is expandable or not. Default is ``False``

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Default is ``True``

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return f"<blockquote{' expandable' if expandable else ''}>{text if escape is False else escape_html(str(text))}</blockquote>"

    return f"{'**' if expandable else ''}>{text if escape is False else escape_markdown(str(text))}"


rtl_mark = "\u200f"
ltr_mark = "\u200e"


def rtl(text: str) -> str:
    r"""Add RTL (Right-to-Left) mark to the given text

    Parameters:
        text (``str``):
            The text to convert

    Returns:
        :py:class:`str`: The formated text
    """

    return f"{rtl_mark}{text}"


def ltr(text: str) -> str:
    r"""Add LTR (Left-to-Right) mark to the given text

    Parameters:
        text (``str``):
            The text to convert

    Returns:
        :py:class:`str`: The formated text
    """

    return f"{ltr_mark}{text}"
