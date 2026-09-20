# Keyboards and callbacks

Inline keyboards are [`ReplyMarkupInlineKeyboard`][pytdbot.types.ReplyMarkupInlineKeyboard]. A callback button’s `data` is **bytes** (TDLib max 64).

```python
from pytdbot import Client, types

await message.reply_text(
    "Pick",
    reply_markup=types.ReplyMarkupInlineKeyboard(
        rows=[[
            types.InlineKeyboardButton(
                text="OK",
                type=types.InlineKeyboardButtonTypeCallback(data=b"ok"),
            ),
        ]]
    ),
)

@client.on_updateNewCallbackQuery()
async def on_cb(c: Client, update: types.UpdateNewCallbackQuery):
    # update.text is the payload decoded as UTF-8 ("ok")
    await update.answer(text="done")
```

[`update.answer`][pytdbot.UpdateNewCallbackQuery.answer] acknowledges the press. [`update.text`][pytdbot.UpdateNewCallbackQuery.text] is the raw bytes as a string.

To pack a Python object instead of raw bytes, use [`utils.callback_data`][pytdbot.utils.callback_data] (JSON, still max 64 bytes). Read it back with [`load_callback_data`][pytdbot.utils.load_callback_data] or [`update.callback_data`][pytdbot.UpdateNewCallbackQuery.callback_data]:

```python
from pytdbot import utils

data = utils.callback_data("ok", {"id": 1})
# types.InlineKeyboardButtonTypeCallback(data=data)

@client.on_updateNewCallbackQuery()
async def on_cb(c: Client, update: types.UpdateNewCallbackQuery):
    cb = update.callback_data
    # cb.action == "ok", cb.data == {"id": 1}
    await update.answer(text="done")
```

See also [`InlineKeyboardButton`][pytdbot.types.InlineKeyboardButton] and [`InlineKeyboardButtonTypeCallback`][pytdbot.types.InlineKeyboardButtonTypeCallback].

!!! tip "Rich messages"
    If you are sending a **rich message**, use [`utils.tg_button`][pytdbot.utils.tg_button] instead of [`ReplyMarkupInlineKeyboard`][pytdbot.types.ReplyMarkupInlineKeyboard].
