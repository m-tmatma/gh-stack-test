"""Shout helper built on top of config.py."""

from config import DEFAULT_NAME, SHOUT_SUFFIX


def shout(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name.upper()}{SHOUT_SUFFIX}"
