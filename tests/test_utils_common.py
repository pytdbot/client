from pytdbot import types, utils


def test_get_message_sender_id_user():
    sender = types.MessageSenderUser(user_id=42)
    assert utils.get_message_sender_id(sender) == 42


def test_get_message_sender_id_chat():
    sender = types.MessageSenderChat(chat_id=-100)
    assert utils.get_message_sender_id(sender) == -100
