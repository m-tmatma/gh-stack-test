from bark import bark


def test_bark_default():
    assert bark() == "World woof!"


def test_bark_custom_name():
    assert bark("Ada") == "Ada woof!"


def test_bark_blank_name_falls_back_to_default():
    assert bark("   ") == "World woof!"
