from hum import hum


def test_hum_default():
    assert hum() == "World mmm~"


def test_hum_custom_name():
    assert hum("Ada") == "Ada mmm~"


def test_hum_blank_name_falls_back_to_default():
    assert hum("   ") == "World mmm~"
