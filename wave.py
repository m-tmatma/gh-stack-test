"""Wave helper built on top of config.py."""

from config import DEFAULT_NAME, WAVE_SUFFIX


def wave(name: str = DEFAULT_NAME) -> str:
    name = name.strip() or DEFAULT_NAME
    return f"Hi {name}!{WAVE_SUFFIX}"
