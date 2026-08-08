from meow import meow


def test_meow_default():
    assert meow() == "World meow!"


def test_meow_custom_name():
    assert meow("Ada") == "Ada meow!"


def test_meow_blank_name_falls_back_to_default():
    assert meow("   ") == "World meow!"
