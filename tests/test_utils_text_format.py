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
