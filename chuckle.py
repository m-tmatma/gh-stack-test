"""Chuckle helper built on top of config.py."""

from config import DEFAULT_NAME, CHUCKLE_SUFFIX


def chuckle(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name} heh{CHUCKLE_SUFFIX}"
