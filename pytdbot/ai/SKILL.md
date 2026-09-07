---
name: pytdbot
description: >
    Write Telegram bots and userbots with Pytdbot (async TDLib wrapper
    with high-level helpers; not the Telegram Bot API).
    Use when the user works with Pytdbot, TDLib, or pytdbot.Client.
---

# Pytdbot

Pytdbot is an async [TDLib](https://github.com/tdlib/td) wrapper for Telegram users/bots in Python, with high-level helpers (bound methods, Client helpers, utils). It is **not** the HTTP Telegram Bot API — do not use Bot API method names, types, or libraries. Use Pytdbot/TDLib names and types only.

## `python -m pytdbot.docs` (use this for the API)

Before calling an unfamiliar method or building a type, run the docs CLI. It searches the installed library and prints parameters, types, and descriptions.

| Command              | When to use                                  | Example                                                                            |
| -------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------- |
| `search <query>`     | Find symbols by keyword                      | `python -m pytdbot.docs search "send photo"`                                       |
| `function <name…>`   | Full TDLib method signature(s)               | `python -m pytdbot.docs function sendMessage getChat`                              |
| `type <name…>`       | Fields of a TDLib type                       | `python -m pytdbot.docs type message`                                              |
| `class <name…>`      | Abstract class → concrete types              | `python -m pytdbot.docs class InputFile`                                           |
| `update <name…>`     | Update payload shape                         | `python -m pytdbot.docs update updateNewMessage`                                   |
| `helper [name…]`     | Pytdbot bound methods, Client helpers, utils | `python -m pytdbot.docs helper reply_text reply_photo`                             |
| `helper -q <query>`  | Search helpers only                          | `python -m pytdbot.docs helper -q escape`                                          |
| `batch <kind:name…>` | Mixed lookups in one call                    | `python -m pytdbot.docs batch function:sendMessage type:message helper:reply_text` |
| `stats`              | Counts / TDLib version                       | `python -m pytdbot.docs stats`                                                     |

Workflow: `search` → pick a name → `function` / `type` / `class` / `helper` for full detail.  
Prefer one invocation: pass several names, or `batch kind:name …` (`function`/`fn`, `type`, `class`, `update`, `helper`).  
Flags: `--json` for machine-readable output (one name is still a single object; several names and `batch` are a JSON array); `search --kind function` (or `type`, `class`, `update`, `helper`) to narrow results.  
Also available as `pytdbot-docs` after install. Same commands either way.

## Preference order

1. Bound methods — `message.reply_text`, `message.reply_photo`, `message.text`, …
2. Client helpers — `sendTextMessage`, `sendPhoto`, `sendAlbum`, `parseText`, …
3. `pytdbot.utils` — formatting (including rich messages), callback data, escapes, …
4. TDLib methods on `Client` — `sendMessage`, `getChat`, … (camelCase)

## Basic bot

```python
import asyncio
from pytdbot import Client, types

client = Client(
    token="BOT_TOKEN",
    api_id=0,
    api_hash="API_HASH",
    files_directory="BotDB",
    database_encryption_key="change-me",
)

@client.on_message()
async def on_msg(c: Client, message: types.Message):
    if message.text:
        await message.reply_text(message.text)

asyncio.run(client.run())
```

Userbot: `user_bot=True` (no token) and handle authorization — see `examples/userbot.py`.

## Handlers

- `async def handler(client, update_or_message)`
- `@client.on_message()` → `types.Message`
- `@client.on_updateNewMessage()` / other `on_update…` → full update
- Filters: `from pytdbot import filters` → `filters.create(...)` then `@client.on_message(filters=my_filter)`

## Common patterns

```python
@client.on_message()
async def echo(c: Client, message: types.Message):
    if isinstance(message.content, types.MessageText):
        await message.reply_text(message.text, entities=message.entities)
    elif isinstance(message.content, types.MessagePhoto):
        await message.reply_photo(message.remote_file_id, caption=message.caption)
```

Parse mode on helpers: `"html"`, `"markdown"`, `"markdownv2"` (or `default_parse_mode=` on `Client`).

```python
await message.reply_text("<b>hi</b>", parse_mode="html")
```

Inline keyboard + callback (with `utils.callback_data`). For **rich messages**, use `utils.tg_button` instead unless the user asks for an inline keyboard — see [Rich messages](#rich-messages).

```python
from pytdbot import utils

await message.reply_text(
    "Pick",
    reply_markup=types.ReplyMarkupInlineKeyboard(
        rows=[[
            types.InlineKeyboardButton(
                text="OK",
                type=types.InlineKeyboardButtonTypeCallback(
                    data=utils.callback_data("ok", {"id": 1})
                ),
            ),
        ]]
    ),
)

@client.on_updateNewCallbackQuery()
async def on_cb(c: Client, update: types.UpdateNewCallbackQuery):
    cb = utils.load_callback_data(update.payload.data)
    # cb.action, cb.data
    await update.answer(text="done")
```

```python
async with message.action("typing"):
    await asyncio.sleep(1)
    await message.reply_text("Done")
```

```python
await client.sendPhoto(chat_id, photo="path_or_remote_id", caption="Hi", parse_mode="html")
```

Raw TDLib: look up with `function` / `type` first, then call; build objects with `types.*`.

```python
chat = await client.getChat(chat_id=chat_id)
if not chat:  # Error is falsy; success types are truthy
    return
# use chat...
```

## `pytdbot.utils`

Import: `from pytdbot import utils` (or `from pytdbot.utils import bold, escape_html, …`).  
Signatures: `python -m pytdbot.docs helper bold` / `helper -q webapp`.

- **Text format** (HTML by default; MarkdownV2 with `html=False`): `bold`, `italic`, `underline`, `strikethrough`, `spoiler`, `code`, `pre`, `pre_code`, `hyperlink`, `mention`, `custom_emoji`, `quote`, `rtl`, `ltr`
- **Escape**: `escape_html`, `escape_markdown`
- **Callback buttons**: `callback_data(action, data=None)` → `bytes` (max 64); `load_callback_data(data)` → `.action` / `.data`
- **Mini Apps (Web App)**: `create_webapp_secret_key(bot_token)` → secret; `parse_webapp_data(secret_key, init_data, max_data_age=60)` → validated `dict` (raises `WebAppDataInvalid` / `WebAppDataOutdated` / `WebAppDataMismatch` from `pytdbot.exception`)
- **Flood / retry**: `get_retry_after_time(error_message)`
- **Other**: `get_bot_id_from_token`, `get_message_sender_id`
- **Rich messages**: builders and send helpers — see [Rich messages](#rich-messages)

```python
from pytdbot import utils

text = f"Hello {utils.bold(name)} — {utils.hyperlink('site', url)}"
await message.reply_text(text, parse_mode="html")

# Mini App initData validation
secret = utils.create_webapp_secret_key(bot_token)
data = utils.parse_webapp_data(secret, init_data)
```

## Rich messages

TDLib rich messages (not Bot API). Build HTML with `pytdbot.utils` helpers (they return strings; join with `+`), then send. Signatures: `python -m pytdbot.docs helper reply_rich_message` / `helper tg_button` / `helper -q tg_`.

```python
from pytdbot import utils

html = (
    utils.heading(1, "Title")
    + utils.paragraph("Hello ", utils.bold(name))
    + utils.unordered_list("one", "two")
    + utils.tg_button_row(
        utils.tg_button("OK", type="callback_data", data="ok", style="success"),
        utils.tg_button("Site", type="url", url="https://example.com"),
    )
)
await message.reply_rich_message(html=html)
# or: await client.sendRichMessage(chat_id, html=html)
# markdown= instead of html= is also accepted (not both)
```

Edit later with `client.editRichMessage`. Convert a received rich payload with `utils.rich_message_to_html`.

### Formatting

Usual HTML helpers work inside rich HTML too: `bold`, `italic`, `underline`, `strikethrough`, `spoiler`, `code`, `pre` / `pre_code`, `hyperlink`, `mention`, `custom_emoji`, `quote`.

| Helper                                                                                                                      | Role                                                         |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `paragraph(*children)`                                                                                                      | Paragraph. Put inline `tg_button`s here                      |
| `heading(level, text, name=None)`                                                                                           | `h1`–`h6`; optional in-doc anchor `name`                     |
| `footer(*children)`, `newline(count=1)`, `horizontal_rule()`                                                                | Footer, `<br>`, `<hr>`                                       |
| `marked`, `subscript`, `superscript`                                                                                        | Highlight / sub / sup                                        |
| `thinking(text)`                                                                                                            | Telegram thinking block                                      |
| `tg_math` / `tg_math_block`                                                                                                 | Inline / block LaTeX                                         |
| `tg_time(unix, format, text="")`                                                                                            | Date-time entity                                             |
| `tg_reference(name, text)`, `anchor(name)`, `in_doc_link(anchor, text)`                                                     | In-document references                                       |
| `email_link(address, text)`, `phone(number, text)`                                                                          | `mailto:` / `tel:`                                           |
| `blockquote(*children, cite=None, expandable=False)`, `aside(*children, cite=None)`                                         | Quotes                                                       |
| `details(*children, summary, open=False)`                                                                                   | Collapsible block                                            |
| `unordered_list(*items)`, `ordered_list(*items, start=, type=, reversed=)`, `list_item(*children, value=, checked=, type=)` | Lists; `checked=` makes a checkbox item                      |
| `table(*rows, bordered=, striped=, compact=, caption=)`, `table_row`, `table_header`, `table_cell`, `table_header_cell`     | Tables (`align` / `valign` / `colspan` / `rowspan` on cells) |
| `image(src, alt=, spoiler=)`, `video(src, spoiler=)`, `audio(src)`, `tg_document(src)`                                      | Media (`src` URL or `tg://…` media id)                       |
| `figure(*children)`, `figcaption(*children)`                                                                                | Figure + caption                                             |
| `tg_map(lat, long, zoom)`, `tg_collage(*media, caption=)`, `tg_slideshow(*media, caption=)`                                 | Map / collage / slideshow                                    |

### Buttons

If you are sending a **rich message**, prefer `utils.tg_button` / `utils.tg_button_row` (rich-message buttons). Do **not** attach `reply_markup=types.ReplyMarkupInlineKeyboard(...)` unless the user explicitly asks for an inline keyboard.

- **Inline** (in the text flow): put `tg_button(...)` inside `paragraph(...)`.
- **Row** (full-width bar): pass buttons to `tg_button_row(*buttons, align=None)`. `align` is `"left"`, `"center"`, or `"right"`; omit it for full-width buttons.

```python
html = utils.paragraph(
    "Pick: ",
    utils.tg_button("Go", type="callback_data", data=utils.callback_data("ok", {"id": 1}), style="success"),
) + utils.tg_button_row(
    utils.tg_button("Open", type="url", url="https://t.me"),
    utils.tg_button("Copy", type="copy_text", text="hello"),
)
await message.reply_rich_message(html=html)
```

`tg_button(*label, type, …)`:

| `type`                                                     | Extra args                                                                                      |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `url`                                                      | `url=`; user buttons: `url="tg://user?id=…"`                                                    |
| `callback_data`                                            | `data=` (`str` or `bytes` from `utils.callback_data`)                                           |
| `web_app`                                                  | `url=`                                                                                          |
| `login_url`                                                | `url=`, optional `forward_text=`, `request_write_access=`                                       |
| `switch_inline_query` / `switch_inline_query_current_chat` | `query=`                                                                                        |
| `switch_inline_query_chosen_chat`                          | `query=`, `allow_user_chats=`, `allow_bot_chats=`, `allow_group_chats=`, `allow_channel_chats=` |
| `copy_text`                                                | `text=` (clipboard)                                                                             |
| `disabled`                                                 | no extra args                                                                                   |

`style=` (optional): `"primary"`, `"danger"`, `"success"`, `"link"` (`"link"` only on callback buttons).

Callback presses are still `on_updateNewCallbackQuery` + `utils.load_callback_data` / `update.answer(...)`, same as a normal inline keyboard.

## Plugins

Split handlers into modules under a folder; pass `types.Plugins` into `Client`.

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
        # optional: only these modules (dotted path = folder + file)
        # include=["plugins.rules", "plugins.admin.ban"],
        # optional: skip modules
        # exclude=["plugins.experimental"],
    ),
)
```

**`Plugins`**

| Arg       | Meaning                                                                                    |
| --------- | ------------------------------------------------------------------------------------------ |
| `folder`  | Directory to scan for `*.py` (recursive)                                                   |
| `include` | If set, only load modules whose path matches (e.g. `plugins.rules` for `plugins/rules.py`) |
| `exclude` | If set (and no `include`), skip these module paths                                         |

**Plugin module** (`plugins/ping.py`) — decorate with `Client.…` (no client instance); those handlers are picked up when the client starts with `plugins=…`:

```python
from pytdbot import Client, types, filters

private = filters.create(lambda _, m: m.chat_id > 0)

@Client.on_message(filters=private)
async def ping(c: Client, message: types.Message):
    if message.text == "/ping":
        await message.reply_text("pong")

@Client.on_updateNewCallbackQuery()
async def on_cb(c: Client, update: types.UpdateNewCallbackQuery):
    await update.answer(text="ok")
```

Same decorator API as on a live client: `on_message`, `on_updateNewMessage`, `on_updateNewCallbackQuery`, `initializer`, `finalizer`, other `on_update…`, plus `filters=`, `position=`, `timeout=`. Handlers must be `async`.

**Runtime**

- Loaded when `Client` is constructed with `plugins=…` (folder must be importable; usually run from project root so `plugins.*` imports work).
- `client.reload_plugins()` — reloads plugin modules (**dev only**, not for production). Handlers registered on the client instance itself are left alone.
- `client.remove_handler(func)` — remove a specific handler function.

## Details

- Types: `from pytdbot import Client, types` → `types.SomeType(...)`.
- Bots: `token=`; userbots: `user_bot=True` + authorization updates.
- `files_directory` + `database_encryption_key` required; one live client per directory.
