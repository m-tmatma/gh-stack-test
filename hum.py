"""Hum helper built on top of config.py."""

from config import DEFAULT_NAME, HUM_SUFFIX


def hum(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{HUM_SUFFIX}"
