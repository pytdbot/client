import pytest
from pytdbot import types


@pytest.mark.asyncio(loop_scope="session")
async def test_authenticates(client):
    assert client.is_authenticated
    assert isinstance(client.me, types.User)
    assert client.me.id


@pytest.mark.asyncio(loop_scope="session")
async def test_get_me(client, assert_ok):
    me = assert_ok(await client.getMe())
    assert isinstance(me, types.User)
    assert me.id == client.me.id


@pytest.mark.asyncio(loop_scope="session")
async def test_get_option_version(client, assert_ok):
    option = assert_ok(await client.getOption(name="version"))
    assert isinstance(option, types.OptionValueString)
    assert option.value


@pytest.mark.asyncio(loop_scope="session")
async def test_parse_text(client, assert_ok):
    parsed = assert_ok(await client.parseText("<b>hi</b>", parse_mode="html"))
    assert isinstance(parsed, types.FormattedText)
    assert parsed.text == "hi"
    assert parsed.entities
