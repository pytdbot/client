# Pytdbot [![version](https://img.shields.io/pypi/v/Pytdbot?style=flat&logo=pypi)](https://pypi.org/project/Pytdbot) [![downloads](https://img.shields.io/pypi/dm/Pytdbot?style=flat)](https://pypistats.org/packages/pytdbot)

Easy, Sample and powerful [TDLib-based](https://github.com/tdlib/td) client for Telegram bots.

### Requirements

- python3.9+
- Telegram [API key](https://my.telegram.org/apps)
- [tdjson](https://github.com/tdlib/td#building)
- [deepdiff](https://github.com/seperman/deepdiff)
- [ujson](https://github.com/ultrajson/ultrajson)

### Installation

```bash
pip install pytdbot
```
From github
```bash
pip install git+https://github.com/pytdbot/client.git
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
    lib_path="/path/to/libtdjson.so" # Path to TDjson shared library.
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
