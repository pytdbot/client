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
        r"""The user authorization state has changed

        Parameters:
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
        r"""A new message was received; can also be an outgoing message

        Parameters:
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
        r"""A request to send a message has reached the Telegram server\. This doesn't mean that the message will be sent successfully\. This update is sent only if the option \"use\_quick\_ack\" is set to true\. This update may be sent multiple times for the same message

        Parameters:
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
        r"""A message has been successfully sent

        Parameters:
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
        r"""A message failed to send\. Be aware that some messages being sent can be irrecoverably deleted, in which case updateDeleteMessages will be received instead of this update

        Parameters:
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
        r"""The message content has changed

        Parameters:
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
        r"""A message was edited\. Changes in the message content will come in a separate updateMessageContent

        Parameters:
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
        r"""The message pinned state was changed

        Parameters:
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
        r"""The information about interactions with a message has changed

        Parameters:
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
        r"""The message content was opened\. Updates voice note messages to \"listened\", video note messages to \"viewed\" and starts the self\-destruct timer

        Parameters:
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
        r"""A message with an unread mention was read

        Parameters:
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
        r"""The list of unread reactions added to a message was changed

        Parameters:
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

    def on_updateMessageFactCheck(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A fact\-check added to a message was changed

        Parameters:
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
                    self.add_handler("updateMessageFactCheck", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateMessageFactCheck", self, position)
            else:
                func._handler = Handler(
                    func, "updateMessageFactCheck", filters, position
                )
            return func

        return decorator

    def on_updateMessageLiveLocationViewed(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A message with a live location was viewed\. When the update is received, the application is expected to update the live location

        Parameters:
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

    def on_updateVideoPublished(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""An automatically scheduled message with video has been successfully sent after conversion

        Parameters:
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
                    self.add_handler("updateVideoPublished", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateVideoPublished", self, position)
            else:
                func._handler = Handler(func, "updateVideoPublished", filters, position)
            return func

        return decorator

    def on_updateNewChat(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A new chat has been loaded/created\. This update is guaranteed to come before the chat identifier is returned to the application\. The chat field changes will be reported through separate updates

        Parameters:
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
        r"""The title of a chat was changed

        Parameters:
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
        r"""A chat photo was changed

        Parameters:
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

    def on_updateChatAccentColors(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Chat accent colors have changed

        Parameters:
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
                    self.add_handler("updateChatAccentColors", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatAccentColors", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatAccentColors", filters, position
                )
            return func

        return decorator

    def on_updateChatPermissions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Chat permissions were changed

        Parameters:
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
        r"""The last message of a chat was changed

        Parameters:
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
        r"""The position of a chat in a chat list has changed\. An updateChatLastMessage or updateChatDraftMessage update might be sent instead of the update

        Parameters:
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

    def on_updateChatAddedToList(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A chat was added to a chat list

        Parameters:
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
                    self.add_handler("updateChatAddedToList", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatAddedToList", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatAddedToList", filters, position
                )
            return func

        return decorator

    def on_updateChatRemovedFromList(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A chat was removed from a chat list

        Parameters:
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
                        "updateChatRemovedFromList", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatRemovedFromList", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatRemovedFromList", filters, position
                )
            return func

        return decorator

    def on_updateChatReadInbox(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Incoming messages were read or the number of unread messages has been changed

        Parameters:
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
        r"""Outgoing messages were read

        Parameters:
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
        r"""The chat action bar was changed

        Parameters:
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

    def on_updateChatBusinessBotManageBar(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The bar for managing business bot was changed in a chat

        Parameters:
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
                        "updateChatBusinessBotManageBar", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateChatBusinessBotManageBar", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateChatBusinessBotManageBar", filters, position
                )
            return func

        return decorator

    def on_updateChatAvailableReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The chat available reactions were changed

        Parameters:
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
        r"""A chat draft has changed\. Be aware that the update may come in the currently opened chat but with old content of the draft\. If the user has changed the content of the draft, this update mustn't be applied

        Parameters:
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

    def on_updateChatEmojiStatus(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Chat emoji status has changed

        Parameters:
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
                    self.add_handler("updateChatEmojiStatus", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatEmojiStatus", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatEmojiStatus", filters, position
                )
            return func

        return decorator

    def on_updateChatMessageSender(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The message sender that is selected to send messages in a chat has changed

        Parameters:
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
        r"""The message auto\-delete or self\-destruct timer setting for a chat was changed

        Parameters:
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
        r"""Notification settings for a chat were changed

        Parameters:
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
        r"""The chat pending join requests were changed

        Parameters:
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
        r"""The default chat reply markup was changed\. Can occur because new messages with reply markup were received or because an old reply markup was hidden by the user

        Parameters:
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
        r"""The chat background was changed

        Parameters:
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
        r"""The chat theme was changed

        Parameters:
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
        r"""The chat unread\_mention\_count has changed

        Parameters:
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
        r"""The chat unread\_reaction\_count has changed

        Parameters:
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
        r"""A chat video chat state has changed

        Parameters:
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
        r"""The value of the default disable\_notification parameter, used when a message is sent to the chat, was changed

        Parameters:
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
        r"""A chat content was allowed or restricted for saving

        Parameters:
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
        r"""Translation of chat messages was enabled or disabled

        Parameters:
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
        r"""A chat was marked as unread or was read

        Parameters:
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
        r"""A chat default appearance has changed

        Parameters:
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
        r"""A chat was blocked or unblocked

        Parameters:
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
        r"""A chat's has\_scheduled\_messages field has changed

        Parameters:
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
        r"""The list of chat folders or a chat folder has changed

        Parameters:
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
        r"""The number of online group members has changed\. This update with non\-zero number of online group members is sent only for currently opened chats\. There is no guarantee that it is sent just after the number of online users has changed

        Parameters:
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

    def on_updateSavedMessagesTopic(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Basic information about a Saved Messages topic has changed\. This update is guaranteed to come before the topic identifier is returned to the application

        Parameters:
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
                        "updateSavedMessagesTopic", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateSavedMessagesTopic", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateSavedMessagesTopic", filters, position
                )
            return func

        return decorator

    def on_updateSavedMessagesTopicCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Number of Saved Messages topics has changed

        Parameters:
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
                        "updateSavedMessagesTopicCount", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateSavedMessagesTopicCount", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateSavedMessagesTopicCount", filters, position
                )
            return func

        return decorator

    def on_updateQuickReplyShortcut(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Basic information about a quick reply shortcut has changed\. This update is guaranteed to come before the quick shortcut name is returned to the application

        Parameters:
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
                        "updateQuickReplyShortcut", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateQuickReplyShortcut", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateQuickReplyShortcut", filters, position
                )
            return func

        return decorator

    def on_updateQuickReplyShortcutDeleted(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A quick reply shortcut and all its messages were deleted

        Parameters:
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
                        "updateQuickReplyShortcutDeleted", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateQuickReplyShortcutDeleted", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateQuickReplyShortcutDeleted", filters, position
                )
            return func

        return decorator

    def on_updateQuickReplyShortcuts(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The list of quick reply shortcuts has changed

        Parameters:
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
                        "updateQuickReplyShortcuts", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateQuickReplyShortcuts", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateQuickReplyShortcuts", filters, position
                )
            return func

        return decorator

    def on_updateQuickReplyShortcutMessages(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The list of quick reply shortcut messages has changed

        Parameters:
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
                        "updateQuickReplyShortcutMessages", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateQuickReplyShortcutMessages", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateQuickReplyShortcutMessages", filters, position
                )
            return func

        return decorator

    def on_updateForumTopicInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Basic information about a topic in a forum chat was changed

        Parameters:
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

    def on_updateForumTopic(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Information about a topic in a forum chat was changed

        Parameters:
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
                    self.add_handler("updateForumTopic", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateForumTopic", self, position)
            else:
                func._handler = Handler(func, "updateForumTopic", filters, position)
            return func

        return decorator

    def on_updateScopeNotificationSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Notification settings for some type of chats were updated

        Parameters:
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

    def on_updateReactionNotificationSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Notification settings for reactions were updated

        Parameters:
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
                        "updateReactionNotificationSettings", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateReactionNotificationSettings", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateReactionNotificationSettings", filters, position
                )
            return func

        return decorator

    def on_updateNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A notification was changed

        Parameters:
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
        r"""A list of active notifications in a notification group has changed

        Parameters:
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
        r"""Contains active notifications that were shown on previous application launches\. This update is sent only if the message database is used\. In that case it comes once before any updateNotification and updateNotificationGroup update

        Parameters:
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
        r"""Describes whether there are some pending notification updates\. Can be used to prevent application from killing, while there are some pending notifications

        Parameters:
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
        r"""Some messages were deleted

        Parameters:
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
        r"""A message sender activity in the chat has changed

        Parameters:
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
        r"""The user went online or offline

        Parameters:
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
        r"""Some data of a user has changed\. This update is guaranteed to come before the user identifier is returned to the application

        Parameters:
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
        r"""Some data of a basic group has changed\. This update is guaranteed to come before the basic group identifier is returned to the application

        Parameters:
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
        r"""Some data of a supergroup or a channel has changed\. This update is guaranteed to come before the supergroup identifier is returned to the application

        Parameters:
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
        r"""Some data of a secret chat has changed\. This update is guaranteed to come before the secret chat identifier is returned to the application

        Parameters:
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
        r"""Some data in userFullInfo has been changed

        Parameters:
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
        r"""Some data in basicGroupFullInfo has been changed

        Parameters:
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
        r"""Some data in supergroupFullInfo has been changed

        Parameters:
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
        r"""A service notification from the server was received\. Upon receiving this the application must show a popup with the content of the notification

        Parameters:
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
        r"""Information about a file was updated

        Parameters:
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
        r"""The file generation process needs to be started by the application\. Use setFileGenerationProgress and finishFileGeneration to generate the file

        Parameters:
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
        r"""File generation is no longer needed

        Parameters:
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
        r"""The state of the file download list has changed

        Parameters:
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
        r"""A file was added to the file download list\. This update is sent only after file download list is loaded for the first time

        Parameters:
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
        r"""A file download was changed\. This update is sent only after file download list is loaded for the first time

        Parameters:
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
        r"""A file was removed from the file download list\. This update is sent only after file download list is loaded for the first time

        Parameters:
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

    def on_updateApplicationVerificationRequired(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A request can't be completed unless application verification is performed; for official mobile applications only\. The method setApplicationVerificationToken must be called once the verification is completed or failed

        Parameters:
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
                        "updateApplicationVerificationRequired", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateApplicationVerificationRequired", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateApplicationVerificationRequired", filters, position
                )
            return func

        return decorator

    def on_updateApplicationRecaptchaVerificationRequired(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A request can't be completed unless reCAPTCHA verification is performed; for official mobile applications only\. The method setApplicationVerificationToken must be called once the verification is completed or failed

        Parameters:
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
                        "updateApplicationRecaptchaVerificationRequired",
                        func,
                        filters,
                        position,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func,
                    "updateApplicationRecaptchaVerificationRequired",
                    self,
                    position,
                )
            else:
                func._handler = Handler(
                    func,
                    "updateApplicationRecaptchaVerificationRequired",
                    filters,
                    position,
                )
            return func

        return decorator

    def on_updateCall(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""New call was created or information about a call was updated

        Parameters:
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
        r"""Information about a group call was updated

        Parameters:
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
        r"""Information about a group call participant was changed\. The updates are sent only after the group call is received through getGroupCall and only if the call is joined or being joined

        Parameters:
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
        r"""New call signaling data arrived

        Parameters:
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
        r"""Some privacy setting rules have been changed

        Parameters:
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
        r"""Number of unread messages in a chat list has changed\. This update is sent only if the message database is used

        Parameters:
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
        r"""Number of unread chats, i\.e\. with unread messages or marked as unread, has changed\. This update is sent only if the message database is used

        Parameters:
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
        r"""A story was changed

        Parameters:
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
        r"""A story became inaccessible

        Parameters:
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
        r"""A story has been successfully sent

        Parameters:
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
        r"""A story failed to send\. If the story sending is canceled, then updateStoryDeleted will be received instead of this update

        Parameters:
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
        r"""The list of active stories posted by a specific chat has changed

        Parameters:
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
        r"""Number of chats in a story list has changed

        Parameters:
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
        r"""Story stealth mode settings have changed

        Parameters:
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
        r"""An option changed its value

        Parameters:
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
        r"""A sticker set has changed

        Parameters:
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
        r"""The list of installed sticker sets was updated

        Parameters:
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
        r"""The list of trending sticker sets was updated or some of them were viewed

        Parameters:
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
        r"""The list of recently used stickers was updated

        Parameters:
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
        r"""The list of favorite stickers was updated

        Parameters:
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
        r"""The list of saved animations was updated

        Parameters:
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
        r"""The list of saved notification sounds was updated\. This update may not be sent until information about a notification sound was requested for the first time

        Parameters:
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

    def on_updateDefaultBackground(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The default background has changed

        Parameters:
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
                    self.add_handler("updateDefaultBackground", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateDefaultBackground", self, position)
            else:
                func._handler = Handler(
                    func, "updateDefaultBackground", filters, position
                )
            return func

        return decorator

    def on_updateChatThemes(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The list of available chat themes has changed

        Parameters:
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
        r"""The list of supported accent colors has changed

        Parameters:
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
        r"""The list of supported accent colors for user profiles has changed

        Parameters:
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
        r"""Some language pack strings have been updated

        Parameters:
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
        r"""The connection state has changed\. This update must be used only to show a human\-readable description of the connection state

        Parameters:
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

    def on_updateFreezeState(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The freeze state of the current user's account has changed

        Parameters:
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
                    self.add_handler("updateFreezeState", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateFreezeState", self, position)
            else:
                func._handler = Handler(func, "updateFreezeState", filters, position)
            return func

        return decorator

    def on_updateTermsOfService(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""New terms of service must be accepted by the user\. If the terms of service are declined, then the deleteAccount method must be called with the reason \"Decline ToS update\"

        Parameters:
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

    def on_updateUnconfirmedSession(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The first unconfirmed session has changed

        Parameters:
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
        r"""The list of bots added to attachment or side menu has changed

        Parameters:
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
        r"""A message was sent by an opened Web App, so the Web App needs to be closed

        Parameters:
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
        r"""The list of active emoji reactions has changed

        Parameters:
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

    def on_updateAvailableMessageEffects(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The list of available message effects has changed

        Parameters:
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
                        "updateAvailableMessageEffects", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateAvailableMessageEffects", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateAvailableMessageEffects", filters, position
                )
            return func

        return decorator

    def on_updateDefaultReactionType(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The type of default reaction has changed

        Parameters:
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

    def on_updateDefaultPaidReactionType(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The type of default paid reaction has changed

        Parameters:
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
                        "updateDefaultPaidReactionType", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateDefaultPaidReactionType", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateDefaultPaidReactionType", filters, position
                )
            return func

        return decorator

    def on_updateSavedMessagesTags(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Tags used in Saved Messages or a Saved Messages topic have changed

        Parameters:
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
                    self.add_handler("updateSavedMessagesTags", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateSavedMessagesTags", self, position)
            else:
                func._handler = Handler(
                    func, "updateSavedMessagesTags", filters, position
                )
            return func

        return decorator

    def on_updateActiveLiveLocationMessages(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The list of messages with active live location that need to be updated by the application has changed\. The list is persistent across application restarts only if the message database is used

        Parameters:
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
                        "updateActiveLiveLocationMessages", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateActiveLiveLocationMessages", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateActiveLiveLocationMessages", filters, position
                )
            return func

        return decorator

    def on_updateOwnedStarCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The number of Telegram Stars owned by the current user has changed

        Parameters:
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
                    self.add_handler("updateOwnedStarCount", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateOwnedStarCount", self, position)
            else:
                func._handler = Handler(func, "updateOwnedStarCount", filters, position)
            return func

        return decorator

    def on_updateChatRevenueAmount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The revenue earned from sponsored messages in a chat has changed\. If chat revenue screen is opened, then getChatRevenueTransactions may be called to fetch new transactions

        Parameters:
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
                    self.add_handler("updateChatRevenueAmount", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateChatRevenueAmount", self, position)
            else:
                func._handler = Handler(
                    func, "updateChatRevenueAmount", filters, position
                )
            return func

        return decorator

    def on_updateStarRevenueStatus(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The Telegram Star revenue earned by a bot or a chat has changed\. If Telegram Star transaction screen of the chat is opened, then getStarTransactions may be called to fetch new transactions

        Parameters:
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
                    self.add_handler("updateStarRevenueStatus", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateStarRevenueStatus", self, position)
            else:
                func._handler = Handler(
                    func, "updateStarRevenueStatus", filters, position
                )
            return func

        return decorator

    def on_updateSpeechRecognitionTrial(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The parameters of speech recognition without Telegram Premium subscription has changed

        Parameters:
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
        r"""The list of supported dice emojis has changed

        Parameters:
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
        r"""Some animated emoji message was clicked and a big animated sticker must be played if the message is visible on the screen\. chatActionWatchingAnimations with the text of the message needs to be sent if the sticker is played

        Parameters:
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
        r"""The parameters of animation search through getOption\(\"animation\_search\_bot\_username\"\) bot has changed

        Parameters:
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
        r"""The list of suggested to the user actions has changed

        Parameters:
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

    def on_updateSpeedLimitNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Download or upload file speed for the user was limited, but it can be restored by subscription to Telegram Premium\. The notification can be postponed until a being downloaded or uploaded file is visible to the user\. Use getOption\(\"premium\_download\_speedup\"\) or getOption\(\"premium\_upload\_speedup\"\) to get expected speedup after subscription to Telegram Premium

        Parameters:
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
                        "updateSpeedLimitNotification", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateSpeedLimitNotification", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateSpeedLimitNotification", filters, position
                )
            return func

        return decorator

    def on_updateContactCloseBirthdays(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""The list of contacts that had birthdays recently or will have birthday soon has changed

        Parameters:
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
                        "updateContactCloseBirthdays", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateContactCloseBirthdays", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateContactCloseBirthdays", filters, position
                )
            return func

        return decorator

    def on_updateAutosaveSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Autosave settings for some type of chats were updated

        Parameters:
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

    def on_updateBusinessConnection(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A business connection has changed; for bots only

        Parameters:
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
                        "updateBusinessConnection", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateBusinessConnection", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateBusinessConnection", filters, position
                )
            return func

        return decorator

    def on_updateNewBusinessMessage(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A new message was added to a business account; for bots only

        Parameters:
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
                        "updateNewBusinessMessage", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateNewBusinessMessage", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateNewBusinessMessage", filters, position
                )
            return func

        return decorator

    def on_updateBusinessMessageEdited(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A message in a business account was edited; for bots only

        Parameters:
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
                        "updateBusinessMessageEdited", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateBusinessMessageEdited", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateBusinessMessageEdited", filters, position
                )
            return func

        return decorator

    def on_updateBusinessMessagesDeleted(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Messages in a business account were deleted; for bots only

        Parameters:
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
                        "updateBusinessMessagesDeleted", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateBusinessMessagesDeleted", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateBusinessMessagesDeleted", filters, position
                )
            return func

        return decorator

    def on_updateNewInlineQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A new incoming inline query; for bots only

        Parameters:
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
        r"""The user has chosen a result of an inline query; for bots only

        Parameters:
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
        r"""A new incoming callback query; for bots only

        Parameters:
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
        r"""A new incoming callback query from a message sent via a bot; for bots only

        Parameters:
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

    def on_updateNewBusinessCallbackQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A new incoming callback query from a business message; for bots only

        Parameters:
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
                        "updateNewBusinessCallbackQuery", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updateNewBusinessCallbackQuery", self, position
                )
            else:
                func._handler = Handler(
                    func, "updateNewBusinessCallbackQuery", filters, position
                )
            return func

        return decorator

    def on_updateNewShippingQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""A new incoming shipping query; for bots only\. Only for invoices with flexible price

        Parameters:
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
        r"""A new incoming pre\-checkout query; for bots only\. Contains full information about a checkout

        Parameters:
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
        r"""A new incoming event; for bots only

        Parameters:
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
        r"""A new incoming query; for bots only

        Parameters:
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
        r"""A poll was updated; for bots only

        Parameters:
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
        r"""A user changed the answer to a poll; for bots only

        Parameters:
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
        r"""User rights changed in a chat; for bots only

        Parameters:
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
        r"""A user sent a join request to a chat; for bots only

        Parameters:
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
        r"""A chat boost has changed; for bots only

        Parameters:
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

    def on_updateMessageReaction(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""User changed its reactions on a message with public reactions; for bots only

        Parameters:
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
                    self.add_handler("updateMessageReaction", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateMessageReaction", self, position)
            else:
                func._handler = Handler(
                    func, "updateMessageReaction", filters, position
                )
            return func

        return decorator

    def on_updateMessageReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Reactions added to a message with anonymous reactions have changed; for bots only

        Parameters:
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
                    self.add_handler("updateMessageReactions", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "updateMessageReactions", self, position)
            else:
                func._handler = Handler(
                    func, "updateMessageReactions", filters, position
                )
            return func

        return decorator

    def on_updatePaidMediaPurchased(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Paid media were purchased by a user; for bots only

        Parameters:
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
                        "updatePaidMediaPurchased", func, filters, position
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func, "updatePaidMediaPurchased", self, position
                )
            else:
                func._handler = Handler(
                    func, "updatePaidMediaPurchased", filters, position
                )
            return func

        return decorator

    def on_updates(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        r"""Contains a list of updates

        Parameters:
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
