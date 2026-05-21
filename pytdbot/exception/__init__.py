__all__ = ("StopHandlers", "AuthorizationError", "WebAppDataError")


class StopHandlers(Exception):
    r"""An exception to stop handlers from execution"""

    pass


class AuthorizationError(Exception):
    r"""An exception for authorization errors"""

    def __init__(self, message: str, code: int = 0) -> None:
        self.code = code
        super().__init__(message)


class WebAppDataError(Exception):
    r"""Base exception for webapp data errors"""

    pass


class WebAppDataInvalid(WebAppDataError):
    r"""An exception for invalid webapp data"""

    pass


class WebAppDataOutdated(WebAppDataError):
    r"""An exception for outdated webapp data"""

    pass


class WebAppDataMismatch(WebAppDataError):
    r"""An exception for mismatched webapp data"""

    pass
