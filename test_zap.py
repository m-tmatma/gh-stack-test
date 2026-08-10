from zap import zap


def test_zap_default():
    assert zap("") == "World zap!"


def test_zap_name():
    assert zap("Dave") == "Dave zap!"
