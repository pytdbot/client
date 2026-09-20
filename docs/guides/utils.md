# Utilities

`from pytdbot import utils`. These format text, pack callback payloads, validate Mini App `initData`, and build [rich messages](rich-messages.md).

## Text

HTML by default; pass `html=False` for MarkdownV2. Helpers escape special characters unless `escape=False`.

| Helper | Role |
| --- | --- |
| [`bold`][pytdbot.utils.bold], [`italic`][pytdbot.utils.italic], [`underline`][pytdbot.utils.underline], [`strikethrough`][pytdbot.utils.strikethrough], [`spoiler`][pytdbot.utils.spoiler] | Emphasis |
| [`code`][pytdbot.utils.code], [`pre`][pytdbot.utils.pre], [`pre_code`][pytdbot.utils.pre_code] | Code |
| [`hyperlink`][pytdbot.utils.hyperlink], [`mention`][pytdbot.utils.mention], [`custom_emoji`][pytdbot.utils.custom_emoji] | Links |
| [`quote`][pytdbot.utils.quote], [`rtl`][pytdbot.utils.rtl], [`ltr`][pytdbot.utils.ltr] | Quote / direction |

```python
from pytdbot import utils

text = f"Hello {utils.bold(name)} — {utils.hyperlink('site', url)}"
await message.reply_text(text, parse_mode="html")
```

[`mention`][pytdbot.utils.mention] takes `(text, user_id)`. For the sender of a message, prefer [`message.mention`][pytdbot.Message.mention].

Escape raw user text with [`escape_html`][pytdbot.utils.escape_html] or [`escape_markdown`][pytdbot.utils.escape_markdown] when you interpolate it yourself.

Turn a received [`FormattedText`][pytdbot.types.FormattedText] back into a string with [`get_formatted_text`][pytdbot.utils.get_formatted_text].

## Callback data

An inline button’s `data` is **bytes** (max 64). Raw bytes are enough:

```python
types.InlineKeyboardButtonTypeCallback(data=b"ok")
```

On press, [`update.text`][pytdbot.UpdateNewCallbackQuery.text] is that payload as UTF-8.

To pack a Python object, use [`callback_data`][pytdbot.utils.callback_data] (`action`, optional JSON-serializable `data`) and read it with [`load_callback_data`][pytdbot.utils.load_callback_data] or [`update.callback_data`][pytdbot.UpdateNewCallbackQuery.callback_data]. See [Keyboards](keyboards.md).

## Mini Apps

```python
secret = utils.create_webapp_secret_key(bot_token)
data = utils.parse_webapp_data(secret, init_data)
```

[`create_webapp_secret_key`][pytdbot.utils.create_webapp_secret_key] takes the bot token. [`parse_webapp_data`][pytdbot.utils.parse_webapp_data] takes that secret, the Web App `initData` string, and optional `max_data_age` (default 60 seconds). It returns a `dict`, or raises [`WebAppDataInvalid`](https://github.com/pytdbot/client/blob/main/pytdbot/exception/__init__.py) / [`WebAppDataOutdated`](https://github.com/pytdbot/client/blob/main/pytdbot/exception/__init__.py) / [`WebAppDataMismatch`](https://github.com/pytdbot/client/blob/main/pytdbot/exception/__init__.py).

## Other

| Helper | Role |
| --- | --- |
| [`get_bot_id_from_token`][pytdbot.utils.get_bot_id_from_token] | Bot id from a token string |
| [`get_message_sender_id`][pytdbot.utils.get_message_sender_id] | Id from [`MessageSenderUser`][pytdbot.types.MessageSenderUser] / [`MessageSenderChat`][pytdbot.types.MessageSenderChat] |
| [`get_retry_after_time`][pytdbot.utils.get_retry_after_time] | Parse a flood-wait message string. On an [`Error`][pytdbot.types.Error], use `result.limited_seconds` instead |

Rich HTML builders (`heading`, `paragraph`, `tg_button`, …) live on [Rich messages](rich-messages.md).
