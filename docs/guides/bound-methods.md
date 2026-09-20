# Bound methods

Types carry shortcuts so you do not rebuild TDLib requests by hand.

| On | Examples |
| --- | --- |
| [`Message`][pytdbot.types.Message] | [`text`][pytdbot.Message.text], [`caption`][pytdbot.Message.caption], [`from_id`][pytdbot.Message.from_id], [`reply_text`][pytdbot.Message.reply_text], [`reply_photo`][pytdbot.Message.reply_photo], [`edit_text`][pytdbot.Message.edit_text], [`action`][pytdbot.Message.action], [`mention`][pytdbot.Message.mention] |
| [`File`][pytdbot.types.File] | [`download`][pytdbot.File.download], [`delete`][pytdbot.File.delete] |
| [`UpdateNewCallbackQuery`][pytdbot.types.UpdateNewCallbackQuery] | [`answer`][pytdbot.UpdateNewCallbackQuery.answer], [`edit_message_text`][pytdbot.UpdateNewCallbackQuery.edit_message_text] |

```python
@client.on_message()
async def echo(c: Client, message: types.Message):
    if isinstance(message.content, types.MessageText):
        await message.reply_text(message.text, entities=message.entities)
    elif isinstance(message.content, types.MessagePhoto):
        await message.reply_photo(message.remote_file_id, caption=message.caption)
```

[`remote_file_id`][pytdbot.Message.remote_file_id] is a `str` remote id ([`InputFileRemote`][pytdbot.types.InputFileRemote]). A local file is [`InputFileLocal`][pytdbot.types.InputFileLocal] with `path=`. See [Sending](sending.md).

Full list: [helper reference](../reference/helpers/index.md).
