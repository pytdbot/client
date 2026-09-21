import pytest
from pytdbot import utils


def test_json_dumps_loads_roundtrip():
    payload = {"a": 1, "b": [True, None]}
    encoded = utils.json_dumps(payload)
    assert utils.json_loads(encoded) == payload

    as_bytes = utils.json_dumps(payload, encode=True)
    assert isinstance(as_bytes, bytes)
    assert utils.json_loads(as_bytes) == payload


def test_callback_data_roundtrip():
    raw = utils.callback_data("ok", {"id": 1})
    assert isinstance(raw, bytes)
    loaded = utils.load_callback_data(raw)
    assert loaded.action == "ok"
    assert loaded.data == {"id": 1}


def test_load_callback_data_invalid_returns_empty():
    empty = utils.load_callback_data(b"not-json")
    assert empty.action == ""
    assert empty.data is None
    assert utils.empty_callback_data.action == ""


def test_callback_data_too_large():
    with pytest.raises(ValueError, match="less than 64 bytes"):
        utils.callback_data("x" * 70)
