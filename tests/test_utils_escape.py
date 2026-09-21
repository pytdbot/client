import pytest
from pytdbot import utils


def test_escape_html():
    assert utils.escape_html("a&b<c>") == "a&amp;b&lt;c&gt;"
    assert utils.escape_html('"q"', quote=True) == "&quot;q&quot;"
    assert utils.escape_html('"q"', quote=False) == '"q"'


def test_escape_markdown_v2():
    assert utils.escape_markdown("a_b*", version=2) == r"a\_b\*"


def test_escape_markdown_v1():
    assert utils.escape_markdown("a_b*", version=1) == r"a\_b\*"


def test_escape_markdown_invalid_version():
    with pytest.raises(ValueError, match="Invalid version"):
        utils.escape_markdown("x", version=3)
