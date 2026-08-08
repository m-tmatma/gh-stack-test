from chuckle import chuckle


def test_chuckle_default():
    assert chuckle() == "World heh heh"


def test_chuckle_custom_name():
    assert chuckle("Ada") == "Ada heh heh"


def test_chuckle_blank_name_falls_back_to_default():
    assert chuckle("   ") == "World heh heh"
