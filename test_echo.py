from echo import echo


def test_echo_default():
    assert echo() == "World World"


def test_echo_custom_name():
    assert echo("Ada") == "Ada Ada"


def test_echo_blank_name_falls_back_to_default():
    assert echo("   ") == "World World"
