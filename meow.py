"""Meow helper built on top of config.py."""

from config import DEFAULT_NAME, MEOW_SUFFIX


def meow(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{MEOW_SUFFIX}"
