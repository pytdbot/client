import hashlib
import hmac
import time
from urllib.parse import urlencode

import pytest
from pytdbot import utils
from pytdbot.exception import (
    WebAppDataInvalid,
    WebAppDataMismatch,
    WebAppDataOutdated,
)


def _signed_init_data(secret, extra=None, auth_date=None):
    data = {"auth_date": str(auth_date if auth_date is not None else int(time.time()))}
    if extra:
        data.update(extra)
    check = "\n".join(f"{k}={data[k]}" for k in sorted(data))
    digest = hmac.new(secret, check.encode(), hashlib.sha256).hexdigest()
    return urlencode({**data, "hash": digest})


def test_create_webapp_secret_key():
    key = utils.create_webapp_secret_key("123:abc")
    assert isinstance(key, bytes)
    assert len(key) == 32
    assert key == utils.create_webapp_secret_key("123:abc")
    assert key != utils.create_webapp_secret_key("other")


def test_parse_webapp_data_valid():
    secret = utils.create_webapp_secret_key("123:abc")
    init = _signed_init_data(secret, extra={"query_id": "q1"})
    parsed = utils.parse_webapp_data(secret, init)
    assert parsed["query_id"] == "q1"
    assert "hash" not in parsed


def test_parse_webapp_data_invalid():
    secret = utils.create_webapp_secret_key("123:abc")
    with pytest.raises(WebAppDataInvalid):
        utils.parse_webapp_data(secret, "foo=bar")


def test_parse_webapp_data_mismatch():
    secret = utils.create_webapp_secret_key("123:abc")
    init = _signed_init_data(secret, extra={"query_id": "q1"})
    other = utils.create_webapp_secret_key("other")
    with pytest.raises(WebAppDataMismatch):
        utils.parse_webapp_data(other, init)


def test_parse_webapp_data_outdated():
    secret = utils.create_webapp_secret_key("123:abc")
    init = _signed_init_data(
        secret, extra={"query_id": "q1"}, auth_date=int(time.time()) - 120
    )
    with pytest.raises(WebAppDataOutdated):
        utils.parse_webapp_data(secret, init, max_data_age=60)
