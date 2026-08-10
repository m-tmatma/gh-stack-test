from vroom import vroom


def test_vroom_default():
    assert vroom("") == "World vroom!"


def test_vroom_name():
    assert vroom("Frank") == "Frank vroom!"
