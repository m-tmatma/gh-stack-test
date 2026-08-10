from buzz import buzz


def test_buzz_default():
    assert buzz() == "World bzzz!"


def test_buzz_custom_name():
    assert buzz("Ada") == "Ada bzzz!"


def test_buzz_blank_name_falls_back_to_default():
    assert buzz("   ") == "World bzzz!"
