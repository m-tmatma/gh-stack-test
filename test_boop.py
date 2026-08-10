from boop import boop


def test_boop_default():
    assert boop("") == "World boop!"


def test_boop_name():
    assert boop("Heidi") == "Heidi boop!"
