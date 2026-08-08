"""Sigh helper built on top of config.py."""

from config import DEFAULT_NAME, SIGH_SUFFIX


def sigh(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{SIGH_SUFFIX}"
