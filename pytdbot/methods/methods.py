import pytdbot

from typing import List, Union

from ..types import (
    ChatTypeSupergroup,
    Error,
    FormattedText,
    InputFile,
    InputFileRemote,
    InputMessageAnimation,
    InputMessageAudio,
    InputMessageContent,
    InputMessageDocument,
    InputMessageForwarded,
    InputMessagePhoto,
    InputMessageReplyTo,
    InputMessageReplyToMessage,
    InputMessageSticker,
    InputMessageText,
    InputMessageVideo,
    InputMessageVideoNote,
    InputMessageVoiceNote,
    InputTextQuote,
    InputThumbnail,
    LinkPreviewOptions,
    Message,
    MessageCopyOptions,
    MessageSelfDestructType,
    MessageSendOptions,
    ReplyMarkup,
    ReplyMarkupForceReply,
    ReplyMarkupInlineKeyboard,
    ReplyMarkupRemoveKeyboard,
    ReplyMarkupShowKeyboard,
    TextEntity,
    TextParseModeHTML,
    TextParseModeMarkdown,
)

from .td_functions import TDLibFunctions


class Methods(TDLibFunctions):
    r"""TDLib API functions class"""

    async def parseText(
        self,
        text: str,
        parse_mode: str = "html",
    ) -> Union[Error, FormattedText]:
        r"""Parses Bold, Italic, Underline, Strikethrough, Spoiler, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text

        Parameters:
            text (``str``):
                The text to parse

            parse_mode (``str``):
                Text parse mode. Currently supported: markdown, markdownv2 and html. Default is "html"

        Returns:
            :class:`~pytdbot.types.FormattedText`
        """

        if not text or not parse_mode:
            return

        parse_mode = parse_mode.lower()

        if parse_mode == "markdown":
            mode = TextParseModeMarkdown(1)
        elif parse_mode == "markdownv2":
            mode = TextParseModeMarkdown(2)
        elif parse_mode == "html":
            mode = TextParseModeHTML()
        else:
            raise ValueError(
                "Invalid parse_mode. Currently supported: markdown, markdownv2, html"
            )

        return await self.parseTextEntities(text, mode)

    async def getSupergroupId(
        self,
        chat_id: int,
    ) -> Union[Error, int, None]:
        r"""Get supergroup id from chat id

        Parameters:
            chat_id (``int``):
                Chat identifier

        Returns:
            ``int``
        """

        chat_info = await self.getChat(chat_id)
        if not chat_info:
            return chat_info

        if isinstance(chat_info.type, ChatTypeSupergroup):
            return chat_info.type.supergroup_id

        return None

    async def sendTextMessage(
        self,
        chat_id: int,
        text: str,
        entities: List[TextEntity] = None,
        parse_mode: str = None,
        disable_web_page_preview: bool = False,
        url: str = None,
        force_small_media: bool = None,
        force_large_media: bool = None,
        show_above_text: bool = None,
        clear_draft: bool = False,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send text message to chat

        Parameters:
            chat_id (``int``):
                Target chat

            text (``str``):
                Text to send

            entities (``list``, *optional*):
                List of ``TextEntity`` objects to parse in the text. If you want to send a text with formatting, use ```parse_mode``` instead

            parse_mode (``str``, *optional*):
                Mode for parsing entities. Default is ``markdown``

            disable_web_page_preview (``bool``, *optional*):
                Disables link previews for links in this message. Default is ``False``

            url (``str``, *optional*):
                URL to use for link preview. If empty, then the first URL found in the message text will be used. Default is ``None``

            force_small_media (``bool``, *optional*):
                True, if shown media preview must be small; ignored in secret chats or if the URL isn't explicitly specified. Default is ``None``

            force_large_media (``bool``, *optional*):
                True, if shown media preview must be large; ignored in secret chats or if the URL isn't explicitly specified. Default is ``None``

            show_above_text (``bool``, *optional*):
                True, if link preview must be shown above message text; otherwise, the link preview will be shown below the message text; ignored in secret chats. Default is ``None``

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``None``

            clear_draft (``bool``, *optional*):
                True, if a chat message draft must be deleted. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup

        Returns:
            :class:`~pytdbot.types.Message`
        """

        parse_mode = parse_mode or self.default_parse_mode
        if entities and isinstance(entities, list):
            text = FormattedText(text=text, entities=entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(text, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            text = parse
        else:
            text = FormattedText(text)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageText(
                text,
                link_preview_options=LinkPreviewOptions(
                    is_disabled=disable_web_page_preview,
                    url=url,
                    force_small_media=force_small_media,
                    force_large_media=force_large_media,
                    show_above_text=show_above_text,
                ),
                clear_draft=clear_draft,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendAnimation(
        self,
        chat_id: int,
        animation: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        duration: int = 0,
        width: int = 0,
        height: int = 0,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        has_spoiler: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send animation to chat

        Parameters:
            chat_id (``int``):
                Target chat

            animation (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Animation to send

            thumbnail (:class:`~pytdbot.types.InputThumbnail`, *optional*):
                Thumbnail of the animation to send

            caption (``str``, *optional*):
                Animation caption

            caption_entities (``list``, *optional*):
                List of ``MessageEntity`` objects to parse in the caption. If you want to send a caption with formatting, use ``parse_mode`` instead

            parse_mode (``str``, *optional*):
                Mode for parsing entities. Default is ``markdown``

            added_sticker_file_ids (``list``, *optional*):
                File identifiers of the stickers added to the animation, if applicable

            duration (``int``, *optional*):
                Duration of the animation, in seconds

            width (``int``, *optional*):
                Width of the animation

            height (``int``, *optional*):
                Height of the animation

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            has_spoiler (``bool``, *optional*):
                True, if the photo preview must be covered by a spoiler animation; not supported in secret chats

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup

        Returns:
            :class:`~pytdbot.types.Message`

        """

        parse_mode = parse_mode or self.default_parse_mode
        if isinstance(caption_entities, list):
            caption = FormattedText(text=caption, entities=caption_entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(caption, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            caption = parse
        else:
            caption = FormattedText(caption)

        if isinstance(animation, str):
            animation = InputFileRemote(animation)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageAnimation(
                animation=animation,
                thumbnail=thumbnail,
                added_sticker_file_ids=added_sticker_file_ids,
                duration=duration,
                width=width,
                height=height,
                caption=caption,
                has_spoiler=has_spoiler,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendAudio(
        self,
        chat_id: int,
        audio: Union[InputFile, str],
        album_cover_thumbnail: InputThumbnail = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        title: str = None,
        performer: str = None,
        duration: int = 0,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send audio to chat

        Parameters:
            chat_id (``int``):
                Target chat

            audio (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Audio to send

            album_cover_thumbnail (:class:`~pytdbot.types.InputThumbnail`, *optional*):
                Thumbnail of the album cover to be set

            caption (``str``, *optional*):
                Audio caption

            caption_entities (``list``, *optional*):
                List of ``MessageEntity`` objects to parse in the caption. If you want to send a caption with formatting, use ``parse_mode`` instead

            parse_mode (``str``, *optional*):
                Mode for parsing entities. Default is ``markdown``

            title (``str``, *optional*):
                Title of the audio

            performer (``str``, *optional*):
                Performer of the audio

            duration (``int``, *optional*):
                Duration of the audio, in seconds

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Message`

        """

        parse_mode = parse_mode or self.default_parse_mode
        if isinstance(caption_entities, list):
            caption = FormattedText(text=caption, entities=caption_entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(caption, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            caption = parse
        else:
            caption = FormattedText(caption)

        if isinstance(audio, str):
            audio = InputFileRemote(audio)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageAudio(
                audio=audio,
                album_cover_thumbnail=album_cover_thumbnail,
                title=title,
                performer=performer,
                duration=duration,
                caption=caption,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendDocument(
        self,
        chat_id: int,
        document: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        disable_content_type_detection: bool = True,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send document to chat

        Parameters:
            chat_id (``int``):
                Target chat

            document (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Document to send

            thumbnail (:class:`~pytdbot.types.InputThumbnail`, *optional*):
                Thumbnail of the document to be set

            caption (``str``, *optional*):
                Document caption

            caption_entities (``list``, *optional*):
                List of ``MessageEntity`` objects to parse in the caption. If you want to send a caption with formatting, use ``parse_mode`` instead

            parse_mode (``str``, *optional*):
                Mode for parsing entities. Default is ``markdown``

            disable_content_type_detection (``bool``, *optional*):
                If true, automatic file type detection will be disabled and the document will be always sent as file. Always true for files sent to secret chats

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Message`
        """

        parse_mode = parse_mode or self.default_parse_mode
        if isinstance(caption_entities, list):
            caption = FormattedText(text=caption, entities=caption_entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(caption, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            caption = parse
        else:
            caption = FormattedText(caption)

        if isinstance(document, str):
            document = InputFileRemote(document)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageDocument(
                document=document,
                thumbnail=thumbnail,
                disable_content_type_detection=disable_content_type_detection,
                caption=caption,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendPhoto(
        self,
        chat_id: int,
        photo: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        width: int = 0,
        height: int = 0,
        self_destruct_type: MessageSelfDestructType = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        has_spoiler: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send photo to chat

        Parameters:
            chat_id (``int``):
                Target chat

            photo (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Photo to send

            thumbnail (:class:`~pytdbot.types.InputThumbnail`, *optional*):
                Thumbnail of the photo to be set

            caption (``str``, *optional*):
                Photo caption

            caption_entities (``list``, *optional*):
                List of ``MessageEntity`` objects to parse in the caption. If you want to send a caption with formatting, use ``parse_mode`` instead

            parse_mode (``str``, *optional*):
                Mode for parsing entities. Default is ``markdown``

            added_sticker_file_ids (``list``, *optional*):
                List of file identifiers of added stickers

            width (``int``, *optional*):
                Photo width

            height (``int``, *optional*):
                Photo height

            self_destruct_type (:class:`~pytdbot.types.MessageSelfDestructType`, *optional*):
                Photo self-destruct type; pass null if none; private chats only

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            has_spoiler (``bool``, *optional*):
                True, if the photo preview must be covered by a spoiler animation; not supported in secret chats

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Message`
        """

        parse_mode = parse_mode or self.default_parse_mode
        if isinstance(caption_entities, list):
            caption = FormattedText(text=caption, entities=caption_entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(caption, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            caption = parse
        else:
            caption = FormattedText(caption)

        if isinstance(photo, str):
            photo = InputFileRemote(photo)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessagePhoto(
                photo=photo,
                thumbnail=thumbnail,
                added_sticker_file_ids=added_sticker_file_ids,
                self_destruct_type=self_destruct_type,
                width=width,
                height=height,
                caption=caption,
                has_spoiler=has_spoiler,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendVideo(
        self,
        chat_id: int,
        video: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        supports_streaming: bool = None,
        duration: int = 0,
        width: int = 0,
        height: int = 0,
        self_destruct_type: MessageSelfDestructType = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        has_spoiler: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send video to chat

        Parameters:
            chat_id (``int``):
                Target chat

            video (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Video to send

            thumbnail (:class:`~pytdbot.types.InputThumbnail`, *optional*):
                Thumbnail of the video to be set

            caption (``str``, *optional*):
                Video caption

            caption_entities (``list``, *optional*):
                List of ``MessageEntity`` objects to parse in the caption. If you want to send a caption with formatting, use ``parse_mode`` instead

            parse_mode (``str``, *optional*):
                Mode for parsing entities. Default is ``markdown``

            added_sticker_file_ids (``list``, *optional*):
                List of file identifiers of added stickers

            supports_streaming (``bool``, *optional*):
                True, if the video should be tried to be streamed

            duration (``int``, *optional*):
                Duration of sent video in seconds

            width (``int``, *optional*):
                Video width

            height (``int``, *optional*):
                Video height

            self_destruct_type (:class:`~pytdbot.types.MessageSelfDestructType`, *optional*):
                Video self-destruct type; pass null if none; private chats only

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            has_spoiler (``bool``, *optional*):
                True, if the photo preview must be covered by a spoiler animation; not supported in secret chats

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Message`
        """

        parse_mode = parse_mode or self.default_parse_mode
        if isinstance(caption_entities, list):
            caption = FormattedText(text=caption, entities=caption_entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(caption, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            caption = parse
        else:
            caption = FormattedText(caption)

        if isinstance(video, str):
            video = InputFileRemote(video)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageVideo(
                video=video,
                thumbnail=thumbnail,
                added_sticker_file_ids=added_sticker_file_ids,
                duration=duration,
                width=width,
                height=height,
                supports_streaming=supports_streaming,
                caption=caption,
                self_destruct_type=self_destruct_type,
                has_spoiler=has_spoiler,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendVideoNote(
        self,
        chat_id: int,
        video_note: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        duration: int = 0,
        length: int = 0,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send video note to chat

        Parameters:
            chat_id (``int``):
                Target chat

            video_note (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Video note to send

            thumbnail (:class:`~pytdbot.types.InputThumbnail`, *optional*):
                Thumbnail of the video note to be set

            duration (``int``, *optional*):
                Duration of sent video note in seconds

            length (``int``, *optional*):
                Video width and height

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Message`

        """

        if isinstance(video_note, str):
            video_note = InputFileRemote(video_note)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageVideoNote(
                video_note=video_note,
                thumbnail=thumbnail,
                duration=duration,
                length=length,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendVoice(
        self,
        chat_id: int,
        voice: Union[InputFile, str],
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        duration: int = 0,
        waveform: bytes = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send voice to chat

        Parameters:
            chat_id (``int``):
                Target chat

            voice (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Voice to send

            caption (``str``, *optional*):
                Voice caption

            caption_entities (``list``, *optional*):
                List of ``MessageEntity`` objects to parse in the caption. If you want to send a caption without parsing entities, use ``parse_mode`` instead

            parse_mode (``str``, *optional*):
                Parse mode for the caption. Default is None

            duration (``int``, *optional*):
                Duration of sent voice in seconds

            waveform (`bytes`, *optional*):
                Waveform representation of the voice note, in 5-bit format

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Message`
        """

        parse_mode = parse_mode or self.default_parse_mode
        if isinstance(caption_entities, list):
            caption = FormattedText(text=caption, entities=caption_entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(caption, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            caption = parse
        else:
            caption = FormattedText(caption)

        if isinstance(voice, str):
            voice = InputFileRemote(voice)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageVoiceNote(
                voice=voice,
                waveform=waveform,
                duration=duration,
                caption=caption,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendSticker(
        self,
        chat_id: int,
        sticker: Union[InputFile, str],
        emoji: str = None,
        thumbnail: InputThumbnail = None,
        width: int = 0,
        height: int = 0,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ) -> Union[Error, Message]:
        r"""Send sticker to chat

        Parameters:
            chat_id (``int``):
                Target chat

            sticker (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Sticker to send

            emoji (``str``, *optional*):
                Emoji associated with the sticker

            thumbnail (:class:`~pytdbot.types.InputThumbnail`, *optional*):
                Sticker thumbnail

            width (``int``, *optional*):
                Sticker width

            height (``int``, *optional*):
                Sticker height

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Message`
        """

        if isinstance(sticker, str):
            sticker = InputFileRemote(sticker)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageSticker(
                sticker=sticker,
                thumbnail=thumbnail,
                width=width,
                height=height,
                emoji=emoji,
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
        )

    async def sendCopy(
        self,
        chat_id: int,
        from_chat_id: int,
        message_id: int,
        in_game_share: bool = None,
        replace_caption: bool = None,
        new_caption: str = None,
        new_caption_entities: list = None,
        parse_mode: str = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
    ) -> Union[Error, Message]:
        r"""Copy message to chat

        Parameters:
            chat_id (``int``):
                Target chat

            from_chat_id (``int``):
                Identifier for the chat this forwarded message came from

            message_id (``int``):
                Identifier of the message to forward

            in_game_share (``bool``, *optional*):
                True, if a game message is being shared from a launched game; applies only to game messages

            replace_caption (``bool``, *optional*):
                True, if media caption of the message copy needs to be replaced

            new_caption (``str``, *optional*):
                New caption of the message copy

            new_caption_entities (``list``, *optional*):
                List of ``MessageEntity`` objects representing entities in the new caption

            parse_mode (``str``, *optional*):
                Mode for parsing entities in the new caption

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            allow_paid_broadcast (``bool``, *optional*):
                Pass true to allow the message to ignore regular broadcast limits for a small fee; for bots only. Default is ``False``

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            quote (:class:`~pytdbot.types.InputTextQuote`, *optional*):
                Chosen quote from the replied message; may be null if none

            reply_to (:class:`~pytdbot.types.InputMessageReplyTo`, *optional*):
                Information about the message or the story this message is replying to; may be null if none

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply. Ignored if ``reply_to`` is specified


        Returns:
            :class:`~pytdbot.types.Message`
        """

        parse_mode = parse_mode or self.default_parse_mode
        if new_caption_entities and isinstance(new_caption_entities, list):
            caption = FormattedText(text=new_caption, entities=new_caption_entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(new_caption, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            caption = parse
        else:
            caption = FormattedText(new_caption)

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageForwarded(
                from_chat_id=from_chat_id,
                message_id=message_id,
                in_game_share=in_game_share,
                copy_options=MessageCopyOptions(
                    send_copy=True, replace_caption=replace_caption, new_caption=caption
                ),
            ),
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to=reply_to,
            reply_to_message_id=reply_to_message_id,
        )

    async def forwardMessage(
        self,
        chat_id: int,
        from_chat_id: int,
        message_id: int,
        in_game_share: bool = False,
        disable_notification: bool = False,
    ):
        r"""Forward message to chat

        Parameters:
            chat_id (``int``):
                Target chat

            from_chat_id (``int``):
                Identifier for the chat this forwarded message came from

            message_id (``int``):
                Identifier of the message to forward

            in_game_share (``bool``, *optional*):
                True, if a game message is being shared from a launched game; applies only to game messages

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Default is ``False``

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.sendMessageWithContent(
            chat_id=chat_id,
            content=InputMessageForwarded(
                from_chat_id=from_chat_id,
                message_id=message_id,
                in_game_share=in_game_share,
            ),
            disable_notification=disable_notification,
        )

    async def editTextMessage(
        self,
        chat_id: int,
        message_id: int,
        text: str,
        parse_mode: str = None,
        entities: list = None,
        disable_web_page_preview: bool = False,
        url: str = None,
        force_small_media: bool = None,
        force_large_media: bool = None,
        show_above_text: bool = None,
        reply_markup: ReplyMarkup = None,
    ) -> Union[Error, Message]:
        r"""Edit text message

        Parameters:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Message identifier in the chat specified in chat_id

            text (``str``):
                New text of the message

            parse_mode (``str``, *optional*):
                Mode for parsing entities in the message text

            entities (``list``, *optional*):
                List of ``MessageEntity`` objects representing entities that may appear in the message text

            disable_web_page_preview (``bool``, *optional*):
                Disables link previews for links in this message. Default is ``False``

            url (``str``, *optional*):
                URL to use for link preview. If empty, then the first URL found in the message text will be used. Default is ``None``

            force_small_media (``bool``, *optional*):
                True, if shown media preview must be small; ignored in secret chats or if the URL isn't explicitly specified. Default is ``None``

            force_large_media (``bool``, *optional*):
                True, if shown media preview must be large; ignored in secret chats or if the URL isn't explicitly specified. Default is ``None``

            show_above_text (``bool``, *optional*):
                True, if link preview must be shown above message text; otherwise, the link preview will be shown below the message text; ignored in secret chats. Default is ``None``

            reply_markup (:class:`~pytdbot.types.ReplyMarkupInlineKeyboard` | :class:`~pytdbot.types.ReplyMarkupShowKeyboard` | :class:`~pytdbot.types.ReplyMarkupForceReply` | :class:`~pytdbot.types.ReplyMarkupRemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Message`
        """

        if not self.use_message_database:
            load_message = await self.getMessage(chat_id, message_id)
            if isinstance(load_message, Error):
                return load_message

        parse_mode = parse_mode or self.default_parse_mode
        if entities and isinstance(entities, list):
            text = FormattedText(text=text, entities=entities)
        elif parse_mode and isinstance(parse_mode, str):
            parse = await self.parseText(text, parse_mode=parse_mode)
            if isinstance(parse, Error):
                return parse
            text = parse
        else:
            text = FormattedText(text)

        return await self.editMessageText(
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=reply_markup
            if isinstance(reply_markup, ReplyMarkup)
            else None,
            input_message_content=InputMessageText(
                text=text,
                link_preview_options=LinkPreviewOptions(
                    is_disabled=disable_web_page_preview,
                    url=url,
                    force_small_media=force_small_media,
                    force_large_media=force_large_media,
                    show_above_text=show_above_text,
                ),
            ),
        )

    async def sendMessageWithContent(
        self,
        chat_id: int,
        content: InputMessageContent,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: InputTextQuote = None,
        reply_to: InputMessageReplyTo = None,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            ReplyMarkupInlineKeyboard,
            ReplyMarkupShowKeyboard,
            ReplyMarkupForceReply,
            ReplyMarkupRemoveKeyboard,
        ] = None,
    ):
        if isinstance(reply_to_message_id, int) and reply_to_message_id > 0:
            reply_to = InputMessageReplyToMessage(
                message_id=reply_to_message_id, quote=quote
            )

        res = await self.sendMessage(
            chat_id=chat_id,
            message_thread_id=message_thread_id,
            reply_to=reply_to,
            options=MessageSendOptions(
                disable_notification=disable_notification,
                protect_content=protect_content,
                allow_paid_broadcast=allow_paid_broadcast,
            ),
            reply_markup=reply_markup
            if isinstance(reply_markup, ReplyMarkup)
            else None,
            input_message_content=content,
        )
        if isinstance(res, Error):
            return res

        return await self._create_request_future(None, f"{res.chat_id}:{res.id}")
