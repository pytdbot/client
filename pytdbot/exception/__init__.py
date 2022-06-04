class StopHandlers(Exception):
    pass


class AuthorizationError(Exception):
    pass


__all__ = ["StopHandlers", "AuthorizationError"]
