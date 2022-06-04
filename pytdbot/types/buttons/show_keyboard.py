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
                A list of rows of inline keyboard buttons.

            resize_keyboard (``bool``, optional):
                True, if the application needs to resize the keyboard vertically. Defaults to False.

            one_time (``bool``, optional):
                True, if the application needs to hide the keyboard after use. Defaults to False.

            is_personal (``bool``, optional):
                True, if the keyboard must automatically be shown to the current user. For outgoing messages, specify true to show the keyboard only for the mentioned users and for the target user of a reply. Defaults to True.

            input_field_placeholder (``str``, optional):
                If non-empty, the placeholder to be shown in the input field when the keyboard is active; 0-64 characters.

        """

        self.rows = rows
        self.resize_keyboard = resize_keyboard
        self.one_time = one_time
        self.is_personal = is_personal
        self.input_field_placeholder = input_field_placeholder

    def to_dict(self) -> dict:
        """Converts the object to a dictionary.

        Returns:
            dict: Show keyboard.
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
        """A button that sends the user's location when pressed; available only in private chats.

        Args:
            text (``str``): Text of the button.

        Returns:
            dict
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {"@type": "keyboardButtonTypeRequestLocation"},
        }

    def phone_number(text: str) -> dict:
        """A button that sends the user's phone number when pressed; available only in private chats.

        Args:
            text (``str``): Text of the button.

        Returns:
            dict
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {"@type": "keyboardButtonTypeRequestPhoneNumber"},
        }

    def poll(text: str, force_regular: bool = None, force_quiz: bool = None) -> dict:
        """A button that allows the user to create and send a poll when pressed; available only in private chats.

        Args:
            text (``str``): Text of the button.
            force_regular (``bool``, optional): If True, only regular polls must be allowed to create.
            force_quiz (``bool``, optional): If True, only polls in quiz mode must be allowed to create.

        Returns:
            dict
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

    def text(text: str) -> dict:
        """A simple button, with text that must be sent when the button is pressed.

        Args:
            text (``str``): Text of the button.

        Returns:
            dict
        """

        return {
            "@type": "replyMarkupShowKeyboard",
            "text": text,
            "type": {"@type": "keyboardButtonTypeText"},
        }
