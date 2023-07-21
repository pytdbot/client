from .base import ReplyMarkup


class ShowKeyboardMarkup(ReplyMarkup):
    """Contains a custom keyboard layout to quickly reply to bots."""

    def __init__(
        self,
        rows: list,
        resize_keyboard: bool = False,
        one_time: bool = False,
        is_personal: bool = True,
        input_field_placeholder: str = None,
    ):
        """

        Args:
            rows (``list``):
                A list of rows of inline keyboard buttons

            resize_keyboard (``bool``, *optional*):
                True, if the application needs to resize the keyboard vertically. Default is ``False``

            one_time (``bool``, *optional*):
                True, if the application needs to hide the keyboard after use. Default is ``False``

            is_personal (``bool``, *optional*):
                True, if the keyboard must automatically be shown to the current user. For outgoing messages, specify true to show the keyboard only for the mentioned users and for the target user of a reply. Default is ``True``

            input_field_placeholder (``str``, *optional*):
                If non-empty, the placeholder to be shown in the input field when the keyboard is active; 0-64 characters

        """

        self.rows = rows
        self.resize_keyboard = resize_keyboard
        self.one_time = one_time
        self.is_personal = is_personal
        self.input_field_placeholder = input_field_placeholder

    def to_dict(self) -> dict:
        """Converts the object to a dictionary

        Returns:
            :py:class:`dict`: Show keyboard
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "rows": self.rows,
            "resize_keyboard": self.resize_keyboard,
            "one_time": self.one_time,
            "is_personal": self.is_personal,
            "input_field_placeholder": self.input_field_placeholder,
        }


class ShowKeyboardButton:
    """Show keyboard types"""

    def location(text: str) -> dict:
        """A button that sends the user's location when pressed; available only in private chats

        Args:
            text (``str``):
                Text of the button

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {"@type": "keyboardButtonTypeRequestLocation"},
        }

    def phone_number(text: str) -> dict:
        """A button that sends the user's phone number when pressed; available only in private chats

        Args:
            text (``str``):
                Text of the button

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {"@type": "keyboardButtonTypeRequestPhoneNumber"},
        }

    def poll(text: str, force_regular: bool = None, force_quiz: bool = None) -> dict:
        """A button that allows the user to create and send a poll when pressed; available only in private chats

        Args:
            text (``str``):
                Text of the button

            force_regular (``bool``, *optional*):
                If True, only regular polls must be allowed to create

            force_quiz (``bool``, *optional*):
                If True, only polls in quiz mode must be allowed to create

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {
                "@type": "keyboardButtonTypeRequestPoll",
                "force_regular": force_regular,
                "force_quiz": force_quiz,
            },
        }

    def request_user(
        text: str,
        id: int,
        restrict_user_is_bot: bool = None,
        user_is_bot: bool = None,
        restrict_user_is_premium: bool = None,
        user_is_premium: bool = None,
    ) -> dict:
        """A button that requests a user to be shared by the current user; available only in private chats. Use the method shareUserWithBot to complete the request

        Args:
            text (``str``):
                Text of the button

            id (``int``):
                Unique button identifier

            restrict_user_is_bot (``bool``, *optional*):
                True, if the shared user must or must not be a bot

            user_is_bot (``bool``, *optional*):
                True, if the shared user must be a bot; otherwise, the shared user must no be a bot. Ignored if ``restrict_user_is_bot`` is ``False``

            restrict_user_is_premium (``bool``, *optional*):
                True, if the shared user must or must not be a Telegram Premium user

            user_is_premium (``bool``, *optional*):
                True, if the shared user must be a Telegram Premium user; otherwise, the shared user must no be a Telegram Premium user. Ignored if ``restrict_user_is_premium`` is ``False``

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {
                "@type": "keyboardButtonTypeRequestUser",
                "id": id,
                "restrict_user_is_bot": restrict_user_is_bot,
                "user_is_bot": user_is_bot,
                "restrict_user_is_premium": restrict_user_is_premium,
                "user_is_premium": user_is_premium,
            },
        }

    def request_chat(
        text: str,
        id: int,
        chat_is_channel: bool,
        restrict_chat_is_forum: bool = None,
        chat_is_forum: bool = None,
        restrict_chat_has_username: bool = None,
        chat_has_username: bool = None,
        chat_is_created: bool = None,
        user_administrator_rights: dict = None,
        bot_administrator_rights: dict = None,
        bot_is_member: bool = None,
    ) -> dict:
        """A button that requests a user to be shared by the current user; available only in private chats. Use the method shareUserWithBot to complete the request

        Args:
            text (``str``):
                Text of the button

            id (``int``):
                Unique button identifier

            chat_is_channel (``bool``):
                True, if the chat must be a channel; otherwise, a basic group or a supergroup chat is shared

            restrict_chat_is_forum (``bool``, *optional*):
                True, if the chat must or must not be a forum supergroup

            chat_is_forum (``bool``, *optional*):
                True, if the chat must be a forum supergroup; otherwise, the chat must not be a forum supergroup. Ignored if ``restrict_chat_is_forum`` is ``False``

            restrict_chat_has_username (``bool``, *optional*):
                True, if the chat must or must not have a username

            chat_has_username (``bool``, *optional*):
                if the chat must have a username; otherwise, the chat must not have a username. Ignored if ``restrict_chat_has_username`` is ``False``

            chat_is_created (``bool``, *optional*):
                True, if the chat must be created by the current user

            user_administrator_rights (``chatAdministratorRights``, *optional*):
                Expected user administrator rights in the chat; may be null if they aren't restricted

            bot_administrator_rights (``chatAdministratorRights``, *optional*):
                Expected user administrator rights in the chat; may be null if they aren't restricted

            bot_is_member (``bool``, *optional*):
                True, if the bot must be a member of the chat; for basic group and supergroup chats only

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {
                "@type": "keyboardButtonTypeRequestChat",
                "id": id,
                "chat_is_channel": chat_is_channel,
                "restrict_chat_is_forum": restrict_chat_is_forum,
                "chat_is_forum": chat_is_forum,
                "restrict_chat_has_username": restrict_chat_has_username,
                "chat_has_username": chat_has_username,
                "chat_is_created": chat_is_created,
                "user_administrator_rights": user_administrator_rights,
                "bot_administrator_rights": bot_administrator_rights,
                "bot_is_member": bot_is_member,
            },
        }

    def text(text: str) -> dict:
        """A simple button, with text that must be sent when the button is pressed

        Args:
            text (``str``):
                Text of the button

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {"@type": "keyboardButtonTypeText"},
        }
