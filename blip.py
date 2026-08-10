"""Standalone blip helper (no shared dependencies)."""

BLIP_SUFFIX = " blip!"


def blip(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{BLIP_SUFFIX}"
