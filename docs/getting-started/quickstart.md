# Quick start

Echo whatever people send you.

You need a bot token from [@BotFather](https://t.me/BotFather) and `api_id` / `api_hash` from [my.telegram.org](https://my.telegram.org/apps).

## Run this

```python
import asyncio
from pytdbot import Client, types

client = Client(
    token="BOT_TOKEN",
    api_id=0,
    api_hash="API_HASH",
    files_directory="BotDB",
    database_encryption_key="change-me",
)

@client.on_message()
async def on_msg(c: Client, message: types.Message):
    if message.text:
        await message.reply_text(message.text)

asyncio.run(client.run())
```

## What you just created

`files_directory` is TDLib’s database and file cache. One live client per directory.

`database_encryption_key` is required.

Prefer [`message.reply_text`][pytdbot.Message.reply_text] over raw [`sendMessage`][pytdbot.functions.sendMessage]. More shortcuts: [bound methods](../guides/bound-methods.md).

## Format text

```python
await message.reply_text("<b>hi</b>", parse_mode="html")
```

Parse modes are `"html"`, `"markdown"`, and `"markdownv2"`. Set a default with `default_parse_mode=` on [`Client`](../guides/client.md).

## Names follow TDLib

Methods look like [`getChat`][pytdbot.functions.getChat] and [`sendMessage`][pytdbot.functions.sendMessage]. If a name is unfamiliar, `python -m pytdbot.docs search "…"` or the [examples](../examples.md).
