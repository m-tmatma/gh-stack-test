"""Purr helper built on top of config.py."""

from config import DEFAULT_NAME, PURR_SUFFIX


def purr(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{PURR_SUFFIX}"
