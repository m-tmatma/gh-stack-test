from murmur import murmur


def test_murmur_default():
    assert murmur() == "(mumble) world..."


def test_murmur_custom_name():
    assert murmur("Ada") == "(mumble) ada..."


def test_murmur_blank_name_falls_back_to_default():
    assert murmur("   ") == "(mumble) world..."
