"""Standalone zip helper (no shared dependencies)."""

ZIP_SUFFIX = " zip!"


def zip_(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{ZIP_SUFFIX}"
