from shout import shout


def test_shout_default():
    assert shout() == "WORLD!!!"


def test_shout_custom_name():
    assert shout("ada") == "ADA!!!"


def test_shout_blank_name_falls_back_to_default():
    assert shout("   ") == "WORLD!!!"
