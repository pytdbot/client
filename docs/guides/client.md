# Client

[`Client`](https://github.com/pytdbot/client/blob/main/pytdbot/client.py) is your connection to Telegram: it starts TDLib, sends requests, and hands you updates.

```python
from pytdbot import Client, types

client = Client(
    token="BOT_TOKEN",          # omit when user_bot=True
    api_id=0,
    api_hash="API_HASH",
    files_directory="BotDB",
    database_encryption_key="change-me",
    default_parse_mode="html",
)
```

| Parameter | Role |
| --- | --- |
| `token` | Bot token. Omit for a [userbot](../getting-started/userbot.md). |
| `api_id` / `api_hash` | From [my.telegram.org](https://my.telegram.org/apps). |
| `files_directory` | TDLib database + files. One live client per directory. |
| `database_encryption_key` | Required. |
| `lib_path` | Path to `libtdjson` if not using `pytdbot[tdjson]`. |
| `plugins` | [`types.Plugins`](plugins.md) folder. |
| `default_parse_mode` | `"html"`, `"markdown"`, or `"markdownv2"`. |
| `user_bot` | `True` for a user account. |
| `workers` | Update worker count (default `5`). `None` handles updates immediately. |
| `td_verbosity` / `td_log` | TDLib logging. |
| `nats_url` / `instance_id` / `no_updates` | [TDLib Server](tdlib-server.md). |

## Run

```python
import asyncio
asyncio.run(client.run())
```

`run()` starts TDLib and blocks until stop.

## Several local clients in one process

```python
from pytdbot import Client, ClientManager

clients = [Client(...), Client(...)]
manager = ClientManager(clients)
await manager.start()
```

[`ClientManager`](https://github.com/pytdbot/client/blob/main/pytdbot/client_manager.py) shares one `tdjson` instance across the list.

## Calling TDLib

Every TDLib function is an async method on the client (camelCase):

```python
chat = await client.getChat(chat_id=chat_id)
if not chat:  # Error is falsy; success types are truthy
    return
```

See [Errors](errors.md). Browse methods in the [function reference](../reference/functions/index.md).
