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
        r"""Get callback query message; ``None`` for inline callback queries"""

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return

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

    async def reply_text(
        self,
        text: str,
        entities: list[pytdbot.types.TextEntity] = None,
        parse_mode: str = None,
        disable_web_page_preview: bool = False,
        url: str = None,
        force_small_media: bool = None,
        force_large_media: bool = None,
        show_above_text: bool = None,
        clear_draft: bool = False,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral text message. Shortcut for :meth:`~pytdbot.Client.sendTextMessage`"""

        return await self._client.sendTextMessage(
            chat_id=getattr(self, "chat_id", 0),
            text=text,
            entities=entities,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview,
            url=url,
            force_small_media=force_small_media,
            force_large_media=force_large_media,
            show_above_text=show_above_text,
            clear_draft=clear_draft,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_rich_message(
        self,
        *,
        markdown: str = None,
        html: str = None,
        media: list[pytdbot.types.InputRichMessageMedia] = None,
        is_rtl: bool = False,
        detect_automatic_blocks: bool = False,
        clear_draft: bool = False,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral rich message. Shortcut for :meth:`~pytdbot.Client.sendRichMessage`"""

        return await self._client.sendRichMessage(
            chat_id=getattr(self, "chat_id", 0),
            markdown=markdown,
            html=html,
            media=media,
            is_rtl=is_rtl,
            detect_automatic_blocks=detect_automatic_blocks,
            clear_draft=clear_draft,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_animation(
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
        has_spoiler: bool = False,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral animation. Shortcut for :meth:`~pytdbot.Client.sendAnimation`"""

        return await self._client.sendAnimation(
            chat_id=getattr(self, "chat_id", 0),
            animation=animation,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            added_sticker_file_ids=added_sticker_file_ids,
            duration=duration,
            width=width,
            height=height,
            has_spoiler=has_spoiler,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_audio(
        self,
        audio: pytdbot.types.InputFile | str,
        album_cover_thumbnail: pytdbot.types.InputThumbnail | None = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        title: str = None,
        performer: str = None,
        duration: int = 0,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral audio. Shortcut for :meth:`~pytdbot.Client.sendAudio`"""

        return await self._client.sendAudio(
            chat_id=getattr(self, "chat_id", 0),
            audio=audio,
            album_cover_thumbnail=album_cover_thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            title=title,
            performer=performer,
            duration=duration,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_document(
        self,
        document: pytdbot.types.InputFile | str,
        thumbnail: pytdbot.types.InputThumbnail | None = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        disable_content_type_detection: bool = True,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral document. Shortcut for :meth:`~pytdbot.Client.sendDocument`"""

        return await self._client.sendDocument(
            chat_id=getattr(self, "chat_id", 0),
            document=document,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            disable_content_type_detection=disable_content_type_detection,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_photo(
        self,
        photo: pytdbot.types.InputFile | str,
        thumbnail: pytdbot.types.InputThumbnail | None = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        width: int = 0,
        height: int = 0,
        has_spoiler: bool = False,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral photo. Shortcut for :meth:`~pytdbot.Client.sendPhoto`"""

        return await self._client.sendPhoto(
            chat_id=getattr(self, "chat_id", 0),
            photo=photo,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            added_sticker_file_ids=added_sticker_file_ids,
            width=width,
            height=height,
            has_spoiler=has_spoiler,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_video(
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
        has_spoiler: bool = False,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral video. Shortcut for :meth:`~pytdbot.Client.sendVideo`"""

        return await self._client.sendVideo(
            chat_id=getattr(self, "chat_id", 0),
            video=video,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            added_sticker_file_ids=added_sticker_file_ids,
            supports_streaming=supports_streaming,
            duration=duration,
            width=width,
            height=height,
            has_spoiler=has_spoiler,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_video_note(
        self,
        video_note: pytdbot.types.InputFile | str,
        thumbnail: pytdbot.types.InputThumbnail | None = None,
        duration: int = 0,
        length: int = 0,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral video note. Shortcut for :meth:`~pytdbot.Client.sendVideoNote`"""

        return await self._client.sendVideoNote(
            chat_id=getattr(self, "chat_id", 0),
            video_note=video_note,
            thumbnail=thumbnail,
            duration=duration,
            length=length,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_voice(
        self,
        voice: pytdbot.types.InputFile | str,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        duration: int = 0,
        waveform: bytes = None,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral voice note. Shortcut for :meth:`~pytdbot.Client.sendVoice`"""

        return await self._client.sendVoice(
            chat_id=getattr(self, "chat_id", 0),
            voice=voice,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            duration=duration,
            waveform=waveform,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
        )

    async def reply_sticker(
        self,
        sticker: pytdbot.types.InputFile | str,
        emoji: str = None,
        thumbnail: pytdbot.types.InputThumbnail | None = None,
        width: int = 0,
        height: int = 0,
        protect_content: bool = False,
        replace_callback_query_message: bool = False,
        reply_markup: pytdbot.types.ReplyMarkupInlineKeyboard
        | pytdbot.types.ReplyMarkupShowKeyboard
        | pytdbot.types.ReplyMarkupForceReply
        | pytdbot.types.ReplyMarkupRemoveKeyboard
        | None = None,
    ) -> pytdbot.types.Error | pytdbot.types.Message:
        r"""Reply to the callback query with an ephemeral sticker. Shortcut for :meth:`~pytdbot.Client.sendSticker`"""

        return await self._client.sendSticker(
            chat_id=getattr(self, "chat_id", 0),
            sticker=sticker,
            emoji=emoji,
            thumbnail=thumbnail,
            width=width,
            height=height,
            protect_content=protect_content,
            callback_query_id=self.id,
            replace_callback_query_message=replace_callback_query_message,
            reply_markup=reply_markup,
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

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return await self._client.editTextMessage(
                inline_message_id=self.inline_message_id,
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

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else self.sender_user_id
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

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return await self._client.editInlineMessageCaption(
                inline_message_id=self.inline_message_id,
                caption=caption,
                show_caption_above_media=show_caption_above_media,
                reply_markup=reply_markup,
            )

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

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return await self._client.editAnimationMessage(
                inline_message_id=self.inline_message_id,
                animation=animation,
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

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else self.sender_user_id
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

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return await self._client.editAudioMessage(
                inline_message_id=self.inline_message_id,
                audio=audio,
                album_cover_thumbnail=album_cover_thumbnail,
                caption=caption,
                caption_entities=caption_entities,
                parse_mode=parse_mode,
                title=title,
                performer=performer,
                duration=duration,
                reply_markup=reply_markup,
            )

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else self.sender_user_id
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

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return await self._client.editDocumentMessage(
                inline_message_id=self.inline_message_id,
                document=document,
                thumbnail=thumbnail,
                caption=caption,
                caption_entities=caption_entities,
                parse_mode=parse_mode,
                disable_content_type_detection=disable_content_type_detection,
                reply_markup=reply_markup,
            )

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else self.sender_user_id
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

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return await self._client.editPhotoMessage(
                inline_message_id=self.inline_message_id,
                photo=photo,
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

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else self.sender_user_id
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

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return await self._client.editVideoMessage(
                inline_message_id=self.inline_message_id,
                video=video,
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

        ephemeral_message_id = 0
        receiver_user_id = 0

        message = await self.getMessage()
        if message:
            ephemeral_message_id = message.ephemeral_message_id
            receiver_user_id = (
                pytdbot.utils.get_message_sender_id(message.receiver_id)
                if message.receiver_id
                else self.sender_user_id
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
        r"""Edit message reply markup. Shortcut for :meth:`~pytdbot.Client.editMessageReplyMarkup` or :meth:`~pytdbot.Client.editInlineMessageReplyMarkup` for inline messages"""

        if isinstance(self, pytdbot.types.UpdateNewInlineCallbackQuery):
            return await self._client.editInlineMessageReplyMarkup(
                inline_message_id=self.inline_message_id, reply_markup=reply_markup
            )

        message = await self.getMessage()
        if message and message.ephemeral_message_id:
            return await self._client.editEphemeralMessage(
                chat_id=self.chat_id,
                receiver_user_id=(
                    pytdbot.utils.get_message_sender_id(message.receiver_id)
                    if message.receiver_id
                    else self.sender_user_id
                ),
                ephemeral_message_id=message.ephemeral_message_id,
                reply_markup=reply_markup,
            )

        return await self._client.editMessageReplyMarkup(
            chat_id=self.chat_id, message_id=self.message_id, reply_markup=reply_markup
        )
