from __future__ import annotations

import pytdbot

from ..types import (
    MessageAnimation,
    MessageAudio,
    MessageDocument,
    MessagePhoto,
    MessageText,
    MessageVideo,
    MessageVoiceNote,
    MessageWidget,
)
from .escape import escape_html, escape_markdown

_CAPTION_CONTENT = (
    MessagePhoto,
    MessageVideo,
    MessageAnimation,
    MessageAudio,
    MessageDocument,
    MessageVoiceNote,
    MessageWidget,
)


def get_formatted_text(
    formatted_text: pytdbot.types.FormattedText,
    html: bool = True,
    escape: bool = True,
) -> str:
    r"""Convert a :class:`~pytdbot.types.FormattedText` object to its text representation string

    Parameters:
        formatted_text (:class:`~pytdbot.types.FormattedText`):
            The formatted text to convert

        html (``bool``, *optional*):
            If ``True``, returns HTML format, if ``False`` returns MarkdownV2. Default is ``True``

        escape (``bool``, *optional*):
            Whether to escape special characters in plain text segments. Default is ``True``

    Returns:
        :py:class:`str`: The formatted text representation
    """

    if not formatted_text or not formatted_text.text:
        return ""

    text = formatted_text.text
    entities = formatted_text.entities or []

    if not entities:
        return _escape_text(text, html, escape)

    events: list[tuple[int, int, int, int, str]] = []

    if text.isascii():
        length = len(text)

        for index, entity in enumerate(entities):
            if entity is None or entity.type is None:
                continue

            tags = _entity_tags(entity.type, html=html)
            if tags is None:
                continue

            start = entity.offset or 0
            end = start + (entity.length or 0)

            if start < 0 or start > length:
                continue

            end = min(end, length)
            if start >= end:
                continue

            open_tag, close_tag = tags
            events.append((start, 1, -end, index, open_tag))
            events.append((end, 0, -start, -index, close_tag))

        if not events:
            return _escape_text(text, html, escape)

        events.sort(key=_event_order)
        escape_func = (
            (escape_html if html else escape_markdown) if escape else (lambda s: s)
        )
        parts: list[str] = []
        last = 0

        for pos, _kind, _nest, _index, tag in events:
            if pos > last:
                parts.append(escape_func(text[last:pos]))
            parts.append(tag)
            last = pos

        if last < length:
            parts.append(escape_func(text[last:]))

        return "".join(parts)

    data = text.encode("utf-16-le", "surrogatepass")
    length = len(data)

    for index, entity in enumerate(entities):
        if entity is None or entity.type is None:
            continue

        tags = _entity_tags(entity.type, html=html)
        if tags is None:
            continue

        start = (entity.offset or 0) * 2
        end = start + (entity.length or 0) * 2

        if start < 0 or start > length:
            continue

        end = min(end, length)
        if start >= end:
            continue

        start_unit = int.from_bytes(data[start : start + 2], "little")
        if 0xDC00 <= start_unit < 0xE000:
            continue

        end_unit = int.from_bytes(data[end - 2 : end], "little")
        if 0xD800 <= end_unit < 0xDC00:
            continue

        open_tag, close_tag = tags
        events.append((start, 1, -end, index, open_tag))
        events.append((end, 0, -start, -index, close_tag))

    if not events:
        return _escape_text(text, html, escape)

    events.sort(key=_event_order)
    parts = []
    last = 0

    for pos, _kind, _nest, _index, tag in events:
        if pos > last:
            segment = data[last:pos].decode("utf-16-le", "surrogatepass")
            parts.append(_escape_text(segment, html, escape))
        parts.append(tag)
        last = pos

    if last < length:
        parts.append(
            _escape_text(data[last:].decode("utf-16-le", "surrogatepass"), html, escape)
        )

    return "".join(parts)


def message_to_html(message: pytdbot.types.Message, escape: bool = True) -> str:
    r"""Convert a message text or caption to its HTML representation

    Parameters:
        message (:class:`~pytdbot.types.Message`):
            The message to convert

        escape (``bool``, *optional*):
            Whether to escape special characters in plain text segments. Default is ``True``

    Returns:
        :py:class:`str`: The HTML formatted text, empty string if the message has no text or caption
    """

    content = message.content

    if isinstance(content, MessageText):
        return get_formatted_text(content.text, html=True, escape=escape)

    if isinstance(content, _CAPTION_CONTENT):
        return get_formatted_text(content.caption, html=True, escape=escape)

    return ""


def _escape_text(text: str, html: bool, escape: bool) -> str:
    if not escape:
        return text
    return escape_html(text) if html else escape_markdown(text)


def _event_order(event: tuple) -> tuple:
    return (event[0], event[1], event[2], event[3])


_DATE_FORMAT = {
    "dateTimePartPrecisionShort": "d",
    "dateTimePartPrecisionLong": "D",
}

_TIME_FORMAT = {
    "dateTimePartPrecisionShort": "t",
    "dateTimePartPrecisionLong": "T",
}


