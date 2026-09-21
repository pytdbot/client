from pytdbot import types, utils


def test_deepdiff_added_removed_changed():
    left = {"a": 1, "b": 2, "c": 3}
    right = {"a": 1, "b": 9, "d": 4}
    logs = utils.deepdiff(left, right)
    assert "b changed to 9" in logs
    assert "c removed" in logs
    assert "d changed to 4" in logs


def test_deepdiff_equal_objects():
    err = types.Error(code=1, message="x")
    assert utils.deepdiff(err, err) == []


def test_deepdiff_non_dict():
    assert utils.deepdiff(1, 1) == []
    assert utils.deepdiff(1, 2) == ["changed to 2"]
