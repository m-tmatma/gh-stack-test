"""Greeting helper built on top of config.py."""

from config import DEFAULT_NAME, GREETING_TEMPLATE


def greet(name: str = DEFAULT_NAME) -> str:
    return GREETING_TEMPLATE.format(name=name)
