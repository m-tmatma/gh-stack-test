from cheer import cheer


def test_cheer_default():
    assert cheer() == "Go World! \\o/"


def test_cheer_custom_name():
    assert cheer("ada") == "Go ada! \\o/"


def test_cheer_blank_name_falls_back_to_default():
    assert cheer("   ") == "Go World! \\o/"
