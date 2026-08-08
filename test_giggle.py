from giggle import giggle


def test_giggle_default():
    assert giggle() == "World hehe~"


def test_giggle_custom_name():
    assert giggle("Ada") == "Ada hehe~"


def test_giggle_blank_name_falls_back_to_default():
    assert giggle("   ") == "World hehe~"
