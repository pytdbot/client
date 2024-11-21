import hashlib
import hmac
import time

from urllib.parse import parse_qs

from ..exception import WebAppDataInvalid, WebAppDataOutdated, WebAppDataMismatch

_webapp_secret_key = b"WebAppData"


def create_webapp_secret_key(bot_token: str) -> bytes:
    r"""Create a secret key for Web App data validation

    \Parameters:
        bot_token (``str``):
            Bot token

    """

    return hmac.new(
        key=_webapp_secret_key,
        msg=bot_token.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).digest()


def parse_webapp_data(
    secret_key: bytes, init_data: str, max_data_age: int = 60
) -> dict:
    r"""Parse and validate init data received from Web App

    \Parameters:
        secret_key (``bytes``):
            Secret key for Web App data validation; can be created using :func:`pytdbot.utils.create_webapp_secret_key`

        init_data (``str``):
            Init data received from Web App

        max_data_age (``int``, *optional*):
            Maximum age of init data in seconds. Default is ``60`` seconds

    Returns:
        ``dict``: Parsed data

    Raises:
        :class:`pytdbot.exception.WebAppDataInvalid`
        :class:`pytdbot.exception.WebAppDataOutdated`
        :class:`pytdbot.exception.WebAppDataMismatch`
    """

    assert isinstance(secret_key, bytes), "secret_key must be bytes"
    assert isinstance(init_data, str), "init_data must be a string"
    assert isinstance(max_data_age, int), "max_data_age must be an int"

    # In Python 3.8.7 or earlier, parse_qs treats ';' as query separator in addition to '&'
    # Which may cause issues with the hash validation
    data = parse_qs(init_data)

    data = {k: v[0] for k, v in data.items()}

    if "hash" not in data or "auth_date" not in data:
        raise WebAppDataInvalid("Missing hash or auth_date")

    if int(data["auth_date"]) < int(time.time() - max_data_age):
        raise WebAppDataOutdated

    received_hash = data.pop("hash")

    sorted_keys = sorted(data.keys())

    data_check_string = "\n".join([f"{key}={data[key]}" for key in sorted_keys])

    expected_hash = hmac.new(
        key=secret_key, msg=data_check_string.encode("utf-8"), digestmod=hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected_hash, received_hash):
        raise WebAppDataMismatch("Hash mismatch")

    return data
