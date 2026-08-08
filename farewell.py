"""Farewell helper built on top of config.py."""

from config import DEFAULT_NAME, FAREWELL_TEMPLATE


def farewell(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return FAREWELL_TEMPLATE.format(name=name)
