from snort import snort


def test_snort_default():
    assert snort() == "World pfft"


def test_snort_custom_name():
    assert snort("Ada") == "Ada pfft"


def test_snort_blank_name_falls_back_to_default():
    assert snort("   ") == "World pfft"
