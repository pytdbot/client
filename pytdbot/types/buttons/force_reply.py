from .base import ReplyMarkup


class ForceReply(ReplyMarkup):
    """Instructs application to force a reply to this message."""

    def __init__(self, is_personal: bool = True, input_field_placeholder: str = None):
        """

        Args:
            is_personal (``bool``, optional):
                True, if a forced reply must automatically be shown to the current user. For outgoing messages, specify true to show the forced reply only for the mentioned users and for the target user of a reply. Defaults to True.

            input_field_placeholder (``str``, optional):
                If non-empty, the placeholder to be shown in the input field when the keyboard is active; 0-64 characters.

        """

        self.is_personal = is_personal
        self.input_field_placeholder = input_field_placeholder

    def to_dict(self) -> dict:
        """Converts the object to a dictionary.

        Returns:
            dict: Force reply.
        """

        return {
            "@type": "replyMarkupForceReply",
            "is_personal": self.is_personal,
            "input_field_placeholder": self.input_field_placeholder,
        }
