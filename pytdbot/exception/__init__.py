__all__ = ["StopHandlers", "AuthorizationError"]


class StopHandlers(Exception):
    pass


class AuthorizationError(Exception):
    pass
