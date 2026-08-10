from beep import beep


def test_beep_default():
    assert beep("") == "World beep!"


def test_beep_name():
    assert beep("Grace") == "Grace beep!"
