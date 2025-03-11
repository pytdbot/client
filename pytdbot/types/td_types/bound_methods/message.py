from typing import List, Union, Literal
from .chatActions import ChatActions
from functools import lru_cache
import pytdbot


class MessageBoundMethods:
    def __init__(self):
        self._client: pytdbot.Client

    @property
    @lru_cache(1)
    def from_id(self) -> Union[int, None]:
        r"""Message Sender ID"""

        if isinstance(self.sender_id, pytdbot.types.MessageSenderChat):
            return self.sender_id.chat_id
        elif isinstance(self.sender_id, pytdbot.types.MessageSenderUser):
            return self.sender_id.user_id

    @property
    @lru_cache(1)
    def reply_to_message_id(self) -> int:
        r"""Replied message ID"""

        if isinstance(self.reply_to, pytdbot.types.MessageReplyToMessage):
            return self.reply_to.message_id

    @property
    @lru_cache(1)
    def text(self) -> str:
        r"""Text of the message"""

        if isinstance(self.content, pytdbot.types.MessageText):
            return self.content.text.text

        return ""

    @property
    @lru_cache(1)
    def entities(self) -> Union[List["pytdbot.types.TextEntity"], None]:
        r"""Entities of the message"""

        if isinstance(self.content, pytdbot.types.MessageText):
            return self.content.text.entities

    @property
    @lru_cache(1)
    def caption(self) -> Union[str, None]:
        r"""Caption of the received media"""

        if isinstance(
            self.content,
            (
                pytdbot.types.MessagePhoto,
                pytdbot.types.MessageVideo,
                pytdbot.types.MessageAnimation,
                pytdbot.types.MessageAudio,
                pytdbot.types.MessageDocument,
                pytdbot.types.MessageVoiceNote,
            ),
        ):
            return self.content.caption.text

    @property
    @lru_cache(1)
    def caption_entities(self) -> Union[List["pytdbot.types.TextEntity"], None]:
        r"""Caption entities of the received media"""

        if isinstance(
            self.content,
            (
                pytdbot.types.MessagePhoto,
                pytdbot.types.MessageVideo,
                pytdbot.types.MessageAnimation,
                pytdbot.types.MessageAudio,
                pytdbot.types.MessageDocument,
                pytdbot.types.MessageVoiceNote,
            ),
        ):
            return self.content.caption.entities

    @property
    @lru_cache(1)
    def remote_file_id(self) -> Union[str, None]:
        r"""Remote file id"""

        file_id = None
        if isinstance(self.content, pytdbot.types.MessagePhoto):
            file_id = self.content.photo.sizes[-1].photo.remote.id
        elif isinstance(self.content, pytdbot.types.MessageVideo):
            file_id = self.content.video.video.remote.id
        elif isinstance(self.content, pytdbot.types.MessageSticker):
            file_id = self.content.sticker.sticker.remote.id
        elif isinstance(self.content, pytdbot.types.MessageAnimation):
            file_id = self.content.animation.animation.remote.id
        elif isinstance(self.content, pytdbot.types.MessageAudio):
            file_id = self.content.audio.audio.remote.id
        elif isinstance(self.content, pytdbot.types.MessageDocument):
            file_id = self.content.document.document.remote.id
        elif isinstance(self.content, pytdbot.types.MessageVoiceNote):
            file_id = self.content.voice_note.voice.remote.id
        elif isinstance(self.content, pytdbot.types.MessageVideoNote):
            file_id = self.content.video_note.video.remote.id

        return file_id

    @property
    @lru_cache(1)
    def remote_unique_file_id(self) -> Union[str, None]:
        r"""Remote unique file id"""

        unique_file_id = None
        if isinstance(self.content, pytdbot.types.MessagePhoto):
            unique_file_id = self.content.photo.sizes[-1].photo.remote.unique_id
        elif isinstance(self.content, pytdbot.types.MessageVideo):
            unique_file_id = self.content.video.video.remote.unique_id
        elif isinstance(self.content, pytdbot.types.MessageSticker):
            unique_file_id = self.content.sticker.sticker.remote.unique_id
        elif isinstance(self.content, pytdbot.types.MessageAnimation):
            unique_file_id = self.content.animation.animation.remote.unique_id
        elif isinstance(self.content, pytdbot.types.MessageAudio):
            unique_file_id = self.content.audio.audio.remote.unique_id
        elif isinstance(self.content, pytdbot.types.MessageDocument):
            unique_file_id = self.content.document.document.remote.unique_id
        elif isinstance(self.content, pytdbot.types.MessageVoiceNote):
            unique_file_id = self.content.voice_note.voice.remote.unique_id
        elif isinstance(self.content, pytdbot.types.MessageVideoNote):
            unique_file_id = self.content.video_note.video.remote.unique_id

        return unique_file_id

    async def mention(self, parse_mode: str = "html") -> Union[str, None]:
        r"""Get the text_mention of the message sender

        Parameters:
            parse_mode (``str``, *optional*):
                The parse mode of the mention. Default is ``html``
        """

        chat = await self._client.getChat(self.from_id)
        if chat:
            return pytdbot.utils.mention(
                chat.title,
                self.from_id,
                html=True if parse_mode.lower() == "html" else False,
            )

    async def getMessageProperties(
        self,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.MessageProperties"]:
        r"""Get the message properties"""

        return await self._client.getMessageProperties(
            chat_id=self.chat_id,
            message_id=self.id,
        )

    async def getRepliedMessage(
        self,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Get the replied message"""

        return await self._client.getRepliedMessage(
            chat_id=self.chat_id,
            message_id=self.id,
        )

    async def getChat(
        self,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Chat"]:
        r"""Get chat info"""

        return await self._client.getChat(self.chat_id)

    async def getChatMember(
        self,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.ChatMember"]:
        r"""Get member info in the current chat"""

        return await self._client.getChatMember(
            chat_id=self.chat_id, member_id=self.sender_id
        )

    async def getUser(
        self,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.User"]:
        r"""Get user info"""

        return await self._client.getUser(self.from_id)

    async def setChatMemberStatus(
        self,
        status: "pytdbot.types.ChatMemberStatus",
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""Set chat member status"""

        return await self._client.setChatMemberStatus(
            chat_id=self.chat_id, member_id=self.sender_id, status=status
        )

    async def leaveChat(self) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""Leave the current chat"""

        return await self._client.leaveChat(self.chat_id)

    async def ban(
        self, banned_until_date: int = None
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""Ban the message sender

        Parameters:

            banned_until_date (``int``):
                Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Always 0 in basic groups
        """

        return await self.setChatMemberStatus(
            status=pytdbot.types.ChatMemberStatusBanned(
                banned_until_date=banned_until_date
            )
        )

    async def delete(
        self,
        revoke: bool = True,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""Delete the received message

        Parameters:
            revoke (``bool``, *optional*):
                Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats
        """

        return await self._client.deleteMessages(
            chat_id=self.chat_id, message_ids=[self.id], revoke=revoke
        )

    async def react(
        self, emoji: str = "👍", is_big: bool = False
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""React to the current message

        Parameters:
            emoji (``str``, *optional*):
                Text representation of the reaction; pass ``None`` to remove the current reaction. Default is ``👍``

            is_big (``bool``, *optional*):
                Pass true if the reactions are added with a big animation. Default is ``False``
        """

        return await self._client.setMessageReactions(
            chat_id=self.chat_id,
            message_id=self.id,
            reaction_types=None
            if not emoji
            else [pytdbot.types.ReactionTypeEmoji(emoji=emoji)],
            is_big=is_big,
        )

    async def pin(
        self,
        disable_notification: bool = False,
        only_for_self: bool = False,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""Pin the message

        Parameters:
            disable_notification (``bool``, *optional*):
                If True, disable notification for the message

            only_for_self (``bool``, *optional*):
                True, if the message needs to be pinned for one side only; private chats only
        """

        return await self._client.pinChatMessage(
            chat_id=self.chat_id,
            message_id=self.id,
            disable_notification=disable_notification,
            only_for_self=only_for_self,
        )

    async def unpin(self) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""Unpin the message"""

        return await self._client.unpinChatMessage(
            chat_id=self.chat_id, message_id=self.id
        )

    async def download(
        self,
        priority: int = 1,
        offset: int = 0,
        limit: int = 0,
        synchronous: bool = True,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.LocalFile"]:
        r"""Download the media file and returns ``LocalFile`` object. Shortcut for :meth:`~pytdbot.Client.downloadFile`."""

        res = None
        if isinstance(self.content, pytdbot.types.MessagePhoto):
            res = await self.content.photo.sizes[-1].photo.download(
                priority=priority, offset=offset, limit=limit, synchronous=synchronous
            )
        elif isinstance(self.content, pytdbot.types.MessageVideo):
            res = await self.content.video.video.download(
                priority=priority, offset=offset, limit=limit, synchronous=synchronous
            )
        elif isinstance(self.content, pytdbot.types.MessageSticker):
            res = await self.content.sticker.sticker.download(
                priority=priority, offset=offset, limit=limit, synchronous=synchronous
            )
        elif isinstance(self.content, pytdbot.types.MessageAnimation):
            res = await self.content.animation.animation.download(
                priority=priority, offset=offset, limit=limit, synchronous=synchronous
            )
        elif isinstance(self.content, pytdbot.types.MessageAudio):
            res = await self.content.audio.audio.download(
                priority=priority, offset=offset, limit=limit, synchronous=synchronous
            )
        elif isinstance(self.content, pytdbot.types.MessageDocument):
            res = await self.content.document.document.download(
                priority=priority, offset=offset, limit=limit, synchronous=synchronous
            )
        elif isinstance(self.content, pytdbot.types.MessageVoiceNote):
            res = await self.content.voice_note.voice.download(
                priority=priority, offset=offset, limit=limit, synchronous=synchronous
            )
        elif isinstance(self.content, pytdbot.types.MessageVideoNote):
            res = await self.content.video_note.video.download(
                priority=priority, offset=offset, limit=limit, synchronous=synchronous
            )

        if isinstance(res, pytdbot.types.Error):
            return res
        elif isinstance(res, pytdbot.types.File):
            return res.local

    def action(
        self,
        action: Literal[
            "typing",
            "upload_photo",
            "record_video",
            "upload_video",
            "record_voice",
            "upload_voice",
            "upload_document",
            "choose_sticker",
            "find_location",
            "record_video_note",
            "upload_video_note",
            "cancel",
        ],
        message_thread_id: int = None,
    ) -> ChatActions:
        r"""Sends a chat action to a specific chat. Supporting context manager (``with`` statement)

        \Example:


            .. code-block:: python

                async with update.action("record_video") as action:
                    ## Any blocking operation
                    await asyncio.sleep(10)
                    action.setAction("upload_video") # change the action to uploading a video

        Or


            .. code-block:: python

                await update.action("typing")
                ## Any blocking operation
                await asyncio.sleep(2)
                await update.reply_text("Hello?")

        \Parameters:
            action (``str``):
                Type of action to broadcast. Choose one, depending on what the user is about to receive: ``typing`` for text messages, ``upload_photo`` for photos, ``record_video`` or ``upload_video`` for videos, ``record_voice`` or ``upload_voice`` for voice notes, ``upload_document`` for general files, ``choose_sticker`` for stickers, ``find_location` for location data, ``record_video_note`` or ``upload_video_note`` for video notes

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the action was performed. Default is ``None``
        """

        return ChatActions(
            client=self._client,
            chat_id=self.chat_id,
            action=action,
            message_thread_id=message_thread_id or self.message_thread_id,
        )

    async def reply_text(
        self,
        text: str,
        entities: List["pytdbot.types.TextEntity"] = None,
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
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with text. Shortcut for :meth:`~pytdbot.Client.sendTextMessage`."""

        return await self._client.sendTextMessage(
            chat_id=self.chat_id,
            text=text,
            entities=entities,
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview,
            url=url,
            force_small_media=force_small_media,
            force_large_media=force_large_media,
            show_above_text=show_above_text,
            clear_draft=clear_draft,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def reply_animation(
        self,
        animation: Union["pytdbot.types.InputFile", str],
        thumbnail: "pytdbot.types.InputThumbnail" = None,
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
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with animation. Shortcut for :meth:`~pytdbot.Client.sendAnimation`."""

        return await self._client.sendAnimation(
            chat_id=self.chat_id,
            animation=animation,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            added_sticker_file_ids=added_sticker_file_ids,
            duration=duration,
            width=width,
            height=height,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            has_spoiler=has_spoiler,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def reply_audio(
        self,
        audio: Union["pytdbot.types.InputFile", str],
        album_cover_thumbnail: "pytdbot.types.InputThumbnail" = None,
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
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with audio. Shortcut for :meth:`~pytdbot.Client.sendAudio`."""

        return await self._client.sendAudio(
            chat_id=self.chat_id,
            audio=audio,
            album_cover_thumbnail=album_cover_thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            title=title,
            performer=performer,
            duration=duration,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def reply_document(
        self,
        document: Union["pytdbot.types.InputFile", str],
        thumbnail: "pytdbot.types.InputThumbnail" = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        disable_content_type_detection: bool = True,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with a document. Shortcut for :meth:`~pytdbot.Client.sendDocument`."""

        return await self._client.sendDocument(
            chat_id=self.chat_id,
            document=document,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            disable_content_type_detection=disable_content_type_detection,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def reply_photo(
        self,
        photo: Union["pytdbot.types.InputFile", str],
        thumbnail: "pytdbot.types.InputThumbnail" = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        width: int = 0,
        height: int = 0,
        self_destruct_type: "pytdbot.types.MessageSelfDestructType" = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        has_spoiler: bool = False,
        message_thread_id: int = 0,
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with a photo. Shortcut for :meth:`~pytdbot.Client.sendPhoto`."""

        return await self._client.sendPhoto(
            chat_id=self.chat_id,
            photo=photo,
            thumbnail=thumbnail,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            added_sticker_file_ids=added_sticker_file_ids,
            width=width,
            height=height,
            self_destruct_type=self_destruct_type,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            has_spoiler=has_spoiler,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def reply_video(
        self,
        video: Union["pytdbot.types.InputFile", str],
        thumbnail: "pytdbot.types.InputThumbnail" = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        supports_streaming: bool = None,
        duration: int = 0,
        width: int = 0,
        height: int = 0,
        self_destruct_type: "pytdbot.types.MessageSelfDestructType" = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        has_spoiler: bool = False,
        message_thread_id: int = 0,
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with a video. Shortcut for :meth:`~pytdbot.Client.sendVideo`."""

        return await self._client.sendVideo(
            chat_id=self.chat_id,
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
            self_destruct_type=self_destruct_type,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            has_spoiler=has_spoiler,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def reply_video_note(
        self,
        video_note: Union["pytdbot.types.InputFile", str],
        thumbnail: "pytdbot.types.InputThumbnail" = None,
        duration: int = 0,
        length: int = 0,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with a video note. Shortcut for :meth:`~pytdbot.Client.sendVideoNote`."""

        return await self._client.sendVideoNote(
            chat_id=self.chat_id,
            video_note=video_note,
            thumbnail=thumbnail,
            duration=duration,
            length=length,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def reply_voice(
        self,
        voice: Union["pytdbot.types.InputFile", str],
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        duration: int = 0,
        waveform: bytes = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with a voice note. Shortcut for :meth:`~pytdbot.Client.sendVoice`."""

        return await self._client.sendVoice(
            chat_id=self.chat_id,
            voice=voice,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            duration=duration,
            waveform=waveform,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def reply_sticker(
        self,
        sticker: Union["pytdbot.types.InputFile", str],
        emoji: str = None,
        thumbnail: "pytdbot.types.InputThumbnail" = None,
        width: int = 0,
        height: int = 0,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_markup: Union[
            "pytdbot.types.ReplyMarkupInlineKeyboard",
            "pytdbot.types.ReplyMarkupShowKeyboard",
            "pytdbot.types.ReplyMarkupForceReply",
            "pytdbot.types.ReplyMarkupRemoveKeyboard",
        ] = None,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Reply to the message with a sticker. Shortcut for :meth:`~pytdbot.Client.sendSticker`."""

        return await self._client.sendSticker(
            chat_id=self.chat_id,
            sticker=sticker,
            emoji=emoji,
            thumbnail=thumbnail,
            width=width,
            height=height,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=self.id,
            reply_markup=reply_markup,
        )

    async def copy(
        self,
        chat_id: int,
        in_game_share: bool = None,
        replace_caption: bool = None,
        new_caption: str = None,
        new_caption_entities: list = None,
        parse_mode: str = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        allow_paid_broadcast: bool = False,
        message_thread_id: int = 0,
        quote: "pytdbot.types.InputTextQuote" = None,
        reply_to_message_id: int = 0,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Copy message to chat. Shortcut for :meth:`~pytdbot.Client.sendCopy`."""

        return await self._client.sendCopy(
            chat_id=chat_id,
            from_chat_id=self.chat_id,
            message_id=self.id,
            in_game_share=in_game_share,
            replace_caption=replace_caption,
            new_caption=new_caption,
            new_caption_entities=new_caption_entities,
            parse_mode=parse_mode,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            message_thread_id=message_thread_id,
            quote=quote,
            reply_to_message_id=reply_to_message_id,
        )

    async def forward(
        self,
        chat_id: int,
        in_game_share: bool = False,
        disable_notification: bool = False,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.Message"]:
        r"""Forward message to chat. Shortcut for :meth:`~pytdbot.Client.forwardMessage`."""

        return await self._client.forwardMessage(
            chat_id=chat_id,
            from_chat_id=self.chat_id,
            message_id=self.id,
            in_game_share=in_game_share,
            disable_notification=disable_notification,
        )

    async def edit_text(
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
        r"""Edit text message. Shortcut for :meth:`~pytdbot.Client.editTextMessage`."""

        return await self._client.editTextMessage(
            chat_id=self.chat_id,
            message_id=self.id,
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
