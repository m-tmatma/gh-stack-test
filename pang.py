"""Standalone pang helper (no shared dependencies)."""

PANG_SUFFIX = " pang!"


def pang(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{PANG_SUFFIX}"
