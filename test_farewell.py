from farewell import farewell


def test_farewell_default():
    assert farewell() == "Goodbye, World!"


def test_farewell_custom_name():
    assert farewell("Ada") == "Goodbye, Ada!"


def test_farewell_blank_name_falls_back_to_default():
    assert farewell("   ") == "Goodbye, World!"
