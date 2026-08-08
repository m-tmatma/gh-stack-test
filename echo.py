"""Echo helper built on top of config.py."""

from config import DEFAULT_NAME, ECHO_REPEAT


def echo(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return " ".join([name] * ECHO_REPEAT)
