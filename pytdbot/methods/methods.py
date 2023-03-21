import pytdbot

from typing import Union
from base64 import b64encode
from .tdlibfunctions import TDLibFunctions
from ..types import (
    Result,
    ReplyMarkup,
    InlineKeyboardMarkup,
    ShowKeyboardMarkup,
    ForceReply,
    RemoveKeyboard,
    InputFile,
    InputThumbnail,
)


class Methods(TDLibFunctions):
    """TDLib API functions class"""

    async def sendTextMessage(
        self,
        chat_id: int,
        text: str,
        entities: list = None,
        parse_mode: str = None,
        disable_web_page_preview: bool = False,
        clear_draft: bool = False,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send text message to chat

        Args:
            chat_id (``int``):
                Target chat

            text (``str``):
                Text to send

            entities (``list``, *optional*):
                List of ``MessageEntity`` objects to parse in the text. If you want to send a text with formatting, use ```parse_mode``` instead

            parse_mode (``str``, *optional*):
                Mode for parsing entities. Defaults to ``markdown``

            disable_web_page_preview (``bool``, *optional*):
                Disables link previews for links in this message. Defaults to ``False``

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Defaults to ``False``

            clear_draft (``bool``, *optional*):
                True, if a chat message draft must be deleted. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup

        Returns:
            :class:`~pytdbot.types.Result`
        """

        if entities is None:
            if parse_mode is not None:
                parse = await self.parseText(text, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _text = parse.result
            else:
                _text = {"@type": "formattedText", "text": text, "entities": []}
        else:
            _text = {"@type": "formattedText", "text": text, "entities": entities}

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessageText",
                "text": _text,
                "disable_web_page_preview": disable_web_page_preview,
                "clear_draft": clear_draft,
            },
        }
        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()
        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

    async def sendAnimation(
        self,
        chat_id: int,
        animation: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        has_spoiler: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send animation to chat

        Args:
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
                Mode for parsing entities. Defaults to ``markdown``

            added_sticker_file_ids (``list``, *optional*):
                File identifiers of the stickers added to the animation, if applicable

            duration (``int``, *optional*):
                Duration of the animation, in seconds

            width (``int``, *optional*):
                Width of the animation

            height (``int``, *optional*):
                Height of the animation

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            has_spoiler (``bool``, *optional*):
                True, if the photo preview must be covered by a spoiler animation; not supported in secret chats

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup

        Returns:
            :class:`~pytdbot.types.Result`

        """

        _caption = None
        if isinstance(caption, str):

            if isinstance(caption_entities, list):
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": caption_entities,
                }
            elif isinstance(parse_mode, str):
                parse = await self.parseText(caption, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _caption = parse.result
            else:
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": [],
                }

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessageAnimation",
                "added_sticker_file_ids": added_sticker_file_ids,
                "duration": duration,
                "width": width,
                "height": height,
                "caption": _caption,
                "has_spoiler": has_spoiler,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        if isinstance(animation, InputFile):
            data["input_message_content"]["animation"] = animation.to_dict()
        elif isinstance(animation, str):
            data["input_message_content"]["animation"] = {
                "@type": "inputFileRemote",
                "id": animation,
            }
        else:
            raise ValueError("animation must be InputFile or str")

        if isinstance(thumbnail, InputThumbnail):
            data["input_message_content"]["thumbnail"] = thumbnail.to_dict()

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

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
        duration: int = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send audio to chat

        Args:
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
                Mode for parsing entities. Defaults to ``markdown``

            title (``str``, *optional*):
                Title of the audio

            performer (``str``, *optional*):
                Performer of the audio

            duration (``int``, *optional*):
                Duration of the audio, in seconds

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Result`

        """

        _caption = None
        if isinstance(caption, str):

            if isinstance(caption_entities, list):
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": caption_entities,
                }
            elif isinstance(parse_mode, str):
                parse = await self.parseText(caption, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _caption = parse.result
            else:
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": [],
                }

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessageAudio",
                "title": title,
                "performer": performer,
                "duration": duration,
                "caption": _caption,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        if isinstance(audio, InputFile):
            data["input_message_content"]["audio"] = audio.to_dict()
        elif isinstance(audio, str):
            data["input_message_content"]["audio"] = {
                "@type": "inputFileRemote",
                "id": audio,
            }
        else:
            raise ValueError("audio must be InputFile or str")

        if isinstance(album_cover_thumbnail, InputThumbnail):
            data["input_message_content"][
                "album_cover_thumbnail"
            ] = album_cover_thumbnail.to_dict()

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

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
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send document to chat

        Args:
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
                Mode for parsing entities. Defaults to ``markdown``

            disable_content_type_detection (``bool``, *optional*):
                If true, automatic file type detection will be disabled and the document will be always sent as file. Always true for files sent to secret chats

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Result`
        """

        _caption = None
        if isinstance(caption, str):

            if isinstance(caption_entities, list):
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": caption_entities,
                }
            elif isinstance(parse_mode, str):
                parse = await self.parseText(caption, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _caption = parse.result
            else:
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": [],
                }

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessageDocument",
                "disable_content_type_detection": disable_content_type_detection,
                "caption": _caption,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        if isinstance(document, InputFile):
            data["input_message_content"]["document"] = document.to_dict()
        elif isinstance(document, str):
            data["input_message_content"]["document"] = {
                "@type": "inputFileRemote",
                "id": document,
            }
        else:
            raise ValueError("document must be InputFile or str")

        if isinstance(thumbnail, InputThumbnail):
            data["input_message_content"]["thumbnail"] = thumbnail.to_dict()

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

    async def sendPhoto(
        self,
        chat_id: int,
        photo: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        added_sticker_file_ids: list = None,
        width: int = None,
        height: int = None,
        self_destruct_time: int = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        has_spoiler: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send photo to chat

        Args:
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
                Mode for parsing entities. Defaults to ``markdown``

            added_sticker_file_ids (``list``, *optional*):
                List of file identifiers of added stickers

            width (``int``, *optional*):
                Photo width

            height (``int``, *optional*):
                Photo height

            self_destruct_time (``int``, *optional*):
                Photo self-destruct time (Time To Live), in seconds (0-60). A non-zero self-destruct time can be specified only in private chats

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            has_spoiler (``bool``, *optional*):
                True, if the photo preview must be covered by a spoiler animation; not supported in secret chats

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Result`
        """

        _caption = None
        if isinstance(caption, str):

            if isinstance(caption_entities, list):
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": caption_entities,
                }
            elif isinstance(parse_mode, str):
                parse = await self.parseText(caption, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _caption = parse.result
            else:
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": [],
                }

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessagePhoto",
                "added_sticker_file_ids": added_sticker_file_ids,
                "width": width,
                "height": height,
                "caption": _caption,
                "self_destruct_time": self_destruct_time,
                "has_spoiler": has_spoiler,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        if isinstance(photo, InputFile):
            data["input_message_content"]["photo"] = photo.to_dict()
        elif isinstance(photo, str):
            data["input_message_content"]["photo"] = {
                "@type": "inputFileRemote",
                "id": photo,
            }
        else:
            raise ValueError("photo must be InputFile or str")

        if isinstance(thumbnail, InputThumbnail):
            data["input_message_content"]["thumbnail"] = thumbnail.to_dict()

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

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
        duration: int = None,
        width: int = None,
        height: int = None,
        self_destruct_time: int = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        has_spoiler: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send video to chat

        Args:
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
                Mode for parsing entities. Defaults to ``markdown``

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

            self_destruct_time (``int``, *optional*):
                Video self-destruct time (Time To Live), in seconds (0-60). A non-zero self-destruct time can be specified only in private chats

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            has_spoiler (``bool``, *optional*):
                True, if the photo preview must be covered by a spoiler animation; not supported in secret chats

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Result`
        """

        _caption = None
        if isinstance(caption, str):

            if isinstance(caption_entities, list):
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": caption_entities,
                }
            elif isinstance(parse_mode, str):
                parse = await self.parseText(caption, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _caption = parse.result
            else:
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": [],
                }

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessageVideo",
                "added_sticker_file_ids": added_sticker_file_ids,
                "supports_streaming": supports_streaming,
                "duration": duration,
                "width": width,
                "height": height,
                "caption": _caption,
                "self_destruct_time": self_destruct_time,
                "has_spoiler": has_spoiler,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        if isinstance(video, InputFile):
            data["input_message_content"]["video"] = video.to_dict()
        elif isinstance(video, str):
            data["input_message_content"]["video"] = {
                "@type": "inputFileRemote",
                "id": video,
            }
        else:
            raise ValueError("video must be InputFile or str")

        if isinstance(thumbnail, InputThumbnail):
            data["input_message_content"]["thumbnail"] = thumbnail.to_dict()

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

    async def sendVideoNote(
        self,
        chat_id: int,
        video_note: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        duration: int = None,
        length: int = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send video note to chat

        Args:
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
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Result`

        """

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessageVideoNote",
                "duration": duration,
                "length": length,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        if isinstance(video_note, InputFile):
            data["input_message_content"]["video_note"] = video_note.to_dict()
        elif isinstance(video_note, str):
            data["input_message_content"]["video_note"] = {
                "@type": "inputFileRemote",
                "id": video_note,
            }
        else:
            raise ValueError("video_note must be InputFile or str")

        if isinstance(thumbnail, InputThumbnail):
            data["input_message_content"]["thumbnail"] = thumbnail.to_dict()

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

    async def sendVoice(
        self,
        chat_id: int,
        voice: Union[InputFile, str],
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = None,
        duration: int = None,
        waveform: bytes = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send voice to chat

        Args:
            chat_id (``int``):
                Target chat

            voice (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``):
                Voice to send

            caption (``str``, *optional*):
                Voice caption

            caption_entities (``list``, *optional*):
                List of ``MessageEntity`` objects to parse in the caption. If you want to send a caption without parsing entities, use ``parse_mode`` instead

            parse_mode (``str``, *optional*):
                Parse mode for the caption. Defaults to None

            duration (``int``, *optional*):
                Duration of sent voice in seconds

            waveform (`bytes`, *optional*):
                Waveform representation of the voice note, in 5-bit format

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Result`
        """

        _caption = None
        if isinstance(caption, str):

            if isinstance(caption_entities, list):
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": caption_entities,
                }
            elif isinstance(parse_mode, str):
                parse = await self.parseText(caption, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _caption = parse.result
            else:
                _caption = {
                    "@type": "formattedText",
                    "text": caption,
                    "entities": [],
                }

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessageVoiceNote",
                "duration": duration,
                "caption": _caption,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        if isinstance(waveform, bytes):
            data["input_message_content"]["waveform"] = str(b64encode(waveform))

        if isinstance(voice, InputFile):
            data["input_message_content"]["voice_note"] = voice.to_dict()
        elif isinstance(voice, str):
            data["input_message_content"]["voice_note"] = {
                "@type": "inputFileRemote",
                "id": voice,
            }
        else:
            raise ValueError("voice must be InputFile or str")

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

    async def sendSticker(
        self,
        chat_id: int,
        sticker: Union[InputFile, str],
        emoji: str = None,
        thumbnail: InputThumbnail = None,
        width: int = None,
        height: int = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
    ) -> Result:
        """Send sticker to chat

        Args:
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
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Result`
        """

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "input_message_content": {
                "@type": "inputMessageSticker",
                "emoji": emoji,
                "width": width,
                "height": height,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        if isinstance(sticker, InputFile):
            data["input_message_content"]["sticker"] = sticker.to_dict()
        elif isinstance(sticker, str):
            data["input_message_content"]["sticker"] = {
                "@type": "inputFileRemote",
                "id": sticker,
            }
        else:
            raise ValueError("document must be InputFile or str")

        if isinstance(thumbnail, InputThumbnail):
            data["input_message_content"]["thumbnail"] = thumbnail.to_dict()

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

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
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        load_replied_message: bool = None,
    ) -> Result:
        """Copy message to chat

        Args:
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
                If True, disable notification for the message. Defaults to ``False``

            protect_content (``bool``, *optional*):
                If True, the content of the message must be protected from forwarding and saving

            message_thread_id (``int``, *optional*):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``, *optional*):
                Identifier of the message to reply

            load_replied_message (``bool``, *optional*):
                If True, the replied message(``reply_to_message_id``) will be reloaded. Defaults to ``None``


        Returns:
            :class:`~pytdbot.types.Result`
        """
        _caption = None
        if isinstance(new_caption, str):

            if isinstance(new_caption_entities, list):
                _caption = {
                    "@type": "formattedText",
                    "text": new_caption,
                    "entities": new_caption_entities,
                }
            elif isinstance(parse_mode, str):
                parse = await self.parseText(new_caption, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _caption = parse.result
            else:
                _caption = {
                    "@type": "formattedText",
                    "text": new_caption,
                    "entities": [],
                }

        if load_replied_message == None and not self.use_message_database:
            load_replied_message = True

        if (
            load_replied_message == True
            and isinstance(reply_to_message_id, int)
            and reply_to_message_id > 0
        ):
            # Because TDLib will ignore `reply_to_message_id`
            # if the message isn't loaded in memory
            await self.getMessage(chat_id, reply_to_message_id)

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
                "protect_content": protect_content,
            },
            "reply_to_message_id": reply_to_message_id,
            "message_thread_id": message_thread_id,
            "input_message_content": {
                "@type": "inputMessageForwarded",
                "from_chat_id": from_chat_id,
                "message_id": message_id,
                "in_game_share": in_game_share,
                "copy_options": {
                    "@type": "messageCopyOptions",
                    "send_copy": True,
                    "replace_caption": replace_caption,
                    "new_caption": _caption,
                },
            },
        }

        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

    async def forwardMessage(
        self,
        chat_id: int,
        from_chat_id: int,
        message_id: int,
        in_game_share: bool = False,
        disable_notification: bool = False,
    ):
        """Forward message to chat

        Args:
            chat_id (``int``):
                Target chat

            from_chat_id (``int``):
                Identifier for the chat this forwarded message came from

            message_id (``int``):
                Identifier of the message to forward

            in_game_share (``bool``, *optional*):
                True, if a game message is being shared from a launched game; applies only to game messages

            disable_notification (``bool``, *optional*):
                If True, disable notification for the message. Defaults to ``False``

        Returns:
            :class:`~pytdbot.types.Result`
        """
        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "options": {
                "@type": "messageSendOptions",
                "disable_notification": disable_notification,
            },
            "input_message_content": {
                "@type": "inputMessageForwarded",
                "from_chat_id": from_chat_id,
                "message_id": message_id,
                "in_game_share": in_game_share,
            },
        }
        res = await self.invoke(data)
        if res.is_error:
            return res
        _new = Result(data)
        self._results[str(res.result["id"]) + str(res.result["chat_id"])] = _new
        await _new.wait()
        return _new

    async def editTextMessage(
        self,
        chat_id: int,
        message_id: int,
        text: str,
        parse_mode: str = None,
        entities: list = None,
        disable_web_page_preview: bool = False,
        reply_markup: ReplyMarkup = None,
    ) -> Result:
        """Edit text message

        Args:
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
                Disables link previews for links in this message

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, *optional*):
                The message reply markup


        Returns:
            :class:`~pytdbot.types.Result`
        """

        if not self.use_message_database:
            load_message = await self.getMessage(chat_id, message_id)
            if load_message.is_error:
                return load_message

        if entities is None:
            if parse_mode is not None:
                parse = await self.parseText(text, parse_mode=parse_mode)
                if parse.is_error:
                    return parse
                else:
                    _text = parse.result
            else:
                _text = {"@type": "formattedText", "text": text, "entities": []}
        else:
            _text = {"@type": "formattedText", "text": text, "entities": entities}

        data = {
            "@type": "editMessageText",
            "chat_id": chat_id,
            "message_id": message_id,
            "input_message_content": {
                "@type": "inputMessageText",
                "text": _text,
                "disable_web_page_preview": disable_web_page_preview,
            },
        }

        if isinstance(reply_markup, ReplyMarkup):
            data["reply_markup"] = reply_markup.to_dict()

        return await self.invoke(data)

    async def parseText(
        self,
        text: str,
        parse_mode: str = "markdownv2",
    ) -> Result:
        """Parses Bold, Italic, Underline, Strikethrough, Spoiler, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text

        Args:
            text (``str``):
                The text to parse

            parse_mode (``str``):
                Text parse mode. Currently supported: markdown, markdownv2 and html. Defaults to "markdownv2"

        Returns:
            :class:`~pytdbot.types.Result`
        """
        if not text or not parse_mode:
            return

        if parse_mode.lower() == "markdown":
            _data = {"@type": "textParseModeMarkdown", "version": 1}
        elif parse_mode.lower() == "markdownv2":
            _data = {"@type": "textParseModeMarkdown", "version": 2}
        elif parse_mode.lower() == "html":
            _data = {"@type": "textParseModeHTML"}
        else:
            raise ValueError(
                "Invalid parse_mode. Currently supported: markdown, markdownv2, html"
            )
        data = {
            "@type": "parseTextEntities",
            "text": text,
            "parse_mode": _data,
        }

        return await self.invoke(data)
