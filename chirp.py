"""Chirp helper built on top of config.py."""

from config import CHIRP_SUFFIX, DEFAULT_NAME


def chirp(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{CHIRP_SUFFIX}"
