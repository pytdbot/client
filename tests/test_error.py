from pytdbot import types
from pytdbot.utils import RETRY_AFTER_PREFEX


def test_error_is_falsy():
    err = types.Error(code=400, message="Bad Request")
    assert not err
    assert err.is_error
    assert err.code == 400
    assert err.message == "Bad Request"


def test_ok_is_truthy():
    ok = types.Ok()
    assert ok
    assert not ok.is_error
    assert ok.limited_seconds == 0


def test_limited_seconds_on_429():
    err = types.Error(code=429, message=f"{RETRY_AFTER_PREFEX}12")
    assert err.limited_seconds == 12


def test_limited_seconds_zero_when_not_429():
    err = types.Error(code=400, message=f"{RETRY_AFTER_PREFEX}12")
    assert err.limited_seconds == 0
