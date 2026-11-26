from __future__ import annotations

from functools import cached_property

import pytdbot


class CallbackQueryBoundMethods:
    def __init__(self):
        self._client: pytdbot.Client

    @cached_property
    def callback_data(self) -> pytdbot.utils.CallbackData:
        r"""Callback data that was set by :func:`~pytdbot.utils.callback_data`

        Args:
            action (``Any``):
                Action name

            data (``Any``, *optional*):
                Callback data
        """

        if isinstance(self.payload, pytdbot.types.CallbackQueryPayloadData):
            return pytdbot.utils.load_callback_data(self.payload.data)

        return pytdbot.utils.empty_callback_data

    @cached_property
    def text(self) -> str:
        r"""Callback data decoded as str"""

        if isinstance(self.payload, pytdbot.types.CallbackQueryPayloadData):
            return self.payload.data.decode("utf-8")

        return ""

    async def getMessage(self) -> pytdbot.types.Error | pytdbot.types.Message | None:
        r"""Get callback query message"""

        if self.message_id:
            return await self._client.getMessage(
                chat_id=self.chat_id, message_id=self.message_id
            )

    async def answer(
        self,
        text: str,
        show_alert: bool | None = None,
        url: str | None = None,
        cache_time: int | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Ok:
        r"""Answer to callback query. Shortcut for :meth:`~pytdbot.Client.answerCallbackQuery`"""

        return await self._client.answerCallbackQuery(
            callback_query_id=self.id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )

    async def edit_message_text(
        self,
        text: str,
        parse_mode: str | None = None,
        entities: list | None = None,
        disable_web_page_preview: bool = False,
        url: str | None = None,
        force_small_media: bool | None = None,
        force_large_media: bool | None = None,
        show_above_text: bool | None = None,
        reply_markup: pytdbot.types.ReplyMarkup | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message | pytdbot.types.Ok:
        r"""Edit callback query message text. Shortcut for :meth:`~pytdbot.Client.editTextMessage`"""

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else 0
            )

        return await self._client.editTextMessage(
            chat_id=self.chat_id,
            message_id=self.message_id,
            ephemeral_message_id=ephemeral_message_id,
            receiver_user_id=receiver_user_id,
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
        caption_entities: list[pytdbot.types.TextEntity] | None = None,
        parse_mode: str | None = None,
        show_caption_above_media: bool | None = None,
        reply_markup: pytdbot.types.ReplyMarkup | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Edit message caption. Ephemeral messages aren't supported"""

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
            caption = pytdbot.types.FormattedText(text=caption)

        return await self._client.editMessageCaption(
            chat_id=self.chat_id,
            message_id=self.message_id,
            caption=caption,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
        )

    async def edit_message_animation(
        self,
        animation: pytdbot.types.InputFile | str,
        thumbnail: pytdbot.types.InputThumbnail | None = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        duration: int = 0,
        width: int = 0,
        height: int = 0,
        show_caption_above_media: bool = False,
        has_spoiler: bool = False,
        reply_markup: pytdbot.types.ReplyMarkup | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message | pytdbot.types.Ok:
        r"""Edit callback query message animation. Shortcut for :meth:`~pytdbot.Client.editAnimationMessage`"""

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else 0
            )

        return await self._client.editAnimationMessage(
            chat_id=self.chat_id,
            animation=animation,
            message_id=self.message_id,
            ephemeral_message_id=ephemeral_message_id,
            receiver_user_id=receiver_user_id,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            added_sticker_file_ids=added_sticker_file_ids,
            duration=duration,
            width=width,
            height=height,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            reply_markup=reply_markup,
        )

    async def edit_message_audio(
        self,
        audio: pytdbot.types.InputFile | str,
        album_cover_thumbnail: pytdbot.types.InputThumbnail | None = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        title: str = None,
        performer: str = None,
        duration: int = 0,
        reply_markup: pytdbot.types.ReplyMarkup | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message | pytdbot.types.Ok:
        r"""Edit callback query message audio. Shortcut for :meth:`~pytdbot.Client.editAudioMessage`"""

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else 0
            )

        return await self._client.editAudioMessage(
            chat_id=self.chat_id,
            audio=audio,
            message_id=self.message_id,
            ephemeral_message_id=ephemeral_message_id,
            receiver_user_id=receiver_user_id,
            album_cover_thumbnail=album_cover_thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            title=title,
            performer=performer,
            duration=duration,
            reply_markup=reply_markup,
        )

    async def edit_message_document(
        self,
        document: pytdbot.types.InputFile | str,
        thumbnail: pytdbot.types.InputThumbnail | None = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        disable_content_type_detection: bool = True,
        reply_markup: pytdbot.types.ReplyMarkup | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message | pytdbot.types.Ok:
        r"""Edit callback query message document. Shortcut for :meth:`~pytdbot.Client.editDocumentMessage`"""

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else 0
            )

        return await self._client.editDocumentMessage(
            chat_id=self.chat_id,
            document=document,
            message_id=self.message_id,
            ephemeral_message_id=ephemeral_message_id,
            receiver_user_id=receiver_user_id,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            disable_content_type_detection=disable_content_type_detection,
            reply_markup=reply_markup,
        )

    async def edit_message_photo(
        self,
        photo: pytdbot.types.InputFile | str,
        thumbnail: pytdbot.types.InputThumbnail | None = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        width: int = 0,
        height: int = 0,
        show_caption_above_media: bool = False,
        has_spoiler: bool = False,
        reply_markup: pytdbot.types.ReplyMarkup | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message | pytdbot.types.Ok:
        r"""Edit callback query message photo. Shortcut for :meth:`~pytdbot.Client.editPhotoMessage`"""

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else 0
            )

        return await self._client.editPhotoMessage(
            chat_id=self.chat_id,
            photo=photo,
            message_id=self.message_id,
            ephemeral_message_id=ephemeral_message_id,
            receiver_user_id=receiver_user_id,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            added_sticker_file_ids=added_sticker_file_ids,
            width=width,
            height=height,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            reply_markup=reply_markup,
        )

    async def edit_message_video(
        self,
        video: pytdbot.types.InputFile | str,
        thumbnail: pytdbot.types.InputThumbnail | None = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        supports_streaming: bool = None,
        duration: int = 0,
        width: int = 0,
        height: int = 0,
        show_caption_above_media: bool = False,
        has_spoiler: bool = False,
        reply_markup: pytdbot.types.ReplyMarkup | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message | pytdbot.types.Ok:
        r"""Edit callback query message video. Shortcut for :meth:`~pytdbot.Client.editVideoMessage`"""

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else 0
            )

        return await self._client.editVideoMessage(
            chat_id=self.chat_id,
            video=video,
            message_id=self.message_id,
            ephemeral_message_id=ephemeral_message_id,
            receiver_user_id=receiver_user_id,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            added_sticker_file_ids=added_sticker_file_ids,
            supports_streaming=supports_streaming,
            duration=duration,
            width=width,
            height=height,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
            reply_markup=reply_markup,
        )

    async def edit_message_reply_markup(
        self, reply_markup: "pytdbot.types.ReplyMarkup"
    ) -> pytdbot.types.Error | pytdbot.types.Message | pytdbot.types.Ok:
        r"""Edit message reply markup. Shortcut for :meth:`~pytdbot.Client.editMessageReplyMarkup`"""

        message = await self.getMessage()
        if message and message.ephemeral_message_id and message.receiver_id:
            return await self._client.editEphemeralMessage(
                chat_id=self.chat_id,
                receiver_user_id=pytdbot.utils.get_message_sender_id(
                    message.receiver_id
                ),
                ephemeral_message_id=message.ephemeral_message_id,
                reply_markup=reply_markup,
            )

        return await self._client.editMessageReplyMarkup(
            chat_id=self.chat_id, message_id=self.message_id, reply_markup=reply_markup
        )
