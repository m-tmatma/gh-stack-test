"""Standalone beep helper (no shared dependencies)."""

BEEP_SUFFIX = " beep!"


def beep(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{BEEP_SUFFIX}"
