# Pytdbot [![Version](https://img.shields.io/pypi/v/Pytdbot?style=flat&logo=pypi)](https://pypi.org/project/Pytdbot) [![TDLib version](https://img.shields.io/badge/TDLib-v1.8.22-blue?logo=telegram)](https://github.com/tdlib/td) [![Downloads](https://static.pepy.tech/personalized-badge/pytdbot?period=month&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/pytdbot)

Pytdbot (Python TDLib) is an asynchronous [**TDLib**](https://github.com/tdlib/td) wrapper for **Telegram** users/bots written in **Python**.  

### Features
- Easy, **Fast** and **Powerful**
- Fully **asynchronous**
- **Decorator** based update handler
- **Bound** methods
- Supports **userbots**, **Plugins**, [**Filters**](https://github.com/pytdbot/client/blob/ad33d05d3e48bc8842b3986613ad2d99480a1fa8/pytdbot/filters.py#L23), [**TDLib**](https://github.com/tdlib/td) functions and much more.


### Requirements

- Python 3.9+
- Telegram [API key](https://my.telegram.org/apps)
- [tdjson](https://github.com/tdlib/td#building)
- [deepdiff](https://github.com/seperman/deepdiff)

### Installation
> For better performance, it's recommended to install [orjson](https://github.com/ijl/orjson#install) or [ujson](https://github.com/ultrajson/ultrajson#ultrajson).

You can install Pytdbot using pip:
```bash
pip install pytdbot
```
To install the development version from Github, use the following command:
```bash
pip install git+https://github.com/pytdbot/client.git
```

### Examples
Basic example:
```python

from pytdbot import Client, utils
from pytdbot.types import LogStreamFile, Update

client = Client(
    api_id=0,  
    api_hash="API_HASH",  
    database_encryption_key="1234echobot$",
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token or phone number if you want to login as user
    files_directory="BotDB",  # Path where to store TDLib files
    lib_path="/path/to/libtdjson.so", # Path to TDjson shared library
    td_log=LogStreamFile("tdlib.log"),  # Set TDLib log file path
    td_verbosity=2,  # TDLib verbosity level
)


@client.on_updateNewMessage()
async def print_message(c: Client, message: Update):
    print(message)


@client.on_updateNewMessage()
async def simple_message(c: Client, message: Update):
    if message.is_private:
        await message.reply_text('Hi! i am simple bot')

    if message.is_self and message.text: # Works only for userbots.
        if message.text == "!id":
            await message.edit_text(
                "\\- Current chat ID: {}\n\\- {} ID: {}".format(
                    utils.code(str(message.chat_id)),
                    utils.bold(c.me["first_name"]),
                    utils.code(str(message.from_id)),
                ),
                parse_mode="markdownv2",
            )



# Run the client
client.run()

```
For more examples, check the [examples](https://github.com/pytdbot/client/tree/main/examples) folder.

# Thanks to
- You for viewing or using this project.

- [@levlam](https://github.com/levlam) for maintaining [TDLib](https://github.com/tdlib/td) and for the help to create [Pytdbot](https://github.com/pytdbot/client).
# License

MIT [License](https://github.com/pytdbot/client/blob/main/LICENSE)
