# Rich messages

Build HTML with [`pytdbot.utils`](utils.md) helpers (they return strings; join with `+`), then send.

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
```

Send with [`reply_rich_message`][pytdbot.Message.reply_rich_message] or [`sendRichMessage`][pytdbot.Client.sendRichMessage] (`chat_id`, `html=`). Pass `markdown=` instead of `html=` (not both). Edit later with [`edit_rich_message`][pytdbot.Message.edit_rich_message] or [`editRichMessage`][pytdbot.Client.editRichMessage]. Convert a received [`RichMessage`][pytdbot.types.RichMessage] with [`rich_message_to_html`][pytdbot.utils.rich_message_to_html] (returns `(html, media)`).

Usual HTML helpers work inside rich HTML too: [`bold`][pytdbot.utils.bold], [`italic`][pytdbot.utils.italic], [`underline`][pytdbot.utils.underline], [`strikethrough`][pytdbot.utils.strikethrough], [`spoiler`][pytdbot.utils.spoiler], [`code`][pytdbot.utils.code], [`pre`][pytdbot.utils.pre] / [`pre_code`][pytdbot.utils.pre_code], [`hyperlink`][pytdbot.utils.hyperlink], [`mention`][pytdbot.utils.mention], [`custom_emoji`][pytdbot.utils.custom_emoji], [`quote`][pytdbot.utils.quote].

## Buttons

On a rich message, use [`tg_button`][pytdbot.utils.tg_button] / [`tg_button_row`][pytdbot.utils.tg_button_row]. Do **not** attach `reply_markup=` [`ReplyMarkupInlineKeyboard`][pytdbot.types.ReplyMarkupInlineKeyboard] unless you explicitly want a normal inline keyboard.

- **Inline** (in the text): put `tg_button(...)` inside [`paragraph`][pytdbot.utils.paragraph].
- **Row** (full-width bar): [`tg_button_row`][pytdbot.utils.tg_button_row]`(*buttons, align=None)`. `align` is `"left"`, `"center"`, or `"right"`; omit it for full-width buttons.

`tg_button(*label, type, …)`:

| `type` | Extra args |
| --- | --- |
| `url` | `url=` |
| `callback_data` | `data=` (`str` or `bytes`; [`callback_data`][pytdbot.utils.callback_data] if you want a Python object) |
| `web_app` | `url=` |
| `login_url` | `url=`, optional `forward_text=`, `request_write_access=` |
| `switch_inline_query` / `switch_inline_query_current_chat` | `query=` |
| `copy_text` | `text=` |
| `disabled` | none |

`style=` (optional): `"primary"`, `"danger"`, `"success"`, `"link"` (`"link"` only on callback buttons).

Callback presses still go through [`on_updateNewCallbackQuery`](handlers.md) + [`load_callback_data`][pytdbot.utils.load_callback_data] / [`update.answer`][pytdbot.UpdateNewCallbackQuery.answer].
