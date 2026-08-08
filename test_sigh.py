from sigh import sigh


def test_sigh_default():
    assert sigh() == "World ..."


def test_sigh_custom_name():
    assert sigh("Ada") == "Ada ..."


def test_sigh_blank_name_falls_back_to_default():
    assert sigh("   ") == "World ..."
