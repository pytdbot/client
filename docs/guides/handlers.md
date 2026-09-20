# Handlers

A handler is an async function you hang on the client. In a [plugin](plugins.md) you decorate `Client` itself; otherwise decorate your live client.

```python
@client.on_message()
async def on_msg(c: Client, message: types.Message):
    ...

@client.on_updateNewMessage()
async def on_raw(c: Client, update: types.UpdateNewMessage):
    ...
```

| Decorator | Payload |
| --- | --- |
| `on_message()` | [`Message`][pytdbot.types.Message] (unpacked from [`updateNewMessage`][pytdbot.types.UpdateNewMessage]) |
| `on_updateNewMessage()` and other `on_update…` | Full update object |
| `on_updateNewCallbackQuery()` | [`UpdateNewCallbackQuery`][pytdbot.types.UpdateNewCallbackQuery] |
| `initializer` / `finalizer` | Run before / after other handlers |

Common kwargs:

- `filters=` — a [`Filter`](filters.md)
- `position=` — order in the list
- `timeout=` — seconds; also `default_handlers_timeout` on the client
- `inner_object=` — pass the inner object of an update (for example `UpdateNewMessage.message`)

Raise [`StopHandlers`](https://github.com/pytdbot/client/blob/main/pytdbot/exception/__init__.py) to skip the rest of the chain.

```python
from pytdbot.exception import StopHandlers

@client.on_message()
async def gate(c: Client, message: types.Message):
    if message.chat_id < 0:
        raise StopHandlers
```

Remove a function later with `client.remove_handler(func)`.
