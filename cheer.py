"""Cheer helper built on top of config.py."""

from config import DEFAULT_NAME, CHEER_SUFFIX


def cheer(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"Go {name}!{CHEER_SUFFIX}"
