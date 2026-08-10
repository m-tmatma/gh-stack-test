"""Standalone zap helper (no shared dependencies)."""

ZAP_SUFFIX = " zap!"


def zap(name: str = "World") -> str:
    name = name.strip() or "World"
    return f"{name}{ZAP_SUFFIX}"
