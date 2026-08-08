"""Bark helper built on top of config.py."""

from config import DEFAULT_NAME, BARK_SUFFIX


def bark(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{BARK_SUFFIX}"
