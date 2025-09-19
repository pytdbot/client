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
        timeout: float = None,
    ) -> Callable:
        r"""The user authorization state has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateAuthorizationState",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateAuthorizationState",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateAuthorizationState",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewMessage(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new message was received; can also be an outgoing message

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewMessage",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewMessage",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewMessage",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageSendAcknowledged(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A request to send a message has reached the Telegram server\. This doesn't mean that the message will be sent successfully\. This update is sent only if the option \"use\_quick\_ack\" is set to true\. This update may be sent multiple times for the same message

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageSendAcknowledged",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageSendAcknowledged",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageSendAcknowledged",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageSendSucceeded(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A message has been successfully sent

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageSendSucceeded",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageSendSucceeded",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageSendSucceeded",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageSendFailed(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A message failed to send\. Be aware that some messages being sent can be irrecoverably deleted, in which case updateDeleteMessages will be received instead of this update

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageSendFailed",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageSendFailed",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageSendFailed",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageContent(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The message content has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageContent",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageContent",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageContent",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageEdited(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A message was edited\. Changes in the message content will come in a separate updateMessageContent

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageEdited",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageEdited",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageEdited",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageIsPinned(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The message pinned state was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageIsPinned",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageIsPinned",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageIsPinned",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageInteractionInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The information about interactions with a message has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageInteractionInfo",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageInteractionInfo",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageInteractionInfo",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageContentOpened(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The message content was opened\. Updates voice note messages to \"listened\", video note messages to \"viewed\" and starts the self\-destruct timer

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageContentOpened",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageContentOpened",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageContentOpened",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageMentionRead(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A message with an unread mention was read

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageMentionRead",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageMentionRead",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageMentionRead",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageUnreadReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of unread reactions added to a message was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageUnreadReactions",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageUnreadReactions",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageUnreadReactions",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageFactCheck(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A fact\-check added to a message was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageFactCheck",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageFactCheck",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageFactCheck",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageSuggestedPostInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Information about suggested post of a message was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageSuggestedPostInfo",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageSuggestedPostInfo",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageSuggestedPostInfo",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageLiveLocationViewed(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A message with a live location was viewed\. When the update is received, the application is expected to update the live location

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageLiveLocationViewed",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageLiveLocationViewed",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageLiveLocationViewed",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateVideoPublished(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""An automatically scheduled message with video has been successfully sent after conversion

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateVideoPublished",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateVideoPublished",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateVideoPublished",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewChat(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new chat has been loaded/created\. This update is guaranteed to come before the chat identifier is returned to the application\. The chat field changes will be reported through separate updates

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewChat",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewChat",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewChat",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatTitle(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The title of a chat was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatTitle",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatTitle",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatTitle",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatPhoto(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat photo was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatPhoto",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatPhoto",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatPhoto",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatAccentColors(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Chat accent colors have changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatAccentColors",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatAccentColors",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatAccentColors",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatPermissions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Chat permissions were changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatPermissions",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatPermissions",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatPermissions",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatLastMessage(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The last message of a chat was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatLastMessage",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatLastMessage",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatLastMessage",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatPosition(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The position of a chat in a chat list has changed\. An updateChatLastMessage or updateChatDraftMessage update might be sent instead of the update

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatPosition",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatPosition",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatPosition",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatAddedToList(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat was added to a chat list

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatAddedToList",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatAddedToList",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatAddedToList",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatRemovedFromList(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat was removed from a chat list

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatRemovedFromList",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatRemovedFromList",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatRemovedFromList",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatReadInbox(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Incoming messages were read or the number of unread messages has been changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatReadInbox",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatReadInbox",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatReadInbox",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatReadOutbox(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Outgoing messages were read

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatReadOutbox",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatReadOutbox",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatReadOutbox",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatActionBar(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The chat action bar was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatActionBar",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatActionBar",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatActionBar",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatBusinessBotManageBar(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The bar for managing business bot was changed in a chat

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatBusinessBotManageBar",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatBusinessBotManageBar",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatBusinessBotManageBar",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatAvailableReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The chat available reactions were changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatAvailableReactions",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatAvailableReactions",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatAvailableReactions",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatDraftMessage(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat draft has changed\. Be aware that the update may come in the currently opened chat but with old content of the draft\. If the user has changed the content of the draft, this update mustn't be applied

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatDraftMessage",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatDraftMessage",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatDraftMessage",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatEmojiStatus(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Chat emoji status has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatEmojiStatus",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatEmojiStatus",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatEmojiStatus",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatMessageSender(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The message sender that is selected to send messages in a chat has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatMessageSender",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatMessageSender",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatMessageSender",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatMessageAutoDeleteTime(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The message auto\-delete or self\-destruct timer setting for a chat was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatMessageAutoDeleteTime",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatMessageAutoDeleteTime",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatMessageAutoDeleteTime",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatNotificationSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Notification settings for a chat were changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatNotificationSettings",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatNotificationSettings",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatNotificationSettings",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatPendingJoinRequests(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The chat pending join requests were changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatPendingJoinRequests",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatPendingJoinRequests",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatPendingJoinRequests",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatReplyMarkup(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The default chat reply markup was changed\. Can occur because new messages with reply markup were received or because an old reply markup was hidden by the user

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatReplyMarkup",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatReplyMarkup",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatReplyMarkup",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatBackground(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The chat background was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatBackground",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatBackground",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatBackground",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatTheme(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The chat theme was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatTheme",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatTheme",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatTheme",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatUnreadMentionCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The chat unread\_mention\_count has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatUnreadMentionCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatUnreadMentionCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatUnreadMentionCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatUnreadReactionCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The chat unread\_reaction\_count has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatUnreadReactionCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatUnreadReactionCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatUnreadReactionCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatVideoChat(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat video chat state has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatVideoChat",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatVideoChat",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatVideoChat",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatDefaultDisableNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The value of the default disable\_notification parameter, used when a message is sent to the chat, was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatDefaultDisableNotification",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatDefaultDisableNotification",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatDefaultDisableNotification",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatHasProtectedContent(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat content was allowed or restricted for saving

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatHasProtectedContent",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatHasProtectedContent",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatHasProtectedContent",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatIsTranslatable(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Translation of chat messages was enabled or disabled

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatIsTranslatable",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatIsTranslatable",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatIsTranslatable",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatIsMarkedAsUnread(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat was marked as unread or was read

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatIsMarkedAsUnread",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatIsMarkedAsUnread",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatIsMarkedAsUnread",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatViewAsTopics(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat default appearance has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatViewAsTopics",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatViewAsTopics",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatViewAsTopics",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatBlockList(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat was blocked or unblocked

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatBlockList",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatBlockList",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatBlockList",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatHasScheduledMessages(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat's has\_scheduled\_messages field has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatHasScheduledMessages",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatHasScheduledMessages",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatHasScheduledMessages",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatFolders(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of chat folders or a chat folder has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatFolders",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatFolders",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatFolders",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatOnlineMemberCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The number of online group members has changed\. This update with non\-zero number of online group members is sent only for currently opened chats\. There is no guarantee that it is sent just after the number of online users has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatOnlineMemberCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatOnlineMemberCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatOnlineMemberCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSavedMessagesTopic(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Basic information about a Saved Messages topic has changed\. This update is guaranteed to come before the topic identifier is returned to the application

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSavedMessagesTopic",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedMessagesTopic",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedMessagesTopic",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSavedMessagesTopicCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Number of Saved Messages topics has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSavedMessagesTopicCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedMessagesTopicCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedMessagesTopicCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateDirectMessagesChatTopic(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Basic information about a topic in a channel direct messages chat administered by the current user has changed\. This update is guaranteed to come before the topic identifier is returned to the application

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateDirectMessagesChatTopic",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateDirectMessagesChatTopic",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateDirectMessagesChatTopic",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateTopicMessageCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Number of messages in a topic has changed; for Saved Messages and channel direct messages chat topics only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateTopicMessageCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateTopicMessageCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateTopicMessageCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateQuickReplyShortcut(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Basic information about a quick reply shortcut has changed\. This update is guaranteed to come before the quick shortcut name is returned to the application

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateQuickReplyShortcut",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateQuickReplyShortcut",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateQuickReplyShortcut",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateQuickReplyShortcutDeleted(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A quick reply shortcut and all its messages were deleted

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateQuickReplyShortcutDeleted",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateQuickReplyShortcutDeleted",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateQuickReplyShortcutDeleted",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateQuickReplyShortcuts(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of quick reply shortcuts has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateQuickReplyShortcuts",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateQuickReplyShortcuts",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateQuickReplyShortcuts",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateQuickReplyShortcutMessages(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of quick reply shortcut messages has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateQuickReplyShortcutMessages",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateQuickReplyShortcutMessages",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateQuickReplyShortcutMessages",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateForumTopicInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Basic information about a topic in a forum chat was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateForumTopicInfo",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateForumTopicInfo",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateForumTopicInfo",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateForumTopic(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Information about a topic in a forum chat was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateForumTopic",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateForumTopic",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateForumTopic",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateScopeNotificationSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Notification settings for some type of chats were updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateScopeNotificationSettings",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateScopeNotificationSettings",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateScopeNotificationSettings",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateReactionNotificationSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Notification settings for reactions were updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateReactionNotificationSettings",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateReactionNotificationSettings",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateReactionNotificationSettings",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A notification was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNotification",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNotification",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNotification",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNotificationGroup(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A list of active notifications in a notification group has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNotificationGroup",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNotificationGroup",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNotificationGroup",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateActiveNotifications(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Contains active notifications that were shown on previous application launches\. This update is sent only if the message database is used\. In that case it comes once before any updateNotification and updateNotificationGroup update

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateActiveNotifications",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateActiveNotifications",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateActiveNotifications",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateHavePendingNotifications(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Describes whether there are some pending notification updates\. Can be used to prevent application from killing, while there are some pending notifications

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateHavePendingNotifications",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateHavePendingNotifications",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateHavePendingNotifications",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateDeleteMessages(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some messages were deleted

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateDeleteMessages",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateDeleteMessages",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateDeleteMessages",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatAction(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A message sender activity in the chat has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatAction",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatAction",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatAction",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateUserStatus(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The user went online or offline

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateUserStatus",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateUserStatus",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateUserStatus",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateUser(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some data of a user has changed\. This update is guaranteed to come before the user identifier is returned to the application

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateUser",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateUser",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateUser",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateBasicGroup(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some data of a basic group has changed\. This update is guaranteed to come before the basic group identifier is returned to the application

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateBasicGroup",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateBasicGroup",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateBasicGroup",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSupergroup(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some data of a supergroup or a channel has changed\. This update is guaranteed to come before the supergroup identifier is returned to the application

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSupergroup",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSupergroup",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSupergroup",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSecretChat(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some data of a secret chat has changed\. This update is guaranteed to come before the secret chat identifier is returned to the application

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSecretChat",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSecretChat",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSecretChat",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateUserFullInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some data in userFullInfo has been changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateUserFullInfo",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateUserFullInfo",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateUserFullInfo",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateBasicGroupFullInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some data in basicGroupFullInfo has been changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateBasicGroupFullInfo",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateBasicGroupFullInfo",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateBasicGroupFullInfo",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSupergroupFullInfo(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some data in supergroupFullInfo has been changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSupergroupFullInfo",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSupergroupFullInfo",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSupergroupFullInfo",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateServiceNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A service notification from the server was received\. Upon receiving this the application must show a popup with the content of the notification

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateServiceNotification",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateServiceNotification",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateServiceNotification",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFile(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Information about a file was updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFile",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFile",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFile",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFileGenerationStart(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The file generation process needs to be started by the application\. Use setFileGenerationProgress and finishFileGeneration to generate the file

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFileGenerationStart",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFileGenerationStart",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFileGenerationStart",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFileGenerationStop(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""File generation is no longer needed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFileGenerationStop",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFileGenerationStop",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFileGenerationStop",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFileDownloads(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The state of the file download list has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFileDownloads",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFileDownloads",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFileDownloads",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFileAddedToDownloads(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A file was added to the file download list\. This update is sent only after file download list is loaded for the first time

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFileAddedToDownloads",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFileAddedToDownloads",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFileAddedToDownloads",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFileDownload(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A file download was changed\. This update is sent only after file download list is loaded for the first time

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFileDownload",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFileDownload",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFileDownload",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFileRemovedFromDownloads(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A file was removed from the file download list\. This update is sent only after file download list is loaded for the first time

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFileRemovedFromDownloads",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFileRemovedFromDownloads",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFileRemovedFromDownloads",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateApplicationVerificationRequired(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A request can't be completed unless application verification is performed; for official mobile applications only\. The method setApplicationVerificationToken must be called once the verification is completed or failed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateApplicationVerificationRequired",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateApplicationVerificationRequired",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateApplicationVerificationRequired",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateApplicationRecaptchaVerificationRequired(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A request can't be completed unless reCAPTCHA verification is performed; for official mobile applications only\. The method setApplicationVerificationToken must be called once the verification is completed or failed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateApplicationRecaptchaVerificationRequired",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateApplicationRecaptchaVerificationRequired",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateApplicationRecaptchaVerificationRequired",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateCall(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""New call was created or information about a call was updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateCall",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateCall",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateCall",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateGroupCall(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Information about a group call was updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateGroupCall",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateGroupCall",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateGroupCall",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateGroupCallParticipant(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Information about a group call participant was changed\. The updates are sent only after the group call is received through getGroupCall and only if the call is joined or being joined

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateGroupCallParticipant",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateGroupCallParticipant",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateGroupCallParticipant",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateGroupCallParticipants(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of group call participants that can send and receive encrypted call data has changed; for group calls not bound to a chat only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateGroupCallParticipants",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateGroupCallParticipants",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateGroupCallParticipants",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateGroupCallVerificationState(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The verification state of an encrypted group call has changed; for group calls not bound to a chat only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateGroupCallVerificationState",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateGroupCallVerificationState",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateGroupCallVerificationState",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewCallSignalingData(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""New call signaling data arrived

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewCallSignalingData",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewCallSignalingData",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewCallSignalingData",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateUserPrivacySettingRules(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some privacy setting rules have been changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateUserPrivacySettingRules",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateUserPrivacySettingRules",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateUserPrivacySettingRules",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateUnreadMessageCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Number of unread messages in a chat list has changed\. This update is sent only if the message database is used

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateUnreadMessageCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateUnreadMessageCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateUnreadMessageCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateUnreadChatCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Number of unread chats, i\.e\. with unread messages or marked as unread, has changed\. This update is sent only if the message database is used

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateUnreadChatCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateUnreadChatCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateUnreadChatCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateStory(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A story was changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateStory",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateStory",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateStory",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateStoryDeleted(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A story became inaccessible

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateStoryDeleted",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryDeleted",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryDeleted",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateStoryPostSucceeded(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A story has been successfully posted

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateStoryPostSucceeded",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryPostSucceeded",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryPostSucceeded",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateStoryPostFailed(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A story failed to post\. If the story posting is canceled, then updateStoryDeleted will be received instead of this update

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateStoryPostFailed",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryPostFailed",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryPostFailed",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatActiveStories(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of active stories posted by a specific chat has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatActiveStories",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatActiveStories",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatActiveStories",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateStoryListChatCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Number of chats in a story list has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateStoryListChatCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryListChatCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryListChatCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateStoryStealthMode(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Story stealth mode settings have changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateStoryStealthMode",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryStealthMode",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateStoryStealthMode",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateOption(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""An option changed its value

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateOption",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateOption",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateOption",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateStickerSet(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A sticker set has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateStickerSet",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateStickerSet",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateStickerSet",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateInstalledStickerSets(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of installed sticker sets was updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateInstalledStickerSets",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateInstalledStickerSets",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateInstalledStickerSets",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateTrendingStickerSets(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of trending sticker sets was updated or some of them were viewed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateTrendingStickerSets",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateTrendingStickerSets",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateTrendingStickerSets",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateRecentStickers(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of recently used stickers was updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateRecentStickers",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateRecentStickers",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateRecentStickers",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFavoriteStickers(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of favorite stickers was updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFavoriteStickers",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFavoriteStickers",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFavoriteStickers",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSavedAnimations(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of saved animations was updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSavedAnimations",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedAnimations",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedAnimations",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSavedNotificationSounds(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of saved notification sounds was updated\. This update may not be sent until information about a notification sound was requested for the first time

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSavedNotificationSounds",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedNotificationSounds",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedNotificationSounds",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateDefaultBackground(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The default background has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateDefaultBackground",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateDefaultBackground",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateDefaultBackground",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateEmojiChatThemes(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of available emoji chat themes has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateEmojiChatThemes",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateEmojiChatThemes",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateEmojiChatThemes",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateAccentColors(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of supported accent colors has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateAccentColors",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateAccentColors",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateAccentColors",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateProfileAccentColors(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of supported accent colors for user profiles has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateProfileAccentColors",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateProfileAccentColors",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateProfileAccentColors",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateLanguagePackStrings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some language pack strings have been updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateLanguagePackStrings",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateLanguagePackStrings",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateLanguagePackStrings",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateConnectionState(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The connection state has changed\. This update must be used only to show a human\-readable description of the connection state

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateConnectionState",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateConnectionState",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateConnectionState",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateFreezeState(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The freeze state of the current user's account has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateFreezeState",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateFreezeState",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateFreezeState",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateAgeVerificationParameters(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The parameters for age verification of the current user's account has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateAgeVerificationParameters",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateAgeVerificationParameters",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateAgeVerificationParameters",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateTermsOfService(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""New terms of service must be accepted by the user\. If the terms of service are declined, then the deleteAccount method must be called with the reason \"Decline ToS update\"

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateTermsOfService",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateTermsOfService",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateTermsOfService",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateUnconfirmedSession(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The first unconfirmed session has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateUnconfirmedSession",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateUnconfirmedSession",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateUnconfirmedSession",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateAttachmentMenuBots(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of bots added to attachment or side menu has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateAttachmentMenuBots",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateAttachmentMenuBots",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateAttachmentMenuBots",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateWebAppMessageSent(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A message was sent by an opened Web App, so the Web App needs to be closed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateWebAppMessageSent",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateWebAppMessageSent",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateWebAppMessageSent",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateActiveEmojiReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of active emoji reactions has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateActiveEmojiReactions",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateActiveEmojiReactions",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateActiveEmojiReactions",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateAvailableMessageEffects(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of available message effects has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateAvailableMessageEffects",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateAvailableMessageEffects",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateAvailableMessageEffects",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateDefaultReactionType(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The type of default reaction has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateDefaultReactionType",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateDefaultReactionType",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateDefaultReactionType",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateDefaultPaidReactionType(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The type of default paid reaction has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateDefaultPaidReactionType",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateDefaultPaidReactionType",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateDefaultPaidReactionType",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSavedMessagesTags(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Tags used in Saved Messages or a Saved Messages topic have changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSavedMessagesTags",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedMessagesTags",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSavedMessagesTags",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateActiveLiveLocationMessages(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of messages with active live location that need to be updated by the application has changed\. The list is persistent across application restarts only if the message database is used

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateActiveLiveLocationMessages",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateActiveLiveLocationMessages",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateActiveLiveLocationMessages",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateOwnedStarCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The number of Telegram Stars owned by the current user has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateOwnedStarCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateOwnedStarCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateOwnedStarCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateOwnedTonCount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The number of Toncoins owned by the current user has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateOwnedTonCount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateOwnedTonCount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateOwnedTonCount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatRevenueAmount(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The revenue earned from sponsored messages in a chat has changed\. If chat revenue screen is opened, then getChatRevenueTransactions may be called to fetch new transactions

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatRevenueAmount",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatRevenueAmount",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatRevenueAmount",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateStarRevenueStatus(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The Telegram Star revenue earned by a user or a chat has changed\. If Telegram Star transaction screen of the chat is opened, then getStarTransactions may be called to fetch new transactions

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateStarRevenueStatus",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateStarRevenueStatus",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateStarRevenueStatus",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateTonRevenueStatus(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The Toncoin revenue earned by the current user has changed\. If Toncoin transaction screen of the chat is opened, then getTonTransactions may be called to fetch new transactions

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateTonRevenueStatus",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateTonRevenueStatus",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateTonRevenueStatus",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSpeechRecognitionTrial(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The parameters of speech recognition without Telegram Premium subscription has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSpeechRecognitionTrial",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSpeechRecognitionTrial",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSpeechRecognitionTrial",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateDiceEmojis(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of supported dice emojis has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateDiceEmojis",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateDiceEmojis",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateDiceEmojis",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateAnimatedEmojiMessageClicked(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Some animated emoji message was clicked and a big animated sticker must be played if the message is visible on the screen\. chatActionWatchingAnimations with the text of the message needs to be sent if the sticker is played

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateAnimatedEmojiMessageClicked",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateAnimatedEmojiMessageClicked",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateAnimatedEmojiMessageClicked",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateAnimationSearchParameters(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The parameters of animation search through getOption\(\"animation\_search\_bot\_username\"\) bot has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateAnimationSearchParameters",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateAnimationSearchParameters",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateAnimationSearchParameters",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSuggestedActions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of suggested to the user actions has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSuggestedActions",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSuggestedActions",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSuggestedActions",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateSpeedLimitNotification(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Download or upload file speed for the user was limited, but it can be restored by subscription to Telegram Premium\. The notification can be postponed until a being downloaded or uploaded file is visible to the user\. Use getOption\(\"premium\_download\_speedup\"\) or getOption\(\"premium\_upload\_speedup\"\) to get expected speedup after subscription to Telegram Premium

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateSpeedLimitNotification",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateSpeedLimitNotification",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateSpeedLimitNotification",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateContactCloseBirthdays(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The list of contacts that had birthdays recently or will have birthday soon has changed

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateContactCloseBirthdays",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateContactCloseBirthdays",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateContactCloseBirthdays",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateAutosaveSettings(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Autosave settings for some type of chats were updated

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateAutosaveSettings",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateAutosaveSettings",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateAutosaveSettings",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateBusinessConnection(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A business connection has changed; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateBusinessConnection",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateBusinessConnection",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateBusinessConnection",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewBusinessMessage(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new message was added to a business account; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewBusinessMessage",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewBusinessMessage",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewBusinessMessage",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateBusinessMessageEdited(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A message in a business account was edited; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateBusinessMessageEdited",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateBusinessMessageEdited",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateBusinessMessageEdited",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateBusinessMessagesDeleted(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Messages in a business account were deleted; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateBusinessMessagesDeleted",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateBusinessMessagesDeleted",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateBusinessMessagesDeleted",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewInlineQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new incoming inline query; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewInlineQuery",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewInlineQuery",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewInlineQuery",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewChosenInlineResult(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""The user has chosen a result of an inline query; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewChosenInlineResult",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewChosenInlineResult",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewChosenInlineResult",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewCallbackQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new incoming callback query; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewCallbackQuery",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewCallbackQuery",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewCallbackQuery",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewInlineCallbackQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new incoming callback query from a message sent via a bot; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewInlineCallbackQuery",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewInlineCallbackQuery",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewInlineCallbackQuery",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewBusinessCallbackQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new incoming callback query from a business message; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewBusinessCallbackQuery",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewBusinessCallbackQuery",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewBusinessCallbackQuery",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewShippingQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new incoming shipping query; for bots only\. Only for invoices with flexible price

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewShippingQuery",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewShippingQuery",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewShippingQuery",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewPreCheckoutQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new incoming pre\-checkout query; for bots only\. Contains full information about a checkout

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewPreCheckoutQuery",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewPreCheckoutQuery",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewPreCheckoutQuery",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewCustomEvent(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new incoming event; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewCustomEvent",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewCustomEvent",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewCustomEvent",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewCustomQuery(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A new incoming query; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewCustomQuery",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewCustomQuery",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewCustomQuery",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updatePoll(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A poll was updated; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updatePoll",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updatePoll",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updatePoll",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updatePollAnswer(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A user changed the answer to a poll; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updatePollAnswer",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updatePollAnswer",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updatePollAnswer",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatMember(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""User rights changed in a chat; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatMember",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatMember",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatMember",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateNewChatJoinRequest(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A user sent a join request to a chat; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateNewChatJoinRequest",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateNewChatJoinRequest",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateNewChatJoinRequest",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateChatBoost(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""A chat boost has changed; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateChatBoost",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateChatBoost",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateChatBoost",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageReaction(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""User changed its reactions on a message with public reactions; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageReaction",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageReaction",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageReaction",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updateMessageReactions(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Reactions added to a message with anonymous reactions have changed; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updateMessageReactions",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageReactions",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updateMessageReactions",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updatePaidMediaPurchased(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Paid media were purchased by a user; for bots only

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updatePaidMediaPurchased",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updatePaidMediaPurchased",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updatePaidMediaPurchased",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator

    def on_updates(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r"""Contains a list of updates

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        """

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(
                        update_type="updates",
                        func=func,
                        filters=filters,
                        position=position,
                        inner_object=False,
                        timeout=timeout,
                    )
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(
                    func=func,
                    update_type="updates",
                    filter=self,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            else:
                func._handler = Handler(
                    func=func,
                    update_type="updates",
                    filter=filters,
                    position=position,
                    inner_object=False,
                    timeout=timeout,
                )
            return func

        return decorator
