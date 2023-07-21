from .base import ReplyMarkup


class RemoveKeyboard(ReplyMarkup):
    """Instructs application to remove the keyboard once this message has been received. This kind of keyboard can't be received in an incoming message; instead, UpdateChatReplyMarkup with message_id == 0 will be sent."""

    def __init__(self, is_personal: bool = True):
        """

        Args:
            is_personal (``bool``, *optional*):
                True, if the keyboard is removed only for the mentioned users or the target user of a reply. Default is ``True``

        """

        self.is_personal = is_personal

    def to_dict(self) -> dict:
        """Converts the object to a dictionary

        Returns:
            :py:class:`dict`: Remove keyboard
        """

        return {"@type": "replyMarkupRemoveKeyboard", "is_personal": self.is_personal}
