# Errors

TDLib answers with objects. A successful result is truthy; an [`Error`][pytdbot.types.Error] is falsy — so you can write `if not chat` after [`getChat`][pytdbot.functions.getChat].

```python
chat = await client.getChat(chat_id=chat_id)
if not chat:
    print(chat.message, chat.code)
    return
```

Raise [`StopHandlers`](https://github.com/pytdbot/client/blob/main/pytdbot/exception/__init__.py) from a handler to skip the rest of the chain. [`AuthorizationError`](https://github.com/pytdbot/client/blob/main/pytdbot/exception/__init__.py) is for login failures.

Flood wait: `Error.limited_seconds` is the retry delay in seconds (`0` unless `code == 429`).

```python
result = await client.sendMessage(...)
if not result:
    wait = result.limited_seconds
```
