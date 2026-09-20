# Sending messages

Two layers, same TDLib underneath:

1. **Bound methods** on the message — [`reply_text`][pytdbot.Message.reply_text], [`reply_photo`][pytdbot.Message.reply_photo], … (preferred)
2. **Client helpers** — [`sendTextMessage`][pytdbot.Client.sendTextMessage], [`sendPhoto`][pytdbot.Client.sendPhoto], [`sendAlbum`][pytdbot.Client.sendAlbum], [`parseText`][pytdbot.Client.parseText]

```python
await message.reply_text("Hello", parse_mode="html")
await client.sendPhoto(
    chat_id,
    photo=types.InputFileLocal(path="cat.jpg"),
    caption="Hi",
)
```

`photo=` (and the same on video, document, …) is an [`InputFile`][pytdbot.classes.InputFile], or a `str` **remote file id** — a string is wrapped as [`InputFileRemote`][pytdbot.types.InputFileRemote]. A local file is [`InputFileLocal`][pytdbot.types.InputFileLocal] with `path=`. A filename string is not a local file.

## Text

[`reply_text`][pytdbot.Message.reply_text] / [`sendTextMessage`][pytdbot.Client.sendTextMessage] take `parse_mode` (`html`, `markdown`, `markdownv2`) or a default on the [Client](client.md).

Build HTML with [`pytdbot.utils`](utils.md):

```python
from pytdbot import utils

text = f"Hello {utils.bold(name)}"
await message.reply_text(text, parse_mode="html")
```

## Media and albums

```python
await message.reply_photo(
    types.InputFileLocal(path="cat.jpg"),
    caption="cat",
)
await message.reply_photo(message.remote_file_id, caption=message.caption)

await message.reply_album(
    [
        types.InputMessagePhoto(
            photo=types.InputPhoto(photo=types.InputFileLocal(path="a.jpg")),
        ),
        types.InputMessagePhoto(
            photo=types.InputPhoto(photo=types.InputFileLocal(path="b.jpg")),
        ),
    ]
)
```

[`reply_album`][pytdbot.Message.reply_album] / [`sendAlbum`][pytdbot.Client.sendAlbum] take a list of [`InputMessagePhoto`][pytdbot.types.InputMessagePhoto] / [`InputMessageVideo`][pytdbot.types.InputMessageVideo] / [`InputMessageAudio`][pytdbot.types.InputMessageAudio] / [`InputMessageDocument`][pytdbot.types.InputMessageDocument] / [`InputMessageAnimation`][pytdbot.types.InputMessageAnimation] — not paths.

## Typing

```python
async with message.action("typing"):
    await asyncio.sleep(1)
    await message.reply_text("Done")
```

[`action`][pytdbot.Message.action] is a context manager (or `await message.action("typing")`).

## Rich messages

A separate format. See [Rich messages](rich-messages.md) — do not mix them with [`ReplyMarkupInlineKeyboard`][pytdbot.types.ReplyMarkupInlineKeyboard] unless you mean to.
