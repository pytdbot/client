from __future__ import annotations

from functools import lru_cache

import pytdbot


class WidgetQueryBoundMethods:
    def __init__(self):
        self._client: pytdbot.Client

    @property
    @lru_cache(1)
    def query_data(self) -> pytdbot.utils.CallbackData:
        r"""Query data that was set by :func:`~pytdbot.utils.callback_data`

        Args:
            action (``Any``):
                Action name

            data (``Any``, *optional*):
                Query data
        """

        return pytdbot.utils.load_callback_data(self.data)

    @property
    @lru_cache(1)
    def text(self) -> str:
        r"""Query data decoded as str"""

        return self.data.decode("utf-8")

    async def getMessage(self) -> pytdbot.types.Error | pytdbot.types.Message | None:
        r"""Get widget query message"""

        if isinstance(self, pytdbot.types.UpdateNewWidgetQuery):
            return await self._client.getMessage(
                chat_id=self.chat_id, message_id=self.message_id
            )

    async def answer(self, data: str) -> pytdbot.types.Error | pytdbot.types.Ok:
        r"""Answer to widget query. Shortcut for :meth:`~pytdbot.Client.answerWidgetQuery`"""

        return await self._client.answerWidgetQuery(widget_query_id=self.id, data=data)
