from typing import Union
from functools import lru_cache

import pytdbot


class MessageSenderBoundMethods:
    def __init__(self):
        self._client: pytdbot.Client

    @property
    @lru_cache(1)
    def from_id(self) -> Union[int, None]:
        """Returns the message sender's ID. ``None`` if not found"""

        if isinstance(self, pytdbot.types.MessageSenderUser):
            return self.user_id

        if isinstance(self, pytdbot.types.MessageSenderChat):
            return self.chat_id

        return None

    @property
    @lru_cache(1)
    def is_user(self) -> bool:
        """Returns ``True`` if the message sender is a user"""

        return isinstance(self, pytdbot.types.MessageSenderUser)

    @property
    @lru_cache(1)
    def is_chat(self) -> bool:
        """Returns ``True`` if the message sender is a chat"""

        return isinstance(self, pytdbot.types.MessageSenderChat)
