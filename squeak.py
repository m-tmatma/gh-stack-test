"""Squeak helper built on top of config.py."""

from config import DEFAULT_NAME, SQUEAK_SUFFIX


def squeak(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{SQUEAK_SUFFIX}"
