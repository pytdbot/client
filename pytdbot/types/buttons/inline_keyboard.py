from base64 import b64encode as b64en
from .base import ReplyMarkup


class InlineKeyboardMarkup(ReplyMarkup):
    """Inline keyboard markup"""

    def __init__(self, rows: list):
        """Inline keyboard markup.
        Args:
            rows (``list``):
                A list of rows of inline keyboard buttons.
        """

        self.rows = rows

    def to_dict(self) -> dict:
        """Converts the object to a dictionary.

        Returns:
            :py:class:`dict`: Inline keyboard.
        """

        return {"@type": "replyMarkupInlineKeyboard", "rows": self.rows}


class InlineKeyboardButton:
    """Inline keyboard button types."""

    def buy(text: str) -> dict:
        """A button to buy something. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type `messageInvoice <https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_invoice.html>`__.

        Args:
            text (``str``):
                Text of the button.

        Returns:
            :py:class:`dict`: Inline keyboard button.
        """

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {
                "@type": "inlineKeyboardButtonTypeBuy",
            },
        }

    def game(text: str) -> dict:
        """A button with a game that sends a callback query to a bot. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type `messageGame <https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_game.html>`__.

        Args:
            text (``str``):
                Text of the button.

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {
                "@type": "inlineKeyboardButtonTypeCallbackGame",
            },
        }

    def callback(text: str, data: bytes) -> dict:
        """A button that sends a callback query to a bot.

        Args:
            text (``str``):
                Text of the button.

            data (``bytes``):
                Data to be sent to the bot via a callback query.

        Returns:
            :py:class:`dict`
        """

        if isinstance(data, str):
            data = data.encode("utf-8")

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {
                "@type": "inlineKeyboardButtonTypeCallback",
                "data": b64en(data).decode(),
            },
        }

    def password(text: str, data: bytes) -> dict:
        """A button that sends a callback query to a bot.

        Args:
            text (``str``):
                Text of the button.

            data (``bytes``):
                Data to be sent to the bot via a callback query.

        Returns:
            :py:class:`dict`
        """

        if isinstance(data, str):
            data = data.encode("utf-8")

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {
                "@type": "inlineKeyboardButtonTypeCallbackWithPassword",
                "data": b64en(data).decode(),
            },
        }

    def login(text: str, url: str, id: int) -> dict:
        """A button that opens a specified URL and automatically authorize the current user if allowed to do so.

        Args:
            text (``str``):
                Text of the button.

            url (``str``):
                An HTTP URL to open.

            id (``str``):
                Unique button identifier.

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {"@type": "inlineKeyboardButtonTypeLoginUrl", "url": url, "id": id},
        }

    def switch_inline(text: str, query: str, in_current_chat: bool = False) -> dict:
        """A button that forces an inline query to the bot to be inserted in the input field.

        Args:
            text (``str``):
                Text pf the button.

            query (``str``):
                Inline query to be sent to the bot.

            in_current_chat (``str``, *optional*):
                True, if the inline query must be sent from the current chat. Defaults to ``False``.

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {
                "@type": "inlineKeyboardButtonTypeSwitchInline",
                "query": query,
                "in_current_chat": in_current_chat,
            },
        }

    def url(text: str, url: str) -> dict:
        """A button that opens a specified URL.

        Args:
            text (``str``):
                Text of the button.

            url (``str``):
                HTTP or tg:// URL to open.

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {"@type": "inlineKeyboardButtonTypeUrl", "url": url},
        }

    def user(text: str, user_id: int) -> dict:
        """A button with a user reference to be handled in the same way as `textEntityTypeMentionName <https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_mention_name.html>`__ entities.

        Args:
            text (``str``):
                Text of the button.

            user_id (``str``):
                User identifier.

        Returns:
            :py:class:`dict`
        """

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {"@type": "inlineKeyboardButtonTypeUser", "user_id": user_id},
        }

    def webapp(text: str, url: str) -> dict:
        """A button that opens a web app by calling openWebApp

        Args:
            text (``str``):
                Text of the button.

            url (``str``):
                An HTTP URL to pass to openWebApp

        Returns:
            :py:class:`dict`: Inline keyboard button.
        """

        return {
            "@type": "inlineKeyboardButton",
            "text": text,
            "type": {"@type": "inlineKeyboardButtonTypeWebApp", "url": url},
        }
