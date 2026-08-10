"""Standalone ping helper (no shared dependencies)."""

PING_SUFFIX = " ping!"


def ping(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{PING_SUFFIX}"
