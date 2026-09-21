from pytdbot import filters


def test_create_true_and_false():
    photo = filters.create(lambda _, event: event == "photo")
    assert photo.func(None, "photo") is True
    assert photo.func(None, "text") is False


def test_create_as_decorator():
    @filters.create
    def only_one(_, event):
        return event == 1

    assert only_one.func(None, 1) is True
    assert only_one.func(None, 2) is False
