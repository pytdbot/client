from pytdbot import types, utils


def test_error_dict_roundtrip():
    err = types.Error(code=404, message="Not Found")
    as_dict = utils.obj_to_dict(err)
    assert as_dict["@type"] == "error"
    assert as_dict["code"] == 404

    as_json = utils.obj_to_json(err)
    assert '"error"' in as_json

    restored = utils.dict_to_obj(
        {"@type": "error", "code": 404, "message": "Not Found"}
    )
    assert isinstance(restored, types.Error)
    assert restored.code == 404
    assert restored.message == "Not Found"


def test_dict_to_obj_nested_list():
    restored = utils.dict_to_obj(
        [
            {"@type": "error", "code": 1, "message": "a"},
            {"@type": "ok"},
        ]
    )
    assert isinstance(restored[0], types.Error)
    assert isinstance(restored[1], types.Ok)
