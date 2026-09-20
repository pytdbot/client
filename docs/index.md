---
hide:
  - navigation
  - toc
---

<div class="hero" markdown>

# Pytdbot

<p class="lede" markdown>Python bots and userbots on [TDLib](https://github.com/tdlib/td) — async, typed, and a bit nicer than calling Telegram by hand.</p>

```bash
pip install pytdbot[tdjson]
```

[Quick start](getting-started/quickstart.md){ .md-button .md-button--primary }
[Guides](guides/client.md){ .md-button }

</div>

<div class="home-first" markdown>

## Your first bot

You need a token from [@BotFather](https://t.me/BotFather) and `api_id` / `api_hash` from [my.telegram.org](https://my.telegram.org/apps). `files_directory` is TDLib’s database — one live client per folder.

`/start` greets the sender by name, shows typing, then edits the message. The reply lives on the `Message` you already have.

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
async def start(c: Client, message: types.Message):
    if message.text != "/start":
        return

    sent = await message.reply_text(
        f"Hey {await message.mention(parse_mode='html')}",
        parse_mode="html",
    )
    async with message.action("typing"):
        await asyncio.sleep(1)
        await sent.edit_text("What can I do for you?")

asyncio.run(client.run())
```

From here: [sending](guides/sending.md), [keyboards](guides/keyboards.md), [plugins](guides/plugins.md). TDLib names (`getChat`, `sendMessage`) are in the [API reference](reference/index.md).

</div>

<div class="home-map" markdown>

<div markdown>

## Start here

Install, run a bot, or log in as a user.

[Install](getting-started/installation.md)  
[Quick start](getting-started/quickstart.md)  
[Userbot](getting-started/userbot.md)

</div>

<div markdown>

## Write a bot

Handlers, replies, buttons, plugins.

[Client](guides/client.md)  
[Handlers](guides/handlers.md)  
[Sending](guides/sending.md)  
[Keyboards](guides/keyboards.md)  
[Plugins](guides/plugins.md)

</div>

<div markdown>

## Look something up

Helpers, types, functions.

[Helpers](reference/helpers/index.md)  
[Types](reference/types/index.md)  
[Functions](reference/functions/index.md)

`python -m pytdbot.docs search "send photo"`

</div>

</div>
