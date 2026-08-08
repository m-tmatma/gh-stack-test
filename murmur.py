"""Murmur helper built on top of config.py."""

from config import DEFAULT_NAME, MURMUR_PREFIX


def murmur(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{MURMUR_PREFIX}{name.lower()}..."
