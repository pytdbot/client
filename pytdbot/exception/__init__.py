__all__ = ("StopHandlers", "AuthorizationError")


class StopHandlers(Exception):
    """An exception to stop handlers from execution"""

    pass


class AuthorizationError(Exception):
    """An exception for authorization errors"""

    pass
