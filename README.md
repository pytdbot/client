# Pytdbot

[![Version](https://img.shields.io/pypi/v/Pytdbot?style=flat&logo=pypi)](https://pypi.org/project/Pytdbot)
[![TDLib version](https://img.shields.io/badge/TDLib-v1.8.65-blue?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMTAwMHB4IiBoZWlnaHQ9IjEwMDBweCIgdmlld0JveD0iMCAwIDEwMDAgMTAwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTMuMiAoNzI2NDMpIC0gaHR0cHM6Ly9za2V0Y2hhcHAuY29tIC0tPgogICAgPHRpdGxlPkFydGJvYXJkPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGRlZnM+CiAgICAgICAgPGxpbmVhckdyYWRpZW50IHgxPSI1MCUiIHkxPSIwJSIgeDI9IjUwJSIgeTI9Ijk5LjI1ODM0MDQlIiBpZD0ibGluZWFyR3JhZGllbnQtMSI+CiAgICAgICAgICAgIDxzdG9wIHN0b3AtY29sb3I9IiMyQUFCRUUiIG9mZnNldD0iMCUiPjwvc3RvcD4KICAgICAgICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iIzIyOUVEOSIgb2Zmc2V0PSIxMDAlIj48L3N0b3A+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGlkPSJBcnRib2FyZCIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPGNpcmNsZSBpZD0iT3ZhbCIgZmlsbD0idXJsKCNsaW5lYXJHcmFkaWVudC0xKSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIj48L2NpcmNsZT4KICAgICAgICA8cGF0aCBkPSJNMjI2LjMyODQxOSw0OTQuNzIyMDY5IEMzNzIuMDg4NTczLDQzMS4yMTY2ODUgNDY5LjI4NDgzOSwzODkuMzUwMDQ5IDUxNy45MTcyMTYsMzY5LjEyMjE2MSBDNjU2Ljc3MjUzNSwzMTEuMzY3NDMgNjg1LjYyNTQ4MSwzMDEuMzM0ODE1IDcwNC40MzE0MjcsMzAxLjAwMzUzMiBDNzA4LjU2NzYyMSwzMDAuOTMwNjcgNzE3LjgxNTgzOSwzMDEuOTU1NzQzIDcyMy44MDY0NDYsMzA2LjgxNjcwNyBDNzI4Ljg2NDc5NywzMTAuOTIxMjEgNzMwLjI1NjU1MiwzMTYuNDY1ODEgNzMwLjkyMjU1MSwzMjAuMzU3MzI5IEM3MzEuNTg4NTUxLDMyNC4yNDg4NDggNzMyLjQxNzg3OSwzMzMuMTEzODI4IDczMS43NTg2MjYsMzQwLjA0MDY2NiBDNzI0LjIzNDAwNyw0MTkuMTAyNDg2IDY5MS42NzUxMDQsNjEwLjk2NDY3NCA2NzUuMTEwOTgyLDY5OS41MTUyNjcgQzY2OC4xMDIwOCw3MzYuOTg0MzQyIDY1NC4zMDEzMzYsNzQ5LjU0NzUzMiA2NDAuOTQwNjE4LDc1MC43NzcwMDYgQzYxMS45MDQ2ODQsNzUzLjQ0ODkzOCA1ODkuODU2MTE1LDczMS41ODgwMzUgNTYxLjczMzM5Myw3MTMuMTUzMjM3IEM1MTcuNzI2ODg2LDY4NC4zMDY0MTYgNDkyLjg2NjAwOSw2NjYuMzQ5MTgxIDQ1MC4xNTAwNzQsNjM4LjIwMDAxMyBDNDAwLjc4NDQyLDYwNS42Njg3OCA0MzIuNzg2MTE5LDU4Ny43ODkwNDggNDYwLjkxOTQ2Miw1NTguNTY4NTYzIEM0NjguMjgyMDkxLDU1MC45MjE0MjMgNTk2LjIxNTA4LDQzNC41NTY0NzkgNTk4LjY5MTIyNyw0MjQuMDAwMzU1IEM1OTkuMDAwOTEsNDIyLjY4MDEzNSA1OTkuMjg4MzEyLDQxNy43NTg5ODEgNTk2LjM2NDc0LDQxNS4xNjA0MzEgQzU5My40NDExNjgsNDEyLjU2MTg4MSA1ODkuMTI2MjI5LDQxMy40NTA0ODQgNTg2LjAxMjQ0OCw0MTQuMTU3MTk4IEM1ODEuNTk4NzU4LDQxNS4xNTg5NDMgNTExLjI5Nzc5Myw0NjEuNjI1Mjc0IDM3NS4xMDk1NTMsNTUzLjU1NjE4OSBDMzU1LjE1NDg1OCw1NjcuMjU4NjIzIDMzNy4wODA1MTUsNTczLjkzNDkwOCAzMjAuODg2NTI0LDU3My41ODUwNDYgQzMwMy4wMzM5NDgsNTczLjE5OTM1MSAyNjguNjkyNzU0LDU2My40OTA5MjggMjQzLjE2MzYwNiw1NTUuMTkyNDA4IEMyMTEuODUxMDY3LDU0NS4wMTM5MzYgMTg2Ljk2NDQ4NCw1MzkuNjMyNTA0IDE4OS4xMzE1NDcsNTIyLjM0NjMwOSBDMTkwLjI2MDI4Nyw1MTMuMzQyNTg5IDIwMi42NTkyNDQsNTA0LjEzNDUwOSAyMjYuMzI4NDE5LDQ5NC43MjIwNjkgWiIgaWQ9IlBhdGgtMyIgZmlsbD0iI0ZGRkZGRiI+PC9wYXRoPgogICAgPC9nPgo8L3N2Zz4=)](https://github.com/tdlib/td)
[![Downloads](https://static.pepy.tech/personalized-badge/pytdbot?period=month&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/pytdbot)
[![Telegram Chat](https://img.shields.io/badge/Pytdbot%20chat-blue?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMTAwMHB4IiBoZWlnaHQ9IjEwMDBweCIgdmlld0JveD0iMCAwIDEwMDAgMTAwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTMuMiAoNzI2NDMpIC0gaHR0cHM6Ly9za2V0Y2hhcHAuY29tIC0tPgogICAgPHRpdGxlPkFydGJvYXJkPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGRlZnM+CiAgICAgICAgPGxpbmVhckdyYWRpZW50IHgxPSI1MCUiIHkxPSIwJSIgeDI9IjUwJSIgeTI9Ijk5LjI1ODM0MDQlIiBpZD0ibGluZWFyR3JhZGllbnQtMSI+CiAgICAgICAgICAgIDxzdG9wIHN0b3AtY29sb3I9IiMyQUFCRUUiIG9mZnNldD0iMCUiPjwvc3RvcD4KICAgICAgICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iIzIyOUVEOSIgb2Zmc2V0PSIxMDAlIj48L3N0b3A+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnIGlkPSJBcnRib2FyZCIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPGNpcmNsZSBpZD0iT3ZhbCIgZmlsbD0idXJsKCNsaW5lYXJHcmFkaWVudC0xKSIgY3g9IjUwMCIgY3k9IjUwMCIgcj0iNTAwIj48L2NpcmNsZT4KICAgICAgICA8cGF0aCBkPSJNMjI2LjMyODQxOSw0OTQuNzIyMDY5IEMzNzIuMDg4NTczLDQzMS4yMTY2ODUgNDY5LjI4NDgzOSwzODkuMzUwMDQ5IDUxNy45MTcyMTYsMzY5LjEyMjE2MSBDNjU2Ljc3MjUzNSwzMTEuMzY3NDMgNjg1LjYyNTQ4MSwzMDEuMzM0ODE1IDcwNC40MzE0MjcsMzAxLjAwMzUzMiBDNzA4LjU2NzYyMSwzMDAuOTMwNjcgNzE3LjgxNTgzOSwzMDEuOTU1NzQzIDcyMy44MDY0NDYsMzA2LjgxNjcwNyBDNzI4Ljg2NDc5NywzMTAuOTIxMjEgNzMwLjI1NjU1MiwzMTYuNDY1ODEgNzMwLjkyMjU1MSwzMjAuMzU3MzI5IEM3MzEuNTg4NTUxLDMyNC4yNDg4NDggNzMyLjQxNzg3OSwzMzMuMTEzODI4IDczMS43NTg2MjYsMzQwLjA0MDY2NiBDNzI0LjIzNDAwNyw0MTkuMTAyNDg2IDY5MS42NzUxMDQsNjEwLjk2NDY3NCA2NzUuMTEwOTgyLDY5OS41MTUyNjcgQzY2OC4xMDIwOCw3MzYuOTg0MzQyIDY1NC4zMDEzMzYsNzQ5LjU0NzUzMiA2NDAuOTQwNjE4LDc1MC43NzcwMDYgQzYxMS45MDQ2ODQsNzUzLjQ0ODkzOCA1ODkuODU2MTE1LDczMS41ODgwMzUgNTYxLjczMzM5Myw3MTMuMTUzMjM3IEM1MTcuNzI2ODg2LDY4NC4zMDY0MTYgNDkyLjg2NjAwOSw2NjYuMzQ5MTgxIDQ1MC4xNTAwNzQsNjM4LjIwMDAxMyBDNDAwLjc4NDQyLDYwNS42Njg3OCA0MzIuNzg2MTE5LDU4Ny43ODkwNDggNDYwLjkxOTQ2Miw1NTguNTY4NTYzIEM0NjguMjgyMDkxLDU1MC45MjE0MjMgNTk2LjIxNTA4LDQzNC41NTY0NzkgNTk4LjY5MTIyNyw0MjQuMDAwMzU1IEM1OTkuMDAwOTEsNDIyLjY4MDEzNSA1OTkuMjg4MzEyLDQxNy43NTg5ODEgNTk2LjM2NDc0LDQxNS4xNjA0MzEgQzU5My40NDExNjgsNDEyLjU2MTg4MSA1ODkuMTI2MjI5LDQxMy40NTA0ODQgNTg2LjAxMjQ0OCw0MTQuMTU3MTk4IEM1ODEuNTk4NzU4LDQxNS4xNTg5NDMgNTExLjI5Nzc5Myw0NjEuNjI1Mjc0IDM3NS4xMDk1NTMsNTUzLjU1NjE4OSBDMzU1LjE1NDg1OCw1NjcuMjU4NjIzIDMzNy4wODA1MTUsNTczLjkzNDkwOCAzMjAuODg2NTI0LDU3My41ODUwNDYgQzMwMy4wMzM5NDgsNTczLjE5OTM1MSAyNjguNjkyNzU0LDU2My40OTA5MjggMjQzLjE2MzYwNiw1NTUuMTkyNDA4IEMyMTEuODUxMDY3LDU0NS4wMTM5MzYgMTg2Ljk2NDQ4NCw1MzkuNjMyNTA0IDE4OS4xMzE1NDcsNTIyLjM0NjMwOSBDMTkwLjI2MDI4Nyw1MTMuMzQyNTg5IDIwMi42NTkyNDQsNTA0LjEzNDUwOSAyMjYuMzI4NDE5LDQ5NC43MjIwNjkgWiIgaWQ9IlBhdGgtMyIgZmlsbD0iI0ZGRkZGRiI+PC9wYXRoPgogICAgPC9nPgo8L3N2Zz4=&label=Telegram)](https://t.me/pytdbotchat)

<a href="https://cupofton.pages.dev/donate?a=UQCeySURtYxvqF2jNXlsFrXuTEqPjJhGx8uoev6tUbD_HELL&n=AYMEN&t=5&c=You+deserve+a+Cup+of+TON+for+Pytdbot%2521" target="_blank" rel="noopener">
    <img src="https://cupofton.pages.dev/assets/badge-1.svg" alt="Buy me a Cup of TON" style="width: 600px; height: auto;">
</a>

Pytdbot is an asynchronous [**TDLib**](https://github.com/tdlib/td) wrapper for **Telegram** users/bots written in **Python**.

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

- Python 3.10+
- Telegram [API key](https://my.telegram.org/apps)
- [tdjson](https://github.com/AYMENJD/tdjson) or [TDLib](https://github.com/tdlib/td#building)
- [deepdiff](https://github.com/seperman/deepdiff)

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
import logging

from pytdbot import Client, types

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s][%(name)s]  %(message)s",
)
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
asyncio.run(client.run())

```

For more examples, check the [examples](https://github.com/pytdbot/client/tree/main/examples) folder.

# Thanks to

- You for viewing or using this project.

- [@levlam](https://github.com/levlam) for maintaining [TDLib](https://github.com/tdlib/td) and for the help to create [Pytdbot](https://github.com/pytdbot/client).

# License

MIT [License](https://github.com/pytdbot/client/blob/main/LICENSE)
