"""Yowl helper built on top of config.py."""

from config import DEFAULT_NAME, YOWL_SUFFIX


def yowl(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{YOWL_SUFFIX}"
