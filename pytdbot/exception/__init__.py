__all__ = ("StopHandlers", "AuthorizationError")


class StopHandlers(Exception):
    r"""An exception to stop handlers from execution"""

    pass


class AuthorizationError(Exception):
    r"""An exception for authorization errors"""

    pass


class WebAppDataInvalid(Exception):
    r"""An exception for invalid webapp data"""

    pass


class WebAppDataOutdated(Exception):
    r"""An exception for outdated webapp data"""

    pass


class WebAppDataMismatch(Exception):
    r"""An exception for mismatched webapp data"""

    pass
