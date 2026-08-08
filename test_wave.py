from wave import wave


def test_wave_default():
    assert wave() == "Hi World! o/"


def test_wave_custom_name():
    assert wave("ada") == "Hi ada! o/"


def test_wave_blank_name_falls_back_to_default():
    assert wave("   ") == "Hi World! o/"
