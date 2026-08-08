"""Snort helper built on top of config.py."""

from config import DEFAULT_NAME, SNORT_SUFFIX


def snort(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{name}{SNORT_SUFFIX}"
