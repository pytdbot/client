from pytdbot import utils


def test_to_camel_case_class():
    assert utils.to_camel_case("error") == "Error"
    assert utils.to_camel_case("messageSender.user") == "MessageSenderUser"
    assert utils.to_camel_case("") == ""


def test_to_camel_case_not_class():
    assert utils.to_camel_case("sendMessage", is_class=False) == "sendMessage"
    assert utils.to_camel_case("foo.bar", is_class=False) == "fooBar"


def test_create_extra_id():
    a = utils.create_extra_id(4)
    b = utils.create_extra_id(4)
    assert isinstance(a, str)
    assert len(a) == 8
    assert a != b


def test_get_bot_id_from_token():
    assert utils.get_bot_id_from_token("123456:AA-secret") == "123456"
    assert utils.get_bot_id_from_token("nocolon") == ""
    assert utils.get_bot_id_from_token("x" * 81) == ""


def test_get_retry_after_time():
    assert utils.get_retry_after_time(f"{utils.RETRY_AFTER_PREFEX}9") == 9
    assert utils.get_retry_after_time("not a flood") == 0
    assert utils.get_retry_after_time(None) == 0
