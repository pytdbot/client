from . import escape_html, escape_markdown


def bold(text: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to bold format

    Args:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return "<b>{}</b>".format(text if escape is False else escape_html(text))
    else:
        return "*{}*".format(text if escape is False else escape_markdown(text))


def italic(text: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to italic format

    Args:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return "<i>{}</i>".format(text if escape is False else escape_html(text))
    else:
        return "_{}_".format(text if escape is False else escape_markdown(text))


def underline(text: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to underline format

    Args:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return "<u>{}</u>".format(text if escape is False else escape_html(text))
    else:
        return "__{}__".format(text if escape is False else escape_markdown(text))


def strikethrough(text: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to strikethrough format

    Args:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return "<s>{}</s>".format(text if escape is False else escape_html(text))
    else:
        return "~{}~".format(text if escape is False else escape_markdown(text))


def spoiler(text: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to spoiler format

    Args:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return '<span class="tg-spoiler">{}</span>'.format(
            text if escape is False else escape_html(text)
        )
    else:
        return "||{}||".format(text if escape is False else escape_markdown(text))


def hyperlink(text: str, url: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to hyperlink format

    Args:
        text (``str``):
            The hyperlink text

        url (``str``):
            The hyperlink url

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    assert isinstance(url, str), "url must be str"

    if html:
        return '<a href="{}">{}</a>'.format(
            url, text if escape is False else escape_html(text)
        )
    else:
        return "[{}]({})".format(
            text if escape is False else escape_markdown(text), url
        )


def mention(text: str, user_id: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to inline mention format

    Args:
        text (``str``):
            The text of inline mention

        user_id (``str``):
            The inline user id to mention

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return '<a href="tg://user?id={}">{}</a>'.format(
            user_id, text if escape is False else escape_html(text)
        )
    else:
        return "[{}](tg://user?id={})".format(
            text if escape is False else escape_markdown(text), user_id
        )


def code(text: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to code format

    Args:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return "<code>{}</code>".format(text if escape is False else escape_html(text))
    else:
        return "`{}`".format(text if escape is False else escape_markdown(text))


def pre(text: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to pre format

    Args:
        text (``str``):
            The text to convert

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    if html:
        return "<pre>{}</pre>".format(text if escape is False else escape_html(text))
    else:
        return "```\n{}\n```".format(text if escape is False else escape_markdown(text))


def pre_code(text: str, language: str, html: bool = False, escape: bool = True) -> str:
    """Convert the given text to pre code format

    Args:
        text (``str``):
            The text to convert

        language (``str``):
            The name of the programming language written in the given code block

        html (``bool``, *optional*):
            Pass ``True`` to return text in ``html`` format. Defaults to ``False`` (``markdownv2``).

        escape (``bool``, *optional*):
            Whether escape special characters to the given text or not. Defaults to ``True``.

    Returns:
        :py:class:`str`: The formated text
    """

    assert isinstance(language, str), "text must be str"

    if html:
        return '<pre><code class="language-{}">{}</code></pre>'.format(
            language, text if escape is False else escape_html(text)
        )
    else:
        return "```{}\n{}\n```".format(
            language, text if escape is False else escape_markdown(text)
        )
