"""Standalone vroom helper (no shared dependencies)."""

VROOM_SUFFIX = " vroom!"


def vroom(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{VROOM_SUFFIX}"
