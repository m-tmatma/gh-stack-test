"""Standalone pong helper (no shared dependencies)."""

PONG_SUFFIX = " pong!"


def pong(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{PONG_SUFFIX}"