def _datetime_format(
    formatting_type: pytdbot.types.DateTimeFormattingType | None,
) -> str:
    r"""Build a date-time format string ``r|w?[dD]?[tT]?`` from TDLib formatting

    - ``r`` — relative to now (cannot combine with other controls)
    - ``w`` — day of week
    - ``d`` / ``D`` — short / long date
    - ``t`` / ``T`` — short / long time

    An empty string means show the underlying text as-is (client may still
    use the unix timestamp for local formatting).
    """

    if formatting_type is None:
        return ""

    t = pytdbot.types

    if isinstance(formatting_type, t.DateTimeFormattingTypeRelative):
        return "r"

    if isinstance(formatting_type, t.DateTimeFormattingTypeAbsolute):
        parts = "w" if formatting_type.show_day_of_week else ""

        if formatting_type.date_precision is not None:
            date_char = _DATE_FORMAT.get(formatting_type.date_precision.getType())
            if date_char:
                parts += date_char

        if formatting_type.time_precision is not None:
            time_char = _TIME_FORMAT.get(formatting_type.time_precision.getType())
            if time_char:
                parts += time_char

        return parts

    return ""


_HTML_TAGS = {
    "textEntityTypeBold": ("<b>", "</b>"),
    "textEntityTypeItalic": ("<i>", "</i>"),
    "textEntityTypeUnderline": ("<u>", "</u>"),
    "textEntityTypeStrikethrough": ("<s>", "</s>"),
    "textEntityTypeSpoiler": ('<span class="tg-spoiler">', "</span>"),
    "textEntityTypeCode": ("<code>", "</code>"),
    "textEntityTypePre": ("<pre>", "</pre>"),
    "textEntityTypeBlockQuote": ("<blockquote>", "</blockquote>"),
    "textEntityTypeExpandableBlockQuote": ("<blockquote expandable>", "</blockquote>"),
}

_MD_TAGS = {
    "textEntityTypeBold": ("*", "*"),
    "textEntityTypeItalic": ("_", "_"),
    "textEntityTypeUnderline": ("__", "__"),
    "textEntityTypeStrikethrough": ("~", "~"),
    "textEntityTypeSpoiler": ("||", "||"),
    "textEntityTypeCode": ("`", "`"),
    "textEntityTypePre": ("```\n", "\n```"),
    "textEntityTypeBlockQuote": (">", ""),
    "textEntityTypeExpandableBlockQuote": ("**>", ""),
}


def _pre_code_tags(
    entity_type: pytdbot.types.TextEntityTypePreCode, html: bool
) -> tuple[str, str]:
    language = entity_type.language or ""
    if html:
        return (f'<pre><code class="language-{language}">', "</code></pre>")
    return (f"```{language}\n", "\n```")


def _text_url_tags(
    entity_type: pytdbot.types.TextEntityTypeTextUrl, html: bool
) -> tuple[str, str]:
    url = entity_type.url or ""
    if html:
        return (f'<a href="{url}">', "</a>")
    return ("[", f"]({url})")


def _mention_name_tags(
    entity_type: pytdbot.types.TextEntityTypeMentionName, html: bool
) -> tuple[str, str]:
    user_id = entity_type.user_id or 0
    if html:
        return (f'<a href="tg://user?id={user_id}">', "</a>")
    return ("[", f"](tg://user?id={user_id})")


def _custom_emoji_tags(
    entity_type: pytdbot.types.TextEntityTypeCustomEmoji, html: bool
) -> tuple[str, str]:
    custom_emoji_id = entity_type.custom_emoji_id or 0
    if html:
        return (f'<tg-emoji emoji-id="{custom_emoji_id}">', "</tg-emoji>")
    return ("![", f"](tg://emoji?id={custom_emoji_id})")


def _date_time_tags(
    entity_type: pytdbot.types.TextEntityTypeDateTime, html: bool
) -> tuple[str, str] | None:
    if not html:
        return None

    unix_time = entity_type.unix_time or 0
    fmt = _datetime_format(entity_type.formatting_type)
    return (
        f'<tg-time unix="{unix_time}" format="{fmt}">',
        "</tg-time>",
    )


_PARAM_TAGS = {
    "textEntityTypePreCode": _pre_code_tags,
    "textEntityTypeTextUrl": _text_url_tags,
    "textEntityTypeMentionName": _mention_name_tags,
    "textEntityTypeCustomEmoji": _custom_emoji_tags,
    "textEntityTypeDateTime": _date_time_tags,
}


def _entity_tags(
    entity_type: pytdbot.types.TextEntityType, html: bool
) -> tuple[str, str] | None:
    r"""Return ``(open_tag, close_tag)`` for a text entity type, or ``None`` if plain"""

    name = entity_type.getType()

    tags = _HTML_TAGS.get(name) if html else _MD_TAGS.get(name)
    if tags is not None:
        return tags

    param = _PARAM_TAGS.get(name)
    return param(entity_type, html) if param else None


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

        custom_emoji_id (``int``):
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
