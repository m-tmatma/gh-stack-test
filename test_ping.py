from ping import ping


def test_ping_default():
    assert ping("") == "World ping!"


def test_ping_name():
    assert ping("Alice") == "Alice ping!"
