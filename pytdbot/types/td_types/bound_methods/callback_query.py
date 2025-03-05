from typing import List, Union
from functools import lru_cache

import pytdbot


class CallbackQueryBoundMethods:
    def __init__(self):
        self._client: pytdbot.Client

    @property
    @lru_cache(1)
    def text(self) -> str:
        r"""Callback data decoded as str"""

        if isinstance(self.payload, pytdbot.types.CallbackQueryPayloadData):
            return self.payload.data.decode("utf-8")

        return ""

    async def getMessage(self) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Get callback query message"""

        if self.message_id:
            return await self._client.getMessage(
                chat_id=self.chat_id, message_id=self.message_id
            )

    async def answer(
        self,
        text: str,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""Answer to callback query. Shortcut for :meth:`~pytdbot.Client.answerCallbackQuery`"""

        return await self._client.answerCallbackQuery(
            self.id, text=text, show_alert=show_alert, url=url, cache_time=cache_time
        )

    async def edit_message_text(
        self,
        text: str,
        parse_mode: str = None,
        entities: list = None,
        disable_web_page_preview: bool = False,
        url: str = None,
        force_small_media: bool = None,
        force_large_media: bool = None,
        show_above_text: bool = None,
        reply_markup: "pytdbot.types.ReplyMarkup" = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Edit callback query message text. Shortcut for :meth:`~pytdbot.Client.editTextMessage`"""

        return await self._client.editTextMessage(
            chat_id=self.chat_id,
            message_id=self.message_id,
            text=text,
            parse_mode=parse_mode,
            entities=entities,
            disable_web_page_preview=disable_web_page_preview,
            url=url,
            force_small_media=force_small_media,
            force_large_media=force_large_media,
            show_above_text=show_above_text,
            reply_markup=reply_markup,
        )

    async def edit_message_caption(
        self,
        caption: str,
        caption_entities: List["pytdbot.types.TextEntity"] = None,
        parse_mode: str = None,
        show_caption_above_media: bool = None,
        reply_markup: "pytdbot.types.ReplyMarkup" = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Edit message caption"""

        parse_mode = parse_mode or self._client.default_parse_mode
        if isinstance(caption_entities, list):
            caption = pytdbot.types.FormattedText(
                text=caption, entities=caption_entities
            )
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self._client.parseText(caption, parse_mode=parse_mode)
            if isinstance(parse, pytdbot.types.Error):
                return parse
            caption = parse
        else:
            caption = pytdbot.types.FormattedText(caption)

        return await self._client.editMessageCaption(
            chat_id=self.chat_id,
            message_id=self.message_id,
            caption=caption,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )

    # TODO: edit_message_media?

    async def edit_message_reply_markup(
        self, reply_markup: "pytdbot.types.ReplyMarkup"
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Edit message reply markup. Shortcut for :meth:`~pytdbot.Client.editMessageReplyMarkup`"""

        return await self._client.editMessageReplyMarkup(
            chat_id=self.chat_id, message_id=self.message_id, reply_markup=reply_markup
        )
