"""Whisper helper built on top of config.py."""

from config import DEFAULT_NAME, WHISPER_PREFIX


def whisper(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"{WHISPER_PREFIX}{name.lower()}"
