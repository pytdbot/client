# Pytdbot

Easy, Sample and powerful [TDLib-based](https://github.com/tdlib/td) client for Telegram bots.

### Requirements

- python3.9+
- Telegram [API key](https://my.telegram.org/apps)
- [TDLib](https://github.com/tdlib/td#building) tdjson

### Installation

```bash
pip install pytdbot
```

### Examples
Basic example:
```python

from pytdbot import Client
from pytdbot.types import Update

client = Client(
    api_id=0,  
    api_hash="API_HASH",  
    database_encryption_key="1234echobot$",
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token. You can get it from https://t.me/botfather
    files_directory="BotDB",  # path where to store session and files.
)


@client.on_updateNewMessage()
async def print_message(c: Client, message: Update):
    print(message)


@client.on_updateNewMessage()
async def simple_message(c: Client, message: Update):
    await message.reply_text('Hi! i am simple bot')


# Run the client
client.run()

```
For more examples, check the [examples](https://github.com/pytdbot/client/tree/main/examples) folder.

# Contributing
Pull requests are always welcome!!
# License

MIT [License](https://github.com/pytdbot/client/blob/main/LICENSE)
