from greeting import greet


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_custom_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_blank_name_falls_back_to_default():
    assert greet("   ") == "Hello, World!"
