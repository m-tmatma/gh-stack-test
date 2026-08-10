"""Chime helper built on top of config.py."""

from config import DEFAULT_NAME, CHIME_SUFFIX


def chime(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{CHIME_SUFFIX}"
