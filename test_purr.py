from purr import purr


def test_purr_default():
    assert purr() == "World purrr~"


def test_purr_custom_name():
    assert purr("Ada") == "Ada purrr~"


def test_purr_blank_name_falls_back_to_default():
    assert purr("   ") == "World purrr~"
