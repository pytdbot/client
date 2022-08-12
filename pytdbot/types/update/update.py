from base64 import b64decode
from typing import Union
from ujson import dumps
from pytdbot.utils import escape_html, escape_markdown
from pytdbot.types import (
    Response,
    InlineKeyboardMarkup,
    ShowKeyboardMarkup,
    ForceReply,
    RemoveKeyboard,
    InputFile,
    InputThumbnail,
)
import pytdbot


class Update:
    """Wrapper for the updates.

    Args:
        client (:class:`~pytdbot.Client`): The client object.
        update (``dict``): The update received from TDLib.
    """

    SERVICE_MESSAGE_TYPES = [
        "messageChatAddMembers",
        "messageBasicGroupChatCreate",
        "messageChatChangePhoto",
        "messageChatChangeTitle",
        "messageChatDeleteMember",
        "messageChatDeletePhoto",
        "messageChatJoinByLink",
        "messageChatJoinByRequest",
        "messageChatSetTheme",
        "messageChatUpgradeFrom",
        "messageChatUpgradeTo",
        "messageCustomServiceAction",
        "messageGameScore",
        "messageInviteVideoChatParticipants",
        "messagePinMessage",
        "messageSupergroupChatCreate",
        "messageVideoChatEnded",
        "messageVideoChatScheduled",
        "messageVideoChatStarted",
    ]

    def __init__(self, client: "pytdbot.Client", update: dict) -> None:
        self.client = client
        self.update = update
        self.type_ = update["@type"]
        self._store = {}

    def __getitem__(self, key):
        return self.update[key]

    def __setitem__(self, key, value):
        self.update[key] = value

    def __delitem__(self, key):
        del self.update[key]

    def __contains__(self, item):
        return item in self.update

    def __iter__(self):
        return iter(self.update.items())

    def __str__(self):
        return dumps(self.update, indent=4)

    @property
    def chat_id(self) -> int:
        """The chat id of the update.

        Returns:
            ``int``
        """
        if self.type_ in [
            "updateNewMessage",
            "updateMessageSendSucceeded",
            "updateMessageSendFailed",
        ]:
            return self.update["message"]["chat_id"]
        elif "chat_id" in self.update:
            return self.update["chat_id"]

    @property
    def from_id(self) -> int:
        """The user id of the sender of the update.

        Returns:
            ``int``
        """
        if self.type_ in [
            "updateNewMessage",
            "updateMessageSendSucceeded",
            "updateMessageSendFailed",
        ]:
            if self.update["message"]["sender_id"]["@type"] == "messageSenderChat":
                return self.update["message"]["sender_id"]["chat_id"]
            else:
                return self.update["message"]["sender_id"]["user_id"]
        elif "user_id" in self.update:
            return self.update["user_id"]
        elif "sender_user_id" in self.update:
            return self.update["sender_user_id"]

    @property
    def message_id(self) -> int:
        """The message id of the received update.

        Returns:
            ``int``
        """
        if self.type_ in [
            "updateNewMessage",
            "updateMessageSendSucceeded",
            "updateMessageSendFailed",
        ]:
            return self.update["message"]["id"]
        elif "message_id" in self.update:
            return self.update["message_id"]
        elif "inline_message_id" in self.update:
            return self.update["inline_message_id"]

    @property
    def reply_to_message_id(self) -> int:
        """The message id of the replied message."""
        if self.type_ in [
            "updateNewMessage",
            "updateMessageSendSucceeded",
            "updateMessageSendFailed",
        ]:
            return self.update["message"]["reply_to_message_id"]

    @property
    def content_type(self) -> str:
        """The content type of the received message.

        Returns:
            ``str``
        """
        if self.type_ in [
            "updateNewMessage",
            "updateMessageSendSucceeded",
            "updateMessageSendFailed",
        ]:
            return self.update["message"]["content"]["@type"]
        elif self.type_ == "updateMessageContent":
            return self.update["new_content"]["@type"]

    @property
    def text(self) -> str:
        """The text of the message.

        Returns:
            ``str``
        """
        if self.type_ == "updateNewMessage" and self.content_type == "messageText":
            return self.update["message"]["content"]["text"]["text"]
        elif self.type_ == "updateMessageContent":
            if "text" in self.update["new_content"]:
                return self.update["new_content"]["text"]["text"]

    @property
    def entities(self) -> list:
        """The entities of the message."""
        if self.type_ in [
            "updateNewMessage",
            "updateMessageSendSucceeded",
            "updateMessageSendFailed",
        ]:
            if self.content_type == "messageText":
                return self.update["message"]["content"]["text"]["entities"]
            elif "caption" in self.update["message"]["content"]:
                return self.update["message"]["content"]["caption"]["entities"]
        elif self.type_ == "updateMessageContent":
            if self.content_type == "messageText":
                return self.update["new_content"]["text"]["entities"]
            elif "caption" in self.update["new_content"]:
                return self.update["new_content"]["caption"]["entities"]

    @property
    def caption(self) -> str:
        """The caption of the received media.

        Returns:
            ``str``
        """
        if self.type_ in [
            "updateNewMessage",
            "updateMessageSendSucceeded",
            "updateMessageSendFailed",
        ]:
            if "caption" in self.update["message"]["content"]:
                return self.update["message"]["content"]["caption"]["text"]
        elif self.type_ == "updateMessageContent":
            if "caption" in self.update["new_content"]:
                return self.update["new_content"]["caption"]["text"]

    @property
    def data(self) -> str:
        """The callback data.

        Returns:
            ``str``: The callback data.
        """
        if "data" in self._store:
            return self._store["data"]
        elif self.type_ in ["updateNewCallbackQuery", "updateNewInlineCallbackQuery"]:
            if self.update["payload"]["@type"] in [
                "callbackQueryPayloadData",
                "callbackQueryPayloadDataWithPassword",
            ]:
                decoded_data = b64decode(self.update["payload"]["data"]).decode("utf-8")
                self._store["data"] = decoded_data
                return decoded_data

    @property
    def query(self) -> str:
        """The query of the inline query or the chosen inline result.

        Returns:
            ``str``
        """
        if self.type_ in ["updateNewInlineQuery", "updateNewChosenInlineResult"]:
            return self.update["query"]

    @property
    def file_id(self) -> str:
        """Remote file id.

        Returns:
            ``str``
        """
        if self.type_ not in [
            "updateNewMessage",
            "updateMessageSendSucceeded",
            "updateMessageSendFailed",
        ]:
            return
        if "content" in self.update["message"]:
            if self.update["message"]["content"]["@type"] == "messageDocument":
                return self.update["message"]["content"]["document"]["document"][
                    "remote"
                ]["id"]
            elif self.update["message"]["content"]["@type"] == "messageVideo":
                return self.update["message"]["content"]["video"]["video"]["remote"][
                    "id"
                ]
            elif self.update["message"]["content"]["@type"] == "messageAnimation":
                return self.update["message"]["content"]["animation"]["animation"][
                    "remote"
                ]["id"]
            elif self.update["message"]["content"]["@type"] == "messageAudio":
                return self.update["message"]["content"]["audio"]["audio"]["remote"][
                    "id"
                ]
            elif self.update["message"]["content"]["@type"] == "messageVoiceNote":
                return self.update["message"]["content"]["voice_note"]["voice"][
                    "remote"
                ]["id"]
            elif self.update["message"]["content"]["@type"] == "messagePhoto":
                return self.update["message"]["content"]["photo"]["sizes"][-1]["photo"][
                    "remote"
                ]["id"]
            elif self.update["message"]["content"]["@type"] == "messageSticker":
                return self.update["message"]["content"]["sticker"]["sticker"][
                    "remote"
                ]["id"]
            elif self.update["message"]["content"]["@type"] == "messageVideoNote":
                return self.update["message"]["content"]["video_note"]["video"][
                    "remote"
                ]["id"]

    @property
    def is_user(self) -> bool:
        """True, if the update is sent by regular user.

        Returns:
            ``bool``
        """
        if isinstance(self.from_id, int):
            return self.from_id > 0

    @property
    def is_private(self) -> bool:
        """True, if the update is sent on private chat.

        Returns:
            ``bool``
        """
        if isinstance(self.chat_id, int):
            return self.chat_id > 0

    @property
    def is_service(self) -> bool:
        """True, if the update is service message.

        Returns:
            ``bool``
        """
        return self.content_type in self.SERVICE_MESSAGE_TYPES

    async def mention(self, parse_mode: str = "markdown", version: int = 1) -> str:
        """Get the text_mention of the message sender.

        Args:
            parse_mode (``str``, optional):
                The parse mode of the mention. Defaults to "markdown".

            version (``int``, optional):
                If the parse mode is "markdown", pass the version of the markdown. Defaults to 1.

        Returns:
            ``str``
        """
        if self.is_user:
            user = await self.client.getUser(self.from_id)
            if not user.is_error:
                name = user["first_name"]
                if parse_mode == "html":
                    return (
                        f"<a href='tg://user?id={self.from_id}'>{escape_html(name)}</a>"
                    )
                elif parse_mode == "markdown":
                    return f"[{escape_markdown(name, version=version)}](tg://user?id={self.from_id})"

    async def getRepliedMessage(
        self,
        timeout: float = None,
    ) -> Response:
        """Get the replied message."""
        if isinstance(self.message_id, int):
            return await self.client.getRepliedMessage(
                self.chat_id, self.message_id, timeout
            )

    async def getMessage(
        self,
        message_id: int,
        timeout: float = None,
    ) -> Response:
        """Get the message by id.

        Args:
            message_id (``int``):
                The message id.

            timeout (``float``, optional):
                Number of seconds to wait for the result before raising a `TimeoutError`.
        """
        if isinstance(message_id, int):
            return await self.client.getMessage(self.chat_id, message_id, timeout)

    async def getChat(
        self,
        timeout: float = None,
    ) -> Response:
        """Get chat info."""
        if isinstance(self.chat_id, int):
            return await self.client.getChat(self.chat_id, timeout)

    async def getUser(
        self,
        timeout: float = None,
    ) -> Response:
        """Get user info."""
        if self.is_user:
            return await self.client.getUser(self.from_id, timeout)

    async def pin(
        self,
        disable_notification: bool = False,
        only_for_self: bool = False,
        timeout: float = None,
    ) -> Response:
        """Pin the message.

        Args:
            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            only_for_self (``bool``, optional):
                True, if the message needs to be pinned for one side only; private chats only.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if isinstance(self.message_id, int):
            return await self.client.pinChatMessage(
                self.chat_id,
                self.message_id,
                disable_notification,
                only_for_self,
                timeout,
            )

    async def delete(
        self,
        revoke: bool = True,
        timeout: float = None,
    ) -> Response:
        """Delete the received message.

        Args:
            revoke (``bool``, optional):
                Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if isinstance(self.message_id, int):
            return await self.client.deleteMessages(
                self.chat_id, [self.message_id], revoke, timeout
            )

    async def forward(
        self,
        chat_id: int,
        message_id: int = None,
        in_game_share: bool = False,
        disable_notification: bool = False,
        timeout: float = None,
    ) -> Response:
        """Forward the message.

        Args:
            chat_id (``int``):
                The chat id.

            message_id (``int``, optional):
                The message id. If None, the current message will be forwarded. Defaults to None.

            in_game_share (``bool``, optional):
                True, if a game message is being shared from a launched game; applies only to game messages.

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if (
            isinstance(self.message_id, int) or isinstance(message_id, int)
        ) and isinstance(self.chat_id, int):
            return await self.client.forwardMessage(
                chat_id,
                self.chat_id,
                message_id or self.message_id,
                in_game_share,
                disable_notification,
                timeout,
            )

    async def reply_text(
        self,
        text: str,
        quote: bool = None,
        entities: list = None,
        parse_mode: str = "markdown",
        disable_web_page_preview: bool = False,
        disable_notification: dict = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
        timeout: float = None,
    ) -> Response:
        """Reply to the message with text. Shortcut for :meth:`~pytdbot.Client.sendTextMessage`.

        Example:


            .. code-block:: python

                update.reply_text("Hello, world!",quote=True)

        Instead of:


            .. code-block:: python

                await client.sendTextMessage(
                    update.chat_id,
                    "Hello, world!",
                    reply_to_message_id=update.message_id
                )

        Args:
            text (``str``):
                The text of the message to be sent.

            quote (``bool``, optional)
                If True, the message is sent as a reply to this message. Ignored if ``reply_to_message_id`` is specified. Default to ``True`` in group/channel chats and ``False`` in private chats.

            entities (``list``, optional):
                List of `MessageEntity` objects to parse in the text. If you want to send a text with formatting, use *parse_mode* instead.

            parse_mode (``str``, optional):
                Mode for parsing entities. Defaults to "markdown".

            disable_web_page_preview (``bool``, optional):
                Disables link previews for links in this message.

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            protect_content (``bool``, optional):
                If True, the content of the message must be protected from forwarding and saving.

            message_thread_id (``int``, optional):
                If not 0, a message thread identifier in which the message will be sent.

            reply_to_message_id (``int``, optional):
                Identifier of the message to reply to or 0.

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, optional):
                The message reply markup.

        Returns:
            :class:`~pytdbot.types.Response`
        """

        if quote == False:
            reply_to_message_id = 0
        elif quote == True:
            reply_to_message_id = self.message_id
        else:
            if self.is_private:
                reply_to_message_id = 0
            else:
                reply_to_message_id = self.message_id

        if isinstance(self.chat_id, int):
            return await self.client.sendTextMessage(
                self.chat_id,
                text,
                entities=entities,
                parse_mode=parse_mode,
                disable_web_page_preview=disable_web_page_preview,
                disable_notification=disable_notification,
                protect_content=protect_content,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                timeout=timeout,
            )

    async def reply_animation(
        self,
        animation: Union[InputFile, str],
        thumbnail: InputThumbnail = None,
        quote: bool = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = "markdown",
        added_sticker_file_ids: list = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
        timeout: float = None,
    ) -> Response:
        """Reply to the message with an animation. Shortcut for :meth:`~pytdbot.Client.sendAnimation`.

        Example:

            .. code-block:: python

                update.reply_animation(
                    'https://c.tenor.com/eXZyHOtNs7gAAAAC/cxyduck-cxydck.gif',
                    quote=True
                )

        Instead of:

            .. code-block:: python

                await client.sendAnimation(
                    update.chat_id,
                    'https://c.tenor.com/eXZyHOtNs7gAAAAC/cxyduck-cxydck.gif',
                    reply_to_message_id=update.message_id
                )

        Args:
            animation (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``, optional):
                Animation to send. Pass a file_id as string to send an animation that exists on the Telegram servers, pass an HTTP URL as a string to send animation by URL, or pass :class:`~pytdbot.types.InputFileLocal` to upload an animation that exists on the local machine.

            thumbnail (:class:`~pytdbot.types.InputThumbnail`, optional):
                Thumbnail of the animation to send.

            quote (``bool``, optional)
                If True, the message is sent as a reply to this message. Ignored if ``reply_to_message_id`` is specified. Default to ``True`` in group/channel chats and ``False`` in private chats.

            caption (``str``, optional):
                Animation caption.

            caption_entities (``list``, optional):
                List of `MessageEntity` objects to parse in the animation caption.

            parse_mode (``str``, optional):
                Mode for parsing entities. Defaults to "markdown".

            added_sticker_file_ids (``list``, optional):
                List of file identifiers of new sticker set that should be added to the current sticker set.

            duration (``int``, optional):
                Duration of sent animation in seconds.

            width (``int``, optional):
                Animation width.

            height (``int``, optional):
                Animation height.

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            protect_content (``bool``, optional):
                If True, the content of the message must be protected from forwarding and saving.

            message_thread_id (``int``, optional):
                If not 0, a message thread identifier in which the message will be sent.

            reply_to_message_id (``int``, optional):
                Identifier of the message to reply to or 0.

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, optional):
                The message reply markup.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if quote == False:
            reply_to_message_id = 0
        elif quote == True:
            reply_to_message_id = self.message_id
        else:
            if self.is_private:
                reply_to_message_id = 0
            else:
                reply_to_message_id = self.message_id

        if isinstance(self.chat_id, int):
            return await self.client.sendAnimation(
                self.chat_id,
                animation,
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
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                timeout=timeout,
            )

    async def reply_audio(
        self,
        audio: Union[InputFile, str],
        quote: bool = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = "markdown",
        duration: int = None,
        performer: str = None,
        title: str = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
        timeout: float = None,
    ) -> Response:
        """Reply to the message with an audio. Shortcut for :meth:`~pytdbot.Client.Methods.sendAudio`.

        Example:

            .. code-block:: python

                await message.reply_audio(
                    'https://t.me/KKK9K/1592',
                    quote=True
                )

        Instead of:

            .. code-block:: python

                await client.sendAudio(
                    message.chat_id,
                    'https://t.me/KKK9K/1592',
                    reply_to_message_id=message.message_id
                )

        Args:
            audio (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``, optional):
                Audio file to send. Pass a file_id as string to send an audio that exists on the Telegram servers, pass an HTTP URL as a string to send an audio from the Internet, or pass :class:`~pytdbot.types.InputFileLocal` to upload an audio from a file on the local machine.

            quote (``bool``, optional)
                If True, the message is sent as a reply to this message. Ignored if ``reply_to_message_id`` is specified. Default to ``True`` in group/channel chats and ``False`` in private chats.

            caption (``str``, optional):
                Audio caption.

            caption_entities (``list``, optional):
                List of `MessageEntity` objects to parse in the audio caption.

            parse_mode (``str``, optional):
                Mode for parsing entities. Defaults to "markdown".

            duration (``int``, optional):
                Duration of the audio in seconds.

            performer (``str``, optional):
                Performer of the audio as defined by sender or by audio tags.

            title (``str``, optional):
                Title of the audio as defined by sender or by audio tags.

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            protect_content (``bool``, optional):
                If True, the content of the message must be protected from forwarding and saving.

            message_thread_id (``int``, optional):
                If not 0, a message thread identifier in which the message will be sent.

            reply_to_message_id (``int``, optional):
                Identifier of the message to reply to or 0.

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, optional):
                The message reply markup.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if quote == False:
            reply_to_message_id = 0
        elif quote == True:
            reply_to_message_id = self.message_id
        else:
            if self.is_private:
                reply_to_message_id = 0
            else:
                reply_to_message_id = self.message_id

        if isinstance(self.chat_id, int):
            return await self.client.sendAudio(
                self.chat_id,
                audio,
                caption=caption,
                caption_entities=caption_entities,
                parse_mode=parse_mode,
                duration=duration,
                performer=performer,
                title=title,
                disable_notification=disable_notification,
                protect_content=protect_content,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                timeout=timeout,
            )

    async def reply_document(
        self,
        document: Union[InputFile, str],
        quote: bool = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = "markdown",
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
        timeout: float = None,
    ) -> Response:
        """Reply to the message with a document. Shortcut for :meth:`~pytdbot.Client.sendDocument`.

        Example:

            .. code-block:: python

                await message.reply_document(
                    'https://github.com/tdlib/td/archive/refs/heads/master.zip',
                    quote=True
                )

        Instead of:

            .. code-block:: python

                await client.sendDocument(
                    message.chat_id,
                    'https://github.com/tdlib/td/archive/refs/heads/master.zip',
                    reply_to_message_id=message.message_id
                )

        Args:
            document (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``, optional):
                File to send. Pass a file_id as string to send a file that exists on the Telegram servers, pass an HTTP URL as a string to send a file from the Internet, or pass :class:`~pytdbot.types.InputFileLocal` to upload a file from the local machine.

            quote (``bool``, optional)
                If True, the message is sent as a reply to this message. Ignored if ``reply_to_message_id`` is specified. Default to ``True`` in group/channel chats and ``False`` in private chats.

            caption (``str``, optional):
                Document caption.

            caption_entities (``list``, optional):
                List of `MessageEntity` objects to parse in the document caption.

            parse_mode (``str``, optional):
                Mode for parsing entities. Defaults to "markdown".

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            protect_content (``bool``, optional):
                If True, the content of the message must be protected from forwarding and saving.

            message_thread_id (``int``, optional):
                If not 0, a message thread identifier in which the message will be sent.

            reply_to_message_id (``int``, optional):
                Identifier of the message to reply to or 0.

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, optional):
                The message reply markup.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if quote == False:
            reply_to_message_id = 0
        elif quote == True:
            reply_to_message_id = self.message_id
        else:
            if self.is_private:
                reply_to_message_id = 0
            else:
                reply_to_message_id = self.message_id

        if isinstance(self.chat_id, int):
            return await self.client.sendDocument(
                self.chat_id,
                document,
                caption=caption,
                caption_entities=caption_entities,
                parse_mode=parse_mode,
                disable_notification=disable_notification,
                protect_content=protect_content,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                timeout=timeout,
            )

    async def reply_sticker(
        self,
        sticker: Union[InputFile, str],
        emoji: str = None,
        quote: bool = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
        timeout: float = None,
    ) -> Response:
        """Reply to the message with a sticker. Shortcut for :meth:`~pytdbot.Client.sendSticker`.

        Example:

            .. code-block:: python

                await message.reply_sticker(
                    types.InputFileLocal('sticker.webp'),
                    quote=True
                )

        Instead of:

            .. code-block:: python

                await client.sendSticker(
                    message.chat_id,
                    types.InputFileLocal('sticker.webp'),
                    reply_to_message_id=message.message_id
                )

        Args:
            sticker (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``, optional):
                Sticker to send. Pass a file_id as string to send a file that exists on the Telegram servers, pass an HTTP URL as a string to send a file from the Internet, or pass :class:`~pytdbot.types.InputFileLocal` to upload a sticker from the local machine.

            emoji (``str``, optional):
                Emoji associated with the sticker.

            quote (``bool``, optional)
                If True, the message is sent as a reply to this message. Ignored if ``reply_to_message_id`` is specified. Default to ``True`` in group/channel chats and ``False`` in private chats.

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            protect_content (``bool``, optional):
                If True, the content of the message must be protected from forwarding and saving.

            message_thread_id (``int``, optional):
                If not 0, a message thread identifier in which the message will be sent.

            reply_to_message_id (``int``, optional):
                Identifier of the message to reply to or 0.

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, optional):
                The message reply markup.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if quote == False:
            reply_to_message_id = 0
        elif quote == True:
            reply_to_message_id = self.message_id
        else:
            if self.is_private:
                reply_to_message_id = 0
            else:
                reply_to_message_id = self.message_id

        if isinstance(self.chat_id, int):
            return await self.client.sendSticker(
                self.chat_id,
                sticker,
                emoji=emoji,
                disable_notification=disable_notification,
                protect_content=protect_content,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                timeout=timeout,
            )

    async def reply_video(
        self,
        video: Union[InputFile, str],
        quote: bool = None,
        duration: int = None,
        width: int = None,
        height: int = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = "markdown",
        supports_streaming: bool = False,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
        timeout: float = None,
    ) -> Response:
        """Reply to the message with a video. Shortcut for :meth:`~pytdbot.Client.sendVideo`.

        Example:

            .. code-block:: python

                await message.reply_video(
                    types.InputFileLocal('video.mp4'),
                    quote=True
                )

        Instead of:

            .. code-block:: python

                await client.sendVideo(
                    message.chat_id,
                    types.InputFileLocal('video.mp4'),
                    reply_to_message_id=message.message_id
                )

        Args:
            video (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``, optional):
                Video to send. Pass a file_id as string to send a file that exists on the Telegram servers, pass an HTTP URL as a string to send a file from the Internet, or pass :class:`~pytdbot.types.InputFileLocal` to upload a video from the local machine.

            quote (``bool``, optional)
                If True, the message is sent as a reply to this message. Ignored if ``reply_to_message_id`` is specified. Default to ``True`` in group/channel chats and ``False`` in private chats.

            duration (``int``, optional):
                Duration of sent video in seconds.

            width (``int``, optional):
                Video width.

            height (``int``, optional):
                Video height.

            caption (``str``, optional):
                Video caption.

            caption_entities (``list``, optional):
                List of `MessageEntity` objects to parse in the document caption.

            parse_mode (``str``, optional):
                Mode for parsing entities. Defaults to "markdown".

            supports_streaming (``bool``, optional):
                Pass True, if the uploaded video is suitable for streaming.

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            protect_content (``bool``, optional):
                If True, the content of the message must be protected from forwarding and saving.

            message_thread_id (``int``, optional):
                If not 0, a message thread identifier in which the message will be sent.

            reply_to_message_id (``int``, optional):
                Identifier of the message to reply to or 0.

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, optional):
                The message reply markup.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if quote == False:
            reply_to_message_id = 0
        elif quote == True:
            reply_to_message_id = self.message_id
        else:
            if self.is_private:
                reply_to_message_id = 0
            else:
                reply_to_message_id = self.message_id

        if isinstance(self.chat_id, int):
            return await self.client.sendVideo(
                self.chat_id,
                video,
                duration=duration,
                width=width,
                height=height,
                caption=caption,
                caption_entities=caption_entities,
                parse_mode=parse_mode,
                supports_streaming=supports_streaming,
                disable_notification=disable_notification,
                protect_content=protect_content,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                timeout=timeout,
            )

    async def reply_photo(
        self,
        photo: Union[InputFile, str],
        quote: bool = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = "markdown",
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
        timeout: float = None,
    ) -> Response:
        """Reply to the message with a photo. Shortcut for :meth:`~pytdbot.Client.sendPhoto`.

        Example:

            .. code-block:: python

                await message.reply_photo(
                    types.InputFileLocal('photo.jpg'),
                    quote=True
                )

        Instead of:

            .. code-block:: python

                await client.sendPhoto(
                    message.chat_id,
                    types.InputFileLocal('photo.jpg'),
                    reply_to_message_id=message.message_id
                )

        Args:
            photo (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``, optional):
                Photo to send. Pass a file_id as string to send a file that exists on the Telegram servers, pass an HTTP URL as a string to send a file from the Internet, or pass :class:`~pytdbot.types.InputFileLocal` to upload a photo from the local machine.

            quote (``bool``, optional)
                If True, the message is sent as a reply to this message. Ignored if ``reply_to_message_id`` is specified. Default to ``True`` in group/channel chats and ``False`` in private chats.

            caption (``str``, optional):
                Photo caption.

            caption_entities (``list``, optional):
                List of `MessageEntity` objects to parse in the document caption.

            parse_mode (``str``, optional):
                Mode for parsing entities. Defaults to "markdown".

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            protect_content (``bool``, optional):
                If True, the content of the message must be protected from forwarding and saving.

            message_thread_id (``int``, optional):
                If not 0, a message thread identifier in which the message will be sent.

            reply_to_message_id (``int``, optional):
                Identifier of the message to reply to or 0.

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, optional):
                The message reply markup.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if quote == False:
            reply_to_message_id = 0
        elif quote == True:
            reply_to_message_id = self.message_id
        else:
            if self.is_private:
                reply_to_message_id = 0
            else:
                reply_to_message_id = self.message_id

        if isinstance(self.chat_id, int):
            return await self.client.sendPhoto(
                self.chat_id,
                photo,
                caption=caption,
                caption_entities=caption_entities,
                parse_mode=parse_mode,
                disable_notification=disable_notification,
                protect_content=protect_content,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                timeout=timeout,
            )

    async def reply_voice(
        self,
        voice: Union[InputFile, str],
        quote: bool = None,
        caption: str = None,
        caption_entities: list = None,
        parse_mode: str = "markdown",
        duration: int = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        message_thread_id: int = 0,
        reply_to_message_id: int = 0,
        reply_markup: Union[
            InlineKeyboardMarkup, ShowKeyboardMarkup, ForceReply, RemoveKeyboard
        ] = None,
        timeout: float = None,
    ) -> Response:
        """Reply to the message with a voice. Shortcut for :meth:`~pytdbot.Client.sendVoice`.

        Example:

            .. code-block:: python

                await message.reply_voice(
                    types.InputFileLocal('voice.ogg'),
                    quote=True
                )

        Instead of:

            .. code-block:: python

                await client.sendVoice(
                    message.chat_id,
                    types.InputFileLocal('voice.ogg'),
                    reply_to_message_id=message.message_id
                )

        Args:
            voice (:class:`~pytdbot.types.InputFileRemote` | :class:`~pytdbot.types.InputFileLocal` | ``str``, optional):
                Voice to send. Pass a file_id as string to send a file that exists on the Telegram servers, pass an HTTP URL as a string to send a file from the Internet, or pass :class:`~pytdbot.types.InputFileLocal` to upload a voice from the local machine.

            quote (``bool``, optional)
                If True, the message is sent as a reply to this message. Ignored if ``reply_to_message_id`` is specified. Default to ``True`` in group/channel chats and ``False`` in private chats.

            caption (``str``, optional):
                Voice caption.

            caption_entities (``list``, optional):
                List of `MessageEntity` objects to parse in the voice caption.

            parse_mode (``str``, optional):
                Mode for parsing entities. Defaults to "markdown".

            duration (``int``, optional):
                Duration of sent voice in seconds.

            disable_notification (``bool``, optional):
                If True, disable notification for the message.

            protect_content (``bool``, optional):
                If True, the content of the message must be protected from forwarding and saving.

            message_thread_id (``int``, optional):
                If not 0, a message thread identifier in which the message will be sent.

            reply_to_message_id (``int``, optional):
                Identifier of the message to reply to or 0.

            reply_markup (:class:`~pytdbot.types.InlineKeyboardMarkup` | :class:`~pytdbot.types.ShowKeyboardMarkup` | :class:`~pytdbot.types.ForceReply` | :class:`~pytdbot.types.RemoveKeyboard`, optional):
                The message reply markup.

        Returns:
            :class:`~pytdbot.types.Response`
        """
        if quote == False:
            reply_to_message_id = 0
        elif quote == True:
            reply_to_message_id = self.message_id
        else:
            if self.is_private:
                reply_to_message_id = 0
            else:
                reply_to_message_id = self.message_id

        if isinstance(self.chat_id, int):
            return await self.client.sendVoice(
                self.chat_id,
                voice,
                caption=caption,
                caption_entities=caption_entities,
                parse_mode=parse_mode,
                duration=duration,
                disable_notification=disable_notification,
                protect_content=protect_content,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
                timeout=timeout,
            )
