_SELF_CLOSING = frozenset({"img", "hr", "input", "tg-map"})
_TRUE_ONLY = frozenset(
    {"checked", "reversed", "open", "tg-spoiler", "bordered", "striped"}
)
_TRUE_ONLY_UNDER = {k.replace("-", "_"): k for k in _TRUE_ONLY}


def tag(tag_name, *children, **attrs):
    r"""Build an HTML tag string

    Parameters:
        tag_name (``str``):
            The HTML tag name

        \*children:
            Child elements to place inside the tag

        \*attrs:
            HTML attributes. Use ``True`` for boolean attributes.
            Use ``None`` or ``False`` to skip an attribute.

    Returns:
        :py:class:`str`: The rendered HTML tag
    """

    parts = []
    for k, v in attrs.items():
        if v is None or v is False:
            continue

        tk = _TRUE_ONLY_UNDER.get(k, k)
        if tk in _TRUE_ONLY and (v is True or v == ""):
            parts.append(tk)
        else:
            parts.append(f'{tk}="{v}"')

    attr_str = (" " + " ".join(parts)) if parts else ""
    content = "".join(children) if children else ""
    if not content and tag_name in _SELF_CLOSING:
        return f"<{tag_name}{attr_str}/>"

    return f"<{tag_name}{attr_str}>{content}</{tag_name}>"


def marked(text):
    r"""Wrap text in marked (highlighted) format

    Parameters:
        text (``str``):
            The text to convert

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("mark", text)


def subscript(text):
    r"""Wrap text in subscript format

    Parameters:
        text (``str``):
            The text to convert

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("sub", text)


def superscript(text):
    r"""Wrap text in superscript format

    Parameters:
        text (``str``):
            The text to convert

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("sup", text)


def anchor(name):
    r"""Create an empty anchor that can be linked to with :py:func:`in_doc_link`

    Parameters:
        name (``str``):
            The anchor name

    Returns:
        :py:class:`str`: The anchor tag
    """

    return tag("a", name=name)


def email_link(address, text):
    r"""Create an inline e-mail link

    Parameters:
        address (``str``):
            The e-mail address

        text (``str``):
            The display text

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("a", text, href=f"mailto:{address}")


def phone(number, text):
    r"""Create an inline phone number link

    Parameters:
        number (``str``):
            The phone number

        text (``str``):
            The display text

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("a", text, href=f"tel:{number}")


def in_doc_link(anchor, text):
    r"""Create an in-document link to an anchor created with :py:func:`anchor`

    Parameters:
        anchor (``str``):
            The anchor name to link to

        text (``str``):
            The display text

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("a", text, href=f"#{anchor}")


def tg_reference(name, text):
    r"""Define referenced text that can be linked to with :py:func:`in_doc_link`

    Parameters:
        name (``str``):
            The reference name

        text (``str``):
            The referenced text

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("tg-reference", text, name=name)


def tg_time(unix, format, text=""):
    r"""Create a date-time entity

    Parameters:
        unix (``int``):
            Unix timestamp

        format (``str``):
            Date-time format string

        text (``str``, *optional*):
            Fallback text. Default is ``""``

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("tg-time", text, unix=str(unix), format=format)


def tg_math(source):
    r"""Wrap text in inline math formula

    Parameters:
        source (``str``):
            LaTeX formula source

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("tg-math", source)


def tg_math_block(source):
    r"""Wrap text in a block math formula

    Parameters:
        source (``str``):
            LaTeX formula source

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("tg-math-block", source)


def heading(level, text, name=None):
    r"""Create a heading with an optional anchor

    Parameters:
        level (``int``):
            Heading level from 1 to 6

        text (``str``):
            The heading text

        name (``str``, *optional*):
            Anchor name for in-document linking. Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    h = tag(f"h{level}", text)
    return tag("a", name=name) + h if name else h


def paragraph(*children):
    r"""Create a paragraph block

    Parameters:
        \*children:
            Child elements

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("p", *children)


