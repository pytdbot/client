from typing import Callable


class Filter:
    r"""Filter class

    A filter is a function that takes a request and returns a boolean. If the returned value is ``True`` then the handler will be called.
    See :func:`~pytdbot.filters.create` for more information
    """

    def __init__(self, func: Callable):
        self.func = func
        if not callable(func):
            raise TypeError("func must be callable")

    def __str__(self) -> str:
        return f"Filter(func={self.func})"

    def __repr__(self) -> str:
        return str(self)


def create(func: Callable) -> Filter:
    r"""A factory to create a filter

    Example:

        .. code-block:: python

            from pytdbot import filters, Client

            client = Client(...)

            # Create a filter by a decorator
            @filters.create
            async def filter_photo(_, event) -> bool:
                if event.content_type == "messagePhoto":
                    return True
                return False

            # Or by a function

            filter_photo = filters.create(filter_photo)

            # Or by lambda

            filter_photo = filters.create(lambda _, event: event.content_type == "messagePhoto")

            @client.on_updateNewMessage(filters=filter_photo)
            async def photo_handler(c,update):
                await update.reply_text('I got a photo!')

            client.run()

    Parameters:
        func (``Callable``):
            The filter function

    """

    return Filter(func)
