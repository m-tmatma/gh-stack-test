from yowl import yowl


def test_yowl_default():
    assert yowl() == "World yoooowl!"


def test_yowl_custom_name():
    assert yowl("Ada") == "Ada yoooowl!"


def test_yowl_blank_name_falls_back_to_default():
    assert yowl("   ") == "World yoooowl!"
