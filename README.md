# Pytdbot [![Version](https://img.shields.io/pypi/v/Pytdbot?style=flat&logo=pypi)](https://pypi.org/project/Pytdbot) [![TDLib version](https://img.shields.io/badge/TDLib-v1.8.47-blue?logo=telegram)](https://github.com/tdlib/td) [![Downloads](https://static.pepy.tech/personalized-badge/pytdbot?period=month&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/pytdbot) [![Telegram Chat](https://img.shields.io/badge/Pytdbot%20chat-blue?logo=telegram&label=Telegram)](https://t.me/pytdbotchat)

Pytdbot (Python TDLib) is an asynchronous [**TDLib**](https://github.com/tdlib/td) wrapper for **Telegram** users/bots written in **Python**.

### Features

`Pytdbot` offers numerous advantages, including:

- **Easy to Use**: Designed with simplicity in mind, making it accessible for developers
- **Performance**: Fast and powerful, making it ready to fight
- **Asynchronous**: Fully asynchronous that allows for non-blocking requests and improved responsiveness
- **Scalable**: Easily scalable using [TDLib Server](https://github.com/pytdbot/tdlib-server)
- **Well-typed**: Provides clear and well-defined methods and types to enhance developer experience
- **Decorator-Based Updates**: Simplifies the implementation of update handlers through a decorator pattern
- **Bound Methods**: Features types bound methods for improved usability
- **Unlimited Support**: Supports **Plugins**, [**filters**](pytdbot/filters.py#L23), [**TDLib**](https://github.com/tdlib/td) types/functions and much more

### Requirements

- Python 3.9+
- Telegram [API key](https://my.telegram.org/apps)
- [tdjson](https://github.com/AYMENJD/tdjson) or [TDLib](https://github.com/tdlib/td#building)
- [deepdiff](https://github.com/seperman/deepdiff)
- [aio-pika](https://github.com/mosquito/aio-pika)

### Installation

> For better performance, it's recommended to install [orjson](https://github.com/ijl/orjson#install) or [ujson](https://github.com/ultrajson/ultrajson#ultrajson).

You can install Pytdbot with TDLib included using pip:

```bash
pip install --upgrade pytdbot[tdjson]
```

If the installation fails, then install without **pre-built** TDLib:

```bash
pip install pytdbot
```

Then you need to build TDLib from [source](https://github.com/tdlib/td#building) and pass it to `Client.lib_path`.

You could also install the development version using the following command:

```bash
pip install --pre pytdbot
```

### Examples

Basic example:

```python

import asyncio

from pytdbot import Client, types

client = Client(
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token
    api_id=0,
    api_hash="API_HASH",
    files_directory="BotDB",  # Path where to store TDLib files
    database_encryption_key="1234echobot$",
    td_verbosity=2,  # TDLib verbosity level
    td_log=types.LogStreamFile("tdlib.log", 104857600),  # Set TDLib log file path
)


@client.on_updateNewMessage()
async def print_message(c: Client, message: types.UpdateNewMessage):
    print(message)


@client.on_message()
async def say_hello(c: Client, message: types.Message):
    msg = await message.reply_text(f"Hey {await message.mention(parse_mode='html')}! I'm cooking up a surprise... 🍳👨‍🍳", parse_mode="html")

    async with message.action("choose_sticker"):
        await asyncio.sleep(5)

        await msg.edit_text("Boo! 👻 Just kidding.")



# Run the client
client.run()

```

For more examples, check the [examples](https://github.com/pytdbot/client/tree/main/examples) folder.

# Thanks to

- You for viewing or using this project.

- [@levlam](https://github.com/levlam) for maintaining [TDLib](https://github.com/tdlib/td) and for the help to create [Pytdbot](https://github.com/pytdbot/client).

# License

MIT [License](https://github.com/pytdbot/client/blob/main/LICENSE)
