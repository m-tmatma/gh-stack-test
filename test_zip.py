from zip import zip_


def test_zip_default():
    assert zip_("") == "World zip!"


def test_zip_name():
    assert zip_("Eve") == "Eve zip!"
