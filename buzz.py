"""Buzz helper built on top of config.py."""

from config import DEFAULT_NAME, BUZZ_SUFFIX


def buzz(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{BUZZ_SUFFIX}"
