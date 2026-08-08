"""Giggle helper built on top of config.py."""

from config import DEFAULT_NAME, GIGGLE_SUFFIX


def giggle(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{GIGGLE_SUFFIX}"
