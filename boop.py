"""Standalone boop helper (no shared dependencies)."""

BOOP_SUFFIX = " boop!"


def boop(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{BOOP_SUFFIX}"