def footer(*children):
    r"""Create a footer block

    Parameters:
        \*children:
            Child elements

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("footer", *children)


def horizontal_rule():
    r"""Create a horizontal rule

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("hr")


def list_item(*children, value=None, checked=None, type=None):
    r"""Create a list item

    Parameters:
        \*children:
            Child elements

        value (``int``, *optional*):
            Explicit item number for ordered lists. Default is ``None``

        checked (``bool``, *optional*):
            Checkbox state. ``True`` for checked, ``False`` for unchecked.
            Default is ``None`` (no checkbox)

        type (``str``, *optional*):
            List item type marker (e.g. ``"i"``, ``"a"``). Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    if checked is not None:
        cb = tag("input", type="checkbox", checked=True if checked else None)
        li_attrs = {"value": str(value)} if value is not None else {}
        if type is not None:
            li_attrs["type"] = type

        return tag("li", cb, *children, **li_attrs)

    attrs = {}
    if value is not None:
        attrs["value"] = str(value)
    if type is not None:
        attrs["type"] = type

    return tag("li", *children, **attrs)


def _wrap_li(item):
    return item if isinstance(item, str) and item.startswith("<li") else tag("li", item)


def unordered_list(*items):
    r"""Create an unordered list

    Parameters:
        \*items:
            List items. Plain strings are automatically wrapped in ``<li>``

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("ul", *(_wrap_li(i) for i in items))


def ordered_list(*items, start=None, type=None, reversed=False):
    r"""Create an ordered list

    Parameters:
        \*items:
            List items. Plain strings are automatically wrapped in ``<li>``

        start (``int``, *optional*):
            Starting number. Default is ``None``

        type (``str``, *optional*):
            List marker type (e.g. ``"a"``, ``"i"``). Default is ``None``

        reversed (``bool``, *optional*):
            Whether the list is reversed. Default is ``False``

    Returns:
        :py:class:`str`: The formatted text
    """

    attrs = {}
    if start is not None:
        attrs["start"] = str(start)
    if type is not None:
        attrs["type"] = type
    if reversed:
        attrs["reversed"] = True

    return tag("ol", *(_wrap_li(i) for i in items), **attrs)


def blockquote(*children, cite=None):
    r"""Create a block quotation

    Parameters:
        \*children:
            Child elements

        cite (``str``, *optional*):
            Citation source. Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    inner = "".join(children)
    if cite is not None:
        inner += tag("cite", cite)

    return tag("blockquote", inner)


def aside(*children, cite=None):
    r"""Create a pull quote

    Parameters:
        \*children:
            Child elements

        cite (``str``, *optional*):
            Citation source. Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    inner = "".join(children)
    if cite is not None:
        inner += tag("cite", cite)

    return tag("aside", inner)


def image(src, alt=None, spoiler=False):
    r"""Create an image block

    Parameters:
        src (``str``):
            Image URL

        alt (``str``, *optional*):
            Alternative text. Default is ``None``

        spoiler (``bool``, *optional*):
            Whether the image is a spoiler. Default is ``False``

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("img", src=src, alt=alt, **({"tg-spoiler": True} if spoiler else {}))


def video(src, spoiler=False):
    r"""Create a video block

    Parameters:
        src (``str``):
            Video URL

        spoiler (``bool``, *optional*):
            Whether the video is a spoiler. Default is ``False``

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("video", src=src, **({"tg-spoiler": True} if spoiler else {}))


def audio(src):
    r"""Create an audio block

    Parameters:
        src (``str``):
            Audio URL

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("audio", src=src)


def figure(*children):
    r"""Create a figure block

    Parameters:
        \*children:
            Child elements (e.g. :py:func:`image`, :py:func:`video`, :py:func:`audio`, :py:func:`figcaption`)

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("figure", *children)


