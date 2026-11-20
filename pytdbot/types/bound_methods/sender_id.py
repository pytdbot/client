from functools import cached_property

import pytdbot


class MessageSenderBoundMethods:
    def __init__(self):
        self._client: pytdbot.Client

    @cached_property
    def from_id(self) -> int | None:
        """Returns the message sender's ID. ``None`` if not found"""

        if isinstance(self, pytdbot.types.MessageSenderUser):
            return self.user_id

        if isinstance(self, pytdbot.types.MessageSenderChat):
            return self.chat_id

        return None

    @cached_property
    def is_user(self) -> bool:
        """Returns ``True`` if the message sender is a user"""

        return isinstance(self, pytdbot.types.MessageSenderUser)

    @cached_property
    def is_chat(self) -> bool:
        """Returns ``True`` if the message sender is a chat"""

        return isinstance(self, pytdbot.types.MessageSenderChat)
