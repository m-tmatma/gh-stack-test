from pang import pang


def test_pang_default():
    assert pang("") == "World pang!"


def test_pang_name():
    assert pang("Carol") == "Carol pang!"
