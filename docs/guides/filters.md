# Filters

A filter is a callable `(client, event) -> bool`. If it returns true, the handler runs. Build one with [`filters.create`](https://github.com/pytdbot/client/blob/main/pytdbot/filters.py).

```python
from pytdbot import Client, types, filters

private = filters.create(lambda _, m: m.chat_id > 0)

@client.on_message(filters=private)
async def only_private(c: Client, message: types.Message):
    await message.reply_text("private chat")
```

Factory:

```python
@filters.create
async def photos(_, event) -> bool:
    return isinstance(event.content, types.MessagePhoto)
```

Use the same object as a decorator on plugin handlers (`@photos` instead of `filters=`), or pass `filters=photos`.

See [`MessagePhoto`][pytdbot.types.MessagePhoto] and [Handlers](handlers.md).
