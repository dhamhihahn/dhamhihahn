"""Core agent implementation for Pyro-AI."""

from __future__ import annotations

from pathlib import Path

from pyro_ai.vision import read_image_pixels, read_video_frames, Pixel


class PyroAI:
    """A minimal AI assistant scaffold."""

    def __init__(self, name: str = "Pyro-AI") -> None:
        self.name = name

    def greet(self) -> str:
        """Return a short greeting."""
        return f"{self.name} online. Ready to assist."

    def load_image_pixels(self, path: str | Path) -> list[list[Pixel]]:
        """Load image pixels for downstream analysis."""
        return read_image_pixels(path)

    def load_video_frames(
        self, path: str | Path, limit: int | None = None
    ) -> list[list[list[Pixel]]]:
        """Load video frames as RGB pixels for downstream analysis."""
        return read_video_frames(path, limit=limit)
