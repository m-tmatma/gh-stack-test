from pong import pong


def test_pong_default():
    assert pong("") == "World pong!"


def test_pong_name():
    assert pong("Bob") == "Bob pong!"
