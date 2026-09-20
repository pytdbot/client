# Plugins

Split handlers into modules under a folder. Pass [`types.Plugins`](https://github.com/pytdbot/client/blob/main/pytdbot/types/plugins/__init__.py) into `Client`.

```python
from pytdbot import Client, types

client = Client(
    token="BOT_TOKEN",
    api_id=0,
    api_hash="API_HASH",
    files_directory="BotDB",
    database_encryption_key="change-me",
    plugins=types.Plugins(
        folder="plugins/",
        # include=["rules", "admin.ban"],
        # exclude=["experimental"],
    ),
)
```

| Arg | Meaning |
| --- | --- |
| `folder` | Directory to scan for `*.py` (recursive) |
| `include` | If set, only these names relative to `folder` (`rules` → `plugins/rules.py`) |
| `exclude` | If set (and no `include`), skip these names |

Plugin module (`plugins/ping.py`) — decorate with `Client.…` (no client instance):

```python
from pytdbot import Client, types, filters

private = filters.create(lambda _, m: m.chat_id > 0)

@Client.on_message(filters=private)
async def ping(c: Client, message: types.Message):
    if message.text == "/ping":
        await message.reply_text("pong")
```

Loaded when `Client` is constructed with `plugins=…`. The folder must be importable (usually run from the project root). Inside a plugin, [`reply_text`][pytdbot.Message.reply_text] is the same bound method as on a live client.

- `client.reload_plugins()` — reload modules (**dev only**)
- `client.remove_handler(func)` — drop one function
