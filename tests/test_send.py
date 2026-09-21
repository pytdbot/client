import pytest
from pytdbot import types


@pytest.mark.asyncio(loop_scope="session")
async def test_send_edit_reply_delete(client, chat_id, assert_ok):
    sent = assert_ok(await client.sendTextMessage(chat_id, "pytdbot-test-1"))
    assert isinstance(sent, types.Message)
    assert sent.id

    edited = assert_ok(
        await client.editTextMessage(
            chat_id=chat_id, message_id=sent.id, text="pytdbot-test-2"
        )
    )
    assert isinstance(edited, types.Message)

    bound = assert_ok(await sent.edit_text("pytdbot-test-3"))
    assert isinstance(bound, types.Message)

    reply = assert_ok(await sent.reply_text("pytdbot-test-reply"))
    assert isinstance(reply, types.Message)

    deleted = assert_ok(
        await client.deleteMessages(
            chat_id=chat_id,
            message_ids=[sent.id, reply.id],
            revoke=True,
        )
    )
    assert isinstance(deleted, types.Ok)
