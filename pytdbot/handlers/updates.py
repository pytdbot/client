import pytdbot

from .handler import Handler
from typing import Callable
from asyncio import iscoroutinefunction
from logging import getLogger

logger = getLogger(__name__)


class Updates:
    """Auto generated TDLib updates"""

    def on_updateAuthorizationState(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The user authorization state has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateAuthorizationState", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateAuthorizationState", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateAuthorizationState", filters, position
                )
            return func

        return decorator

    def on_updateNewMessage(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new message was received; can also be an outgoing message

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNewMessage", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNewMessage", self, position)
            else:
                func._handler = Handler(func, "updateNewMessage", filters, position)
            return func

        return decorator

    def on_updateMessageSendAcknowledged(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A request to send a message has reached the Telegram server\. This doesn't mean that the message will be sent successfully\. This update is sent only if the option "use\_quick\_ack" is set to true\. This update may be sent multiple times for the same message

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateMessageSendAcknowledged", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateMessageSendAcknowledged", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateMessageSendAcknowledged", filters, position
                )
            return func

        return decorator

    def on_updateMessageSendSucceeded(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A message has been successfully sent

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateMessageSendSucceeded", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateMessageSendSucceeded", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateMessageSendSucceeded", filters, position
                )
            return func

        return decorator

    def on_updateMessageSendFailed(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A message failed to send\. Be aware that some messages being sent can be irrecoverably deleted, in which case updateDeleteMessages will be received instead of this update

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateMessageSendFailed", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateMessageSendFailed", self, position)
            else:
                func._handler = Handler(
                    func, "updateMessageSendFailed", filters, position
                )
            return func

        return decorator

    def on_updateMessageContent(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The message content has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateMessageContent", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateMessageContent", self, position)
            else:
                func._handler = Handler(func, "updateMessageContent", filters, position)
            return func

        return decorator

    def on_updateMessageEdited(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A message was edited\. Changes in the message content will come in a separate updateMessageContent

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateMessageEdited", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateMessageEdited", self, position)
            else:
                func._handler = Handler(func, "updateMessageEdited", filters, position)
            return func

        return decorator

    def on_updateMessageIsPinned(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The message pinned state was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateMessageIsPinned", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateMessageIsPinned", self, position)
            else:
                func._handler = Handler(
                    func, "updateMessageIsPinned", filters, position
                )
            return func

        return decorator

    def on_updateMessageInteractionInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The information about interactions with a message has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateMessageInteractionInfo", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateMessageInteractionInfo", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateMessageInteractionInfo", filters, position
                )
            return func

        return decorator

    def on_updateMessageContentOpened(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The message content was opened\. Updates voice note messages to "listened", video note messages to "viewed" and starts the self\-destruct timer

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateMessageContentOpened", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateMessageContentOpened", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateMessageContentOpened", filters, position
                )
            return func

        return decorator

    def on_updateMessageMentionRead(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A message with an unread mention was read

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateMessageMentionRead", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateMessageMentionRead", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateMessageMentionRead", filters, position
                )
            return func

        return decorator

    def on_updateMessageUnreadReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of unread reactions added to a message was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateMessageUnreadReactions", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateMessageUnreadReactions", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateMessageUnreadReactions", filters, position
                )
            return func

        return decorator

    def on_updateMessageLiveLocationViewed(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A message with a live location was viewed\. When the update is received, the application is supposed to update the live location

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateMessageLiveLocationViewed", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateMessageLiveLocationViewed", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateMessageLiveLocationViewed", filters, position
                )
            return func

        return decorator

    def on_updateNewChat(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new chat has been loaded/created\. This update is guaranteed to come before the chat identifier is returned to the application\. The chat field changes will be reported through separate updates

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNewChat", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNewChat", self, position)
            else:
                func._handler = Handler(func, "updateNewChat", filters, position)
            return func

        return decorator

    def on_updateChatTitle(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The title of a chat was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatTitle", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatTitle", self, position)
            else:
                func._handler = Handler(func, "updateChatTitle", filters, position)
            return func

        return decorator

    def on_updateChatPhoto(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat photo was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatPhoto", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatPhoto", self, position)
            else:
                func._handler = Handler(func, "updateChatPhoto", filters, position)
            return func

        return decorator

    def on_updateChatAccentColor(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat accent color has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatAccentColor", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatAccentColor", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatAccentColor", filters, position
                )
            return func

        return decorator

    def on_updateChatBackgroundCustomEmoji(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat's custom emoji for reply background has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatBackgroundCustomEmoji", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatBackgroundCustomEmoji", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatBackgroundCustomEmoji", filters, position
                )
            return func

        return decorator

    def on_updateChatPermissions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Chat permissions were changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatPermissions", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatPermissions", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatPermissions", filters, position
                )
            return func

        return decorator

    def on_updateChatLastMessage(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The last message of a chat was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatLastMessage", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatLastMessage", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatLastMessage", filters, position
                )
            return func

        return decorator

    def on_updateChatPosition(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The position of a chat in a chat list has changed\. An updateChatLastMessage or updateChatDraftMessage update might be sent instead of the update

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatPosition", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatPosition", self, position)
            else:
                func._handler = Handler(func, "updateChatPosition", filters, position)
            return func

        return decorator

    def on_updateChatReadInbox(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Incoming messages were read or the number of unread messages has been changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatReadInbox", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatReadInbox", self, position)
            else:
                func._handler = Handler(func, "updateChatReadInbox", filters, position)
            return func

        return decorator

    def on_updateChatReadOutbox(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Outgoing messages were read

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatReadOutbox", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatReadOutbox", self, position)
            else:
                func._handler = Handler(func, "updateChatReadOutbox", filters, position)
            return func

        return decorator

    def on_updateChatActionBar(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The chat action bar was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatActionBar", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatActionBar", self, position)
            else:
                func._handler = Handler(func, "updateChatActionBar", filters, position)
            return func

        return decorator

    def on_updateChatAvailableReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The chat available reactions were changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatAvailableReactions", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatAvailableReactions", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatAvailableReactions", filters, position
                )
            return func

        return decorator

    def on_updateChatDraftMessage(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat draft has changed\. Be aware that the update may come in the currently opened chat but with old content of the draft\. If the user has changed the content of the draft, this update mustn't be applied

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatDraftMessage", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatDraftMessage", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatDraftMessage", filters, position
                )
            return func

        return decorator

    def on_updateChatMessageSender(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The message sender that is selected to send messages in a chat has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatMessageSender", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatMessageSender", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatMessageSender", filters, position
                )
            return func

        return decorator

    def on_updateChatMessageAutoDeleteTime(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The message auto\-delete or self\-destruct timer setting for a chat was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatMessageAutoDeleteTime", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatMessageAutoDeleteTime", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatMessageAutoDeleteTime", filters, position
                )
            return func

        return decorator

    def on_updateChatNotificationSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Notification settings for a chat were changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatNotificationSettings", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatNotificationSettings", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatNotificationSettings", filters, position
                )
            return func

        return decorator

    def on_updateChatPendingJoinRequests(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The chat pending join requests were changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatPendingJoinRequests", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatPendingJoinRequests", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatPendingJoinRequests", filters, position
                )
            return func

        return decorator

    def on_updateChatReplyMarkup(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The default chat reply markup was changed\. Can occur because new messages with reply markup were received or because an old reply markup was hidden by the user

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatReplyMarkup", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatReplyMarkup", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatReplyMarkup", filters, position
                )
            return func

        return decorator

    def on_updateChatBackground(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The chat background was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatBackground", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatBackground", self, position)
            else:
                func._handler = Handler(func, "updateChatBackground", filters, position)
            return func

        return decorator

    def on_updateChatTheme(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The chat theme was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatTheme", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatTheme", self, position)
            else:
                func._handler = Handler(func, "updateChatTheme", filters, position)
            return func

        return decorator

    def on_updateChatUnreadMentionCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The chat unread\_mention\_count has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatUnreadMentionCount", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatUnreadMentionCount", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatUnreadMentionCount", filters, position
                )
            return func

        return decorator

    def on_updateChatUnreadReactionCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The chat unread\_reaction\_count has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatUnreadReactionCount", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatUnreadReactionCount", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatUnreadReactionCount", filters, position
                )
            return func

        return decorator

    def on_updateChatVideoChat(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat video chat state has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatVideoChat", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatVideoChat", self, position)
            else:
                func._handler = Handler(func, "updateChatVideoChat", filters, position)
            return func

        return decorator

    def on_updateChatDefaultDisableNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The value of the default disable\_notification parameter, used when a message is sent to the chat, was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatDefaultDisableNotification", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatDefaultDisableNotification", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatDefaultDisableNotification", filters, position
                )
            return func

        return decorator

    def on_updateChatHasProtectedContent(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat content was allowed or restricted for saving

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatHasProtectedContent", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatHasProtectedContent", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatHasProtectedContent", filters, position
                )
            return func

        return decorator

    def on_updateChatIsTranslatable(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Translation of chat messages was enabled or disabled

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatIsTranslatable", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatIsTranslatable", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatIsTranslatable", filters, position
                )
            return func

        return decorator

    def on_updateChatIsMarkedAsUnread(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat was marked as unread or was read

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatIsMarkedAsUnread", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatIsMarkedAsUnread", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatIsMarkedAsUnread", filters, position
                )
            return func

        return decorator

    def on_updateChatViewAsTopics(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat default appearance has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatViewAsTopics", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatViewAsTopics", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatViewAsTopics", filters, position
                )
            return func

        return decorator

    def on_updateChatBlockList(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat was blocked or unblocked

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatBlockList", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatBlockList", self, position)
            else:
                func._handler = Handler(func, "updateChatBlockList", filters, position)
            return func

        return decorator

    def on_updateChatHasScheduledMessages(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat's has\_scheduled\_messages field has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatHasScheduledMessages", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatHasScheduledMessages", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatHasScheduledMessages", filters, position
                )
            return func

        return decorator

    def on_updateChatFolders(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of chat folders or a chat folder has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatFolders", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatFolders", self, position)
            else:
                func._handler = Handler(func, "updateChatFolders", filters, position)
            return func

        return decorator

    def on_updateChatOnlineMemberCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The number of online group members has changed\. This update with non\-zero number of online group members is sent only for currently opened chats\. There is no guarantee that it is sent just after the number of online users has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateChatOnlineMemberCount", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatOnlineMemberCount", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatOnlineMemberCount", filters, position
                )
            return func

        return decorator

    def on_updateForumTopicInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Basic information about a topic in a forum chat was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateForumTopicInfo", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateForumTopicInfo", self, position)
            else:
                func._handler = Handler(func, "updateForumTopicInfo", filters, position)
            return func

        return decorator

    def on_updateScopeNotificationSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Notification settings for some type of chats were updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateScopeNotificationSettings", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateScopeNotificationSettings", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateScopeNotificationSettings", filters, position
                )
            return func

        return decorator

    def on_updateNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A notification was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNotification", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNotification", self, position)
            else:
                func._handler = Handler(func, "updateNotification", filters, position)
            return func

        return decorator

    def on_updateNotificationGroup(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A list of active notifications in a notification group has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNotificationGroup", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNotificationGroup", self, position)
            else:
                func._handler = Handler(
                    func, "updateNotificationGroup", filters, position
                )
            return func

        return decorator

    def on_updateActiveNotifications(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Contains active notifications that were shown on previous application launches\. This update is sent only if the message database is used\. In that case it comes once before any updateNotification and updateNotificationGroup update

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateActiveNotifications", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateActiveNotifications", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateActiveNotifications", filters, position
                )
            return func

        return decorator

    def on_updateHavePendingNotifications(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Describes whether there are some pending notification updates\. Can be used to prevent application from killing, while there are some pending notifications

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateHavePendingNotifications", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateHavePendingNotifications", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateHavePendingNotifications", filters, position
                )
            return func

        return decorator

    def on_updateDeleteMessages(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some messages were deleted

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateDeleteMessages", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateDeleteMessages", self, position)
            else:
                func._handler = Handler(func, "updateDeleteMessages", filters, position)
            return func

        return decorator

    def on_updateChatAction(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A message sender activity in the chat has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatAction", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatAction", self, position)
            else:
                func._handler = Handler(func, "updateChatAction", filters, position)
            return func

        return decorator

    def on_updateUserStatus(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The user went online or offline

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateUserStatus", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateUserStatus", self, position)
            else:
                func._handler = Handler(func, "updateUserStatus", filters, position)
            return func

        return decorator

    def on_updateUser(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some data of a user has changed\. This update is guaranteed to come before the user identifier is returned to the application

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateUser", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateUser", self, position)
            else:
                func._handler = Handler(func, "updateUser", filters, position)
            return func

        return decorator

    def on_updateBasicGroup(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some data of a basic group has changed\. This update is guaranteed to come before the basic group identifier is returned to the application

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateBasicGroup", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateBasicGroup", self, position)
            else:
                func._handler = Handler(func, "updateBasicGroup", filters, position)
            return func

        return decorator

    def on_updateSupergroup(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some data of a supergroup or a channel has changed\. This update is guaranteed to come before the supergroup identifier is returned to the application

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateSupergroup", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateSupergroup", self, position)
            else:
                func._handler = Handler(func, "updateSupergroup", filters, position)
            return func

        return decorator

    def on_updateSecretChat(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some data of a secret chat has changed\. This update is guaranteed to come before the secret chat identifier is returned to the application

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateSecretChat", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateSecretChat", self, position)
            else:
                func._handler = Handler(func, "updateSecretChat", filters, position)
            return func

        return decorator

    def on_updateUserFullInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some data in userFullInfo has been changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateUserFullInfo", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateUserFullInfo", self, position)
            else:
                func._handler = Handler(func, "updateUserFullInfo", filters, position)
            return func

        return decorator

    def on_updateBasicGroupFullInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some data in basicGroupFullInfo has been changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateBasicGroupFullInfo", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateBasicGroupFullInfo", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateBasicGroupFullInfo", filters, position
                )
            return func

        return decorator

    def on_updateSupergroupFullInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some data in supergroupFullInfo has been changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateSupergroupFullInfo", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateSupergroupFullInfo", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateSupergroupFullInfo", filters, position
                )
            return func

        return decorator

    def on_updateServiceNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A service notification from the server was received\. Upon receiving this the application must show a popup with the content of the notification

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateServiceNotification", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateServiceNotification", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateServiceNotification", filters, position
                )
            return func

        return decorator

    def on_updateFile(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Information about a file was updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateFile", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateFile", self, position)
            else:
                func._handler = Handler(func, "updateFile", filters, position)
            return func

        return decorator

    def on_updateFileGenerationStart(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The file generation process needs to be started by the application

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateFileGenerationStart", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateFileGenerationStart", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateFileGenerationStart", filters, position
                )
            return func

        return decorator

    def on_updateFileGenerationStop(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """File generation is no longer needed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateFileGenerationStop", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateFileGenerationStop", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateFileGenerationStop", filters, position
                )
            return func

        return decorator

    def on_updateFileDownloads(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The state of the file download list has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateFileDownloads", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateFileDownloads", self, position)
            else:
                func._handler = Handler(func, "updateFileDownloads", filters, position)
            return func

        return decorator

    def on_updateFileAddedToDownloads(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A file was added to the file download list\. This update is sent only after file download list is loaded for the first time

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateFileAddedToDownloads", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateFileAddedToDownloads", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateFileAddedToDownloads", filters, position
                )
            return func

        return decorator

    def on_updateFileDownload(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A file download was changed\. This update is sent only after file download list is loaded for the first time

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateFileDownload", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateFileDownload", self, position)
            else:
                func._handler = Handler(func, "updateFileDownload", filters, position)
            return func

        return decorator

    def on_updateFileRemovedFromDownloads(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A file was removed from the file download list\. This update is sent only after file download list is loaded for the first time

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateFileRemovedFromDownloads", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateFileRemovedFromDownloads", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateFileRemovedFromDownloads", filters, position
                )
            return func

        return decorator

    def on_updateCall(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """New call was created or information about a call was updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateCall", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateCall", self, position)
            else:
                func._handler = Handler(func, "updateCall", filters, position)
            return func

        return decorator

    def on_updateGroupCall(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Information about a group call was updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateGroupCall", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateGroupCall", self, position)
            else:
                func._handler = Handler(func, "updateGroupCall", filters, position)
            return func

        return decorator

    def on_updateGroupCallParticipant(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Information about a group call participant was changed\. The updates are sent only after the group call is received through getGroupCall and only if the call is joined or being joined

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateGroupCallParticipant", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateGroupCallParticipant", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateGroupCallParticipant", filters, position
                )
            return func

        return decorator

    def on_updateNewCallSignalingData(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """New call signaling data arrived

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateNewCallSignalingData", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateNewCallSignalingData", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateNewCallSignalingData", filters, position
                )
            return func

        return decorator

    def on_updateUserPrivacySettingRules(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some privacy setting rules have been changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateUserPrivacySettingRules", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateUserPrivacySettingRules", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateUserPrivacySettingRules", filters, position
                )
            return func

        return decorator

    def on_updateUnreadMessageCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Number of unread messages in a chat list has changed\. This update is sent only if the message database is used

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateUnreadMessageCount", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateUnreadMessageCount", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateUnreadMessageCount", filters, position
                )
            return func

        return decorator

    def on_updateUnreadChatCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Number of unread chats, i\.e\. with unread messages or marked as unread, has changed\. This update is sent only if the message database is used

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateUnreadChatCount", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateUnreadChatCount", self, position)
            else:
                func._handler = Handler(
                    func, "updateUnreadChatCount", filters, position
                )
            return func

        return decorator

    def on_updateStory(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A story was changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateStory", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateStory", self, position)
            else:
                func._handler = Handler(func, "updateStory", filters, position)
            return func

        return decorator

    def on_updateStoryDeleted(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A story became inaccessible

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateStoryDeleted", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateStoryDeleted", self, position)
            else:
                func._handler = Handler(func, "updateStoryDeleted", filters, position)
            return func

        return decorator

    def on_updateStorySendSucceeded(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A story has been successfully sent

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateStorySendSucceeded", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateStorySendSucceeded", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateStorySendSucceeded", filters, position
                )
            return func

        return decorator

    def on_updateStorySendFailed(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A story failed to send\. If the story sending is canceled, then updateStoryDeleted will be received instead of this update

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateStorySendFailed", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateStorySendFailed", self, position)
            else:
                func._handler = Handler(
                    func, "updateStorySendFailed", filters, position
                )
            return func

        return decorator

    def on_updateChatActiveStories(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of active stories posted by a specific chat has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatActiveStories", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatActiveStories", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatActiveStories", filters, position
                )
            return func

        return decorator

    def on_updateStoryListChatCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Number of chats in a story list has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateStoryListChatCount", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateStoryListChatCount", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateStoryListChatCount", filters, position
                )
            return func

        return decorator

    def on_updateStoryStealthMode(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Story stealth mode settings have changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateStoryStealthMode", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateStoryStealthMode", self, position)
            else:
                func._handler = Handler(
                    func, "updateStoryStealthMode", filters, position
                )
            return func

        return decorator

    def on_updateOption(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """An option changed its value

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateOption", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateOption", self, position)
            else:
                func._handler = Handler(func, "updateOption", filters, position)
            return func

        return decorator

    def on_updateStickerSet(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A sticker set has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateStickerSet", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateStickerSet", self, position)
            else:
                func._handler = Handler(func, "updateStickerSet", filters, position)
            return func

        return decorator

    def on_updateInstalledStickerSets(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of installed sticker sets was updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateInstalledStickerSets", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateInstalledStickerSets", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateInstalledStickerSets", filters, position
                )
            return func

        return decorator

    def on_updateTrendingStickerSets(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of trending sticker sets was updated or some of them were viewed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateTrendingStickerSets", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateTrendingStickerSets", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateTrendingStickerSets", filters, position
                )
            return func

        return decorator

    def on_updateRecentStickers(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of recently used stickers was updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateRecentStickers", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateRecentStickers", self, position)
            else:
                func._handler = Handler(func, "updateRecentStickers", filters, position)
            return func

        return decorator

    def on_updateFavoriteStickers(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of favorite stickers was updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateFavoriteStickers", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateFavoriteStickers", self, position)
            else:
                func._handler = Handler(
                    func, "updateFavoriteStickers", filters, position
                )
            return func

        return decorator

    def on_updateSavedAnimations(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of saved animations was updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateSavedAnimations", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateSavedAnimations", self, position)
            else:
                func._handler = Handler(
                    func, "updateSavedAnimations", filters, position
                )
            return func

        return decorator

    def on_updateSavedNotificationSounds(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of saved notification sounds was updated\. This update may not be sent until information about a notification sound was requested for the first time

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateSavedNotificationSounds", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateSavedNotificationSounds", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateSavedNotificationSounds", filters, position
                )
            return func

        return decorator

    def on_updateSelectedBackground(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The selected background has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateSelectedBackground", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateSelectedBackground", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateSelectedBackground", filters, position
                )
            return func

        return decorator

    def on_updateChatThemes(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of available chat themes has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatThemes", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatThemes", self, position)
            else:
                func._handler = Handler(func, "updateChatThemes", filters, position)
            return func

        return decorator

    def on_updateAccentColors(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of supported accent colors has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateAccentColors", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateAccentColors", self, position)
            else:
                func._handler = Handler(func, "updateAccentColors", filters, position)
            return func

        return decorator

    def on_updateProfileAccentColors(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of supported accent colors for user profiles has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateProfileAccentColors", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateProfileAccentColors", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateProfileAccentColors", filters, position
                )
            return func

        return decorator

    def on_updateLanguagePackStrings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some language pack strings have been updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateLanguagePackStrings", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateLanguagePackStrings", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateLanguagePackStrings", filters, position
                )
            return func

        return decorator

    def on_updateConnectionState(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The connection state has changed\. This update must be used only to show a human\-readable description of the connection state

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateConnectionState", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateConnectionState", self, position)
            else:
                func._handler = Handler(
                    func, "updateConnectionState", filters, position
                )
            return func

        return decorator

    def on_updateTermsOfService(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """New terms of service must be accepted by the user\. If the terms of service are declined, then the deleteAccount method must be called with the reason "Decline ToS update"

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateTermsOfService", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateTermsOfService", self, position)
            else:
                func._handler = Handler(func, "updateTermsOfService", filters, position)
            return func

        return decorator

    def on_updateUsersNearby(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of users nearby has changed\. The update is guaranteed to be sent only 60 seconds after a successful searchChatsNearby request

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateUsersNearby", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateUsersNearby", self, position)
            else:
                func._handler = Handler(func, "updateUsersNearby", filters, position)
            return func

        return decorator

    def on_updateUnconfirmedSession(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The first unconfirmed session has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateUnconfirmedSession", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateUnconfirmedSession", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateUnconfirmedSession", filters, position
                )
            return func

        return decorator

    def on_updateAttachmentMenuBots(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of bots added to attachment or side menu has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateAttachmentMenuBots", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateAttachmentMenuBots", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateAttachmentMenuBots", filters, position
                )
            return func

        return decorator

    def on_updateWebAppMessageSent(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A message was sent by an opened Web App, so the Web App needs to be closed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateWebAppMessageSent", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateWebAppMessageSent", self, position)
            else:
                func._handler = Handler(
                    func, "updateWebAppMessageSent", filters, position
                )
            return func

        return decorator

    def on_updateActiveEmojiReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of active emoji reactions has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateActiveEmojiReactions", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateActiveEmojiReactions", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateActiveEmojiReactions", filters, position
                )
            return func

        return decorator

    def on_updateDefaultReactionType(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The type of default reaction has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateDefaultReactionType", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateDefaultReactionType", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateDefaultReactionType", filters, position
                )
            return func

        return decorator

    def on_updateSpeechRecognitionTrial(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The parameters of speech recognition without Telegram Premium subscription has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateSpeechRecognitionTrial", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateSpeechRecognitionTrial", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateSpeechRecognitionTrial", filters, position
                )
            return func

        return decorator

    def on_updateDiceEmojis(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of supported dice emojis has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateDiceEmojis", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateDiceEmojis", self, position)
            else:
                func._handler = Handler(func, "updateDiceEmojis", filters, position)
            return func

        return decorator

    def on_updateAnimatedEmojiMessageClicked(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Some animated emoji message was clicked and a big animated sticker must be played if the message is visible on the screen\. chatActionWatchingAnimations with the text of the message needs to be sent if the sticker is played

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateAnimatedEmojiMessageClicked", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateAnimatedEmojiMessageClicked", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateAnimatedEmojiMessageClicked", filters, position
                )
            return func

        return decorator

    def on_updateAnimationSearchParameters(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The parameters of animation search through getOption\("animation\_search\_bot\_username"\) bot has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateAnimationSearchParameters", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateAnimationSearchParameters", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateAnimationSearchParameters", filters, position
                )
            return func

        return decorator

    def on_updateSuggestedActions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The list of suggested to the user actions has changed

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateSuggestedActions", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateSuggestedActions", self, position)
            else:
                func._handler = Handler(
                    func, "updateSuggestedActions", filters, position
                )
            return func

        return decorator

    def on_updateAddChatMembersPrivacyForbidden(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Adding users to a chat has failed because of their privacy settings\. An invite link can be shared with the users if appropriate

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateAddChatMembersPrivacyForbidden", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateAddChatMembersPrivacyForbidden", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateAddChatMembersPrivacyForbidden", filters, position
                )
            return func

        return decorator

    def on_updateAutosaveSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Autosave settings for some type of chats were updated

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateAutosaveSettings", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateAutosaveSettings", self, position)
            else:
                func._handler = Handler(
                    func, "updateAutosaveSettings", filters, position
                )
            return func

        return decorator

    def on_updateNewInlineQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new incoming inline query; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNewInlineQuery", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNewInlineQuery", self, position)
            else:
                func._handler = Handler(func, "updateNewInlineQuery", filters, position)
            return func

        return decorator

    def on_updateNewChosenInlineResult(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """The user has chosen a result of an inline query; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateNewChosenInlineResult", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateNewChosenInlineResult", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateNewChosenInlineResult", filters, position
                )
            return func

        return decorator

    def on_updateNewCallbackQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new incoming callback query; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNewCallbackQuery", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNewCallbackQuery", self, position)
            else:
                func._handler = Handler(
                    func, "updateNewCallbackQuery", filters, position
                )
            return func

        return decorator

    def on_updateNewInlineCallbackQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new incoming callback query from a message sent via a bot; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateNewInlineCallbackQuery", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateNewInlineCallbackQuery", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateNewInlineCallbackQuery", filters, position
                )
            return func

        return decorator

    def on_updateNewShippingQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new incoming shipping query; for bots only\. Only for invoices with flexible price

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNewShippingQuery", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNewShippingQuery", self, position)
            else:
                func._handler = Handler(
                    func, "updateNewShippingQuery", filters, position
                )
            return func

        return decorator

    def on_updateNewPreCheckoutQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new incoming pre\-checkout query; for bots only\. Contains full information about a checkout

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateNewPreCheckoutQuery", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateNewPreCheckoutQuery", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateNewPreCheckoutQuery", filters, position
                )
            return func

        return decorator

    def on_updateNewCustomEvent(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new incoming event; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNewCustomEvent", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNewCustomEvent", self, position)
            else:
                func._handler = Handler(func, "updateNewCustomEvent", filters, position)
            return func

        return decorator

    def on_updateNewCustomQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A new incoming query; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateNewCustomQuery", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateNewCustomQuery", self, position)
            else:
                func._handler = Handler(func, "updateNewCustomQuery", filters, position)
            return func

        return decorator

    def on_updatePoll(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A poll was updated; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updatePoll", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updatePoll", self, position)
            else:
                func._handler = Handler(func, "updatePoll", filters, position)
            return func

        return decorator

    def on_updatePollAnswer(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A user changed the answer to a poll; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updatePollAnswer", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updatePollAnswer", self, position)
            else:
                func._handler = Handler(func, "updatePollAnswer", filters, position)
            return func

        return decorator

    def on_updateChatMember(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """User rights changed in a chat; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatMember", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatMember", self, position)
            else:
                func._handler = Handler(func, "updateChatMember", filters, position)
            return func

        return decorator

    def on_updateNewChatJoinRequest(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A user sent a join request to a chat; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        "updateNewChatJoinRequest", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateNewChatJoinRequest", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateNewChatJoinRequest", filters, position
                )
            return func

        return decorator

    def on_updateChatBoost(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """A chat boost has changed; for bots only

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updateChatBoost", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatBoost", self, position)
            else:
                func._handler = Handler(func, "updateChatBoost", filters, position)
            return func

        return decorator

    def on_updates(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        """Contains a list of updates

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("updates", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updates", self, position)
            else:
                func._handler = Handler(func, "updates", filters, position)
            return func

        return decorator