def figcaption(*children):
    r"""Create a figure caption

    Parameters:
        \*children:
            Child elements

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("figcaption", *children)


def tg_map(lat, long, zoom):
    r"""Create a map block

    Parameters:
        lat (``float``):
            Latitude

        long (``float``):
            Longitude

        zoom (``int``):
            Zoom level

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("tg-map", lat=str(lat), long=str(long), zoom=str(zoom))


def tg_collage(*children, caption=None):
    r"""Create a media collage

    Parameters:
        \*children:
            Media elements (e.g. :py:func:`image`, :py:func:`video`)

        caption (``str``, *optional*):
            Collage caption. Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    inner = "".join(children)
    if caption is not None:
        inner += tag("figcaption", caption)

    return tag("tg-collage", inner)


def tg_slideshow(*children, caption=None):
    r"""Create a media slideshow

    Parameters:
        \*children:
            Media elements (e.g. :py:func:`image`, :py:func:`video`)

        caption (``str``, *optional*):
            Slideshow caption. Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    inner = "".join(children)
    if caption is not None:
        inner += tag("figcaption", caption)

    return tag("tg-slideshow", inner)


def table_cell(*children, colspan=None, rowspan=None, align=None, valign=None):
    r"""Create a table data cell

    Parameters:
        \*children:
            Cell content

        colspan (``int``, *optional*):
            Number of columns to span. Default is ``None``

        rowspan (``int``, *optional*):
            Number of rows to span. Default is ``None``

        align (``str``, *optional*):
            Horizontal alignment (``"left"``, ``"center"``, ``"right"``). Default is ``None``

        valign (``str``, *optional*):
            Vertical alignment (``"top"``, ``"middle"``, ``"bottom"``). Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag(
        "td", *children, colspan=colspan, rowspan=rowspan, align=align, valign=valign
    )


def table_header_cell(*children, colspan=None, rowspan=None, align=None, valign=None):
    r"""Create a table header cell

    Parameters:
        \*children:
            Cell content

        colspan (``int``, *optional*):
            Number of columns to span. Default is ``None``

        rowspan (``int``, *optional*):
            Number of rows to span. Default is ``None``

        align (``str``, *optional*):
            Horizontal alignment (``"left"``, ``"center"``, ``"right"``). Default is ``None``

        valign (``str``, *optional*):
            Vertical alignment (``"top"``, ``"middle"``, ``"bottom"``). Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag(
        "th", *children, colspan=colspan, rowspan=rowspan, align=align, valign=valign
    )


def table_row(*cells):
    r"""Create a table row

    Parameters:
        \*cells:
            Cell elements

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag("tr", *cells)


def table_header(*cells):
    r"""Create a table header row with ``<th>`` cells

    Parameters:
        \*cells:
            Header cell values

    Returns:
        :py:class:`str`: The formatted text
    """

    return tag(
        "tr",
        *(
            c if isinstance(c, str) and c.startswith("<th") else tag("th", c)
            for c in cells
        ),
    )


def table(*rows, bordered=False, striped=False, caption=None):
    r"""Create a table

    Parameters:
        \*rows:
            Table rows

        bordered (``bool``, *optional*):
            Whether the table has borders. Default is ``False``

        striped (``bool``, *optional*):
            Whether the table has striped rows. Default is ``False``

        caption (``str``, *optional*):
            Table caption. Default is ``None``

    Returns:
        :py:class:`str`: The formatted text
    """

    inner = (tag("caption", caption) if caption else "") + "".join(rows)

    attrs = {}
    if bordered:
        attrs["bordered"] = ""
    if striped:
        attrs["striped"] = ""

    return tag("table", inner, **attrs)


def details(*children, summary, open=False):
    r"""Create a collapsible details block

    Parameters:
        \*children:
            Content shown when expanded

        summary (``str``):
            Summary text displayed when collapsed

        open (``bool``, *optional*):
            Whether the block is expanded by default. Default is ``False``

    Returns:
        :py:class:`str`: The formatted text
    """

    content = tag("summary", summary) + "".join(children)
    return tag("details", content, **({"open": True} if open else {}))
