__all__ = ("StopHandlers", "AuthorizationError")


class StopHandlers(Exception):
    r"""An exception to stop handlers from execution"""

    pass


class AuthorizationError(Exception):
    r"""An exception for authorization errors"""

    pass
