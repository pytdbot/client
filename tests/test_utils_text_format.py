import pytest
from pytdbot import types, utils


@pytest.mark.parametrize(
    ("fn", "html", "md"),
    [
        (utils.bold, "<b>hi</b>", "*hi*"),
        (utils.italic, "<i>hi</i>", "_hi_"),
        (utils.underline, "<u>hi</u>", "__hi__"),
        (utils.strikethrough, "<s>hi</s>", "~hi~"),
        (utils.spoiler, '<span class="tg-spoiler">hi</span>', "||hi||"),
        (utils.code, "<code>hi</code>", "`hi`"),
        (utils.pre, "<pre>hi</pre>", "```\nhi\n```"),
    ],
)
def test_text_wrappers(fn, html, md):
    assert fn("hi") == html
    assert fn("hi", html=False) == md


def test_hyperlink():
    assert utils.hyperlink("x", "https://t.me") == '<a href="https://t.me">x</a>'
    assert utils.hyperlink("x", "https://t.me", html=False) == "[x](https://t.me)"


def test_mention():
    assert utils.mention("me", "1") == '<a href="tg://user?id=1">me</a>'
    assert utils.mention("me", "1", html=False) == "[me](tg://user?id=1)"


def test_custom_emoji():
    assert utils.custom_emoji("😀", 9) == '<tg-emoji emoji-id="9">😀</tg-emoji>'
    assert utils.custom_emoji("😀", 9, html=False) == "![😀](tg://emoji?id=9)"


def test_pre_code():
    assert (
        utils.pre_code("x = 1", "py")
        == '<pre><code class="language-py">x = 1</code></pre>'
    )
    assert utils.pre_code("x = 1", "py", html=False) == "```py\nx \\= 1\n```"


def test_quote():
    assert utils.quote("hi") == "<blockquote>hi</blockquote>"
    assert (
        utils.quote("hi", expandable=True) == "<blockquote expandable>hi</blockquote>"
    )
    assert utils.quote("hi", html=False) == ">hi"
    assert utils.quote("hi", expandable=True, html=False) == "**>hi"


def test_rtl_ltr():
    assert utils.rtl("ar") == "\u200far"
    assert utils.ltr("en") == "\u200een"


def test_escape_inside_bold():
    assert utils.bold("a&b") == "<b>a&amp;b</b>"
    assert utils.bold("a&b", escape=False) == "<b>a&b</b>"


def test_get_formatted_text_plain():
    ft = types.FormattedText(text="hello")
    assert utils.get_formatted_text(ft) == "hello"
    assert utils.get_formatted_text(types.FormattedText(text="")) == ""


def test_get_formatted_text_bold():
    ft = types.FormattedText(
        text="hello",
        entities=[
            types.TextEntity(offset=0, length=5, type=types.TextEntityTypeBold())
        ],
    )
    assert utils.get_formatted_text(ft) == "<b>hello</b>"
    assert utils.get_formatted_text(ft, html=False) == "*hello*"


def test_get_formatted_text_utf16_offsets():
    ft = types.FormattedText(
        text="👋hi friend",
        entities=[
            types.TextEntity(offset=2, length=2, type=types.TextEntityTypeBold())
        ],
    )
    assert utils.get_formatted_text(ft) == "👋<b>hi</b> friend"


def test_get_formatted_text_nested():
    ft = types.FormattedText(
        text="hello world",
        entities=[
            types.TextEntity(offset=0, length=11, type=types.TextEntityTypeBold()),
            types.TextEntity(
                offset=6,
                length=5,
                type=types.TextEntityTypeTextUrl(url="https://example.com"),
            ),
        ],
    )
    assert (
        utils.get_formatted_text(ft)
        == '<b>hello <a href="https://example.com">world</a></b>'
    )


def test_get_formatted_text_skips_none_entities():
    ft = types.FormattedText(
        text="hello",
        entities=[
            None,
            types.TextEntity(offset=0, length=5, type=types.TextEntityTypeBold()),
        ],
    )
    assert utils.get_formatted_text(ft) == "<b>hello</b>"


def test_get_formatted_text_lone_surrogate():
    ft = types.FormattedText(
        text="a\ud800b",
        entities=[
            types.TextEntity(offset=0, length=1, type=types.TextEntityTypeBold())
        ],
    )
    assert utils.get_formatted_text(ft) == "<b>a</b>\ud800b"


def test_get_formatted_text_escaped_plain():
    ft = types.FormattedText(text="a<b & c")
    assert utils.get_formatted_text(ft) == "a&lt;b &amp; c"
    assert utils.get_formatted_text(ft, escape=False) == "a<b & c"


def test_get_formatted_text_adjacent():
    ft = types.FormattedText(
        text="abcdef",
        entities=[
            types.TextEntity(offset=0, length=3, type=types.TextEntityTypeBold()),
            types.TextEntity(offset=3, length=3, type=types.TextEntityTypeItalic()),
        ],
    )
    assert utils.get_formatted_text(ft) == "<b>abc</b><i>def</i>"


def test_message_to_html():
    text = types.FormattedText(
        text="hi",
        entities=[
            types.TextEntity(offset=0, length=2, type=types.TextEntityTypeBold())
        ],
    )
    message = types.Message(
        content=types.MessageText(text=text, link_preview_options=None)
    )
    assert utils.message_to_html(message) == "<b>hi</b>"
    assert utils.message_to_html(types.Message()) == ""


def test_message_to_html_caption():
    caption = types.FormattedText(
        text="a & b",
        entities=[
            types.TextEntity(offset=4, length=1, type=types.TextEntityTypeBold())
        ],
    )
    message = types.Message(
        content=types.MessagePhoto(
            photo=None,
            video=None,
            caption=caption,
            show_caption_above_media=False,
            has_spoiler=False,
            is_secret=False,
        )
    )
    assert utils.message_to_html(message) == "a &amp; <b>b</b>"
    widget = types.Message(
        content=types.MessageWidget(
            width=0,
            height=0,
            html="",
            public_data="",
            chat_data="",
            widget_id=0,
            caption=caption,
            show_caption_above_media=False,
            is_copy=False,
            can_send_queries=False,
            can_send_background_queries=False,
        )
    )
    assert utils.message_to_html(widget) == "a &amp; <b>b</b>"
    assert widget.caption == "a & b"
    assert (
        utils.message_to_html(
            types.Message(
                content=types.MessagePhoto(
                    photo=None,
                    video=None,
                    caption=types.FormattedText(text=""),
                    show_caption_above_media=False,
                    has_spoiler=False,
                    is_secret=False,
                )
            )
        )
        == ""
    )
