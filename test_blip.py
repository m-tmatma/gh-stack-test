from blip import blip


def test_blip_default():
    assert blip("") == "World blip!"


def test_blip_name():
    assert blip("Ivan") == "Ivan blip!"
