from whisper import whisper


def test_whisper_default():
    assert whisper() == "(psst) world"


def test_whisper_custom_name():
    assert whisper("Ada") == "(psst) ada"


def test_whisper_blank_name_falls_back_to_default():
    assert whisper("   ") == "(psst) world"
