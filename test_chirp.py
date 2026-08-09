from chirp import chirp


def test_chirp_default():
    assert chirp() == "World chirp chirp!"


def test_chirp_custom_name():
    assert chirp("Ada") == "Ada chirp chirp!"


def test_chirp_blank_name_falls_back_to_default():
    assert chirp("   ") == "World chirp chirp!"
