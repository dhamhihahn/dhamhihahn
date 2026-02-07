"""Vision utilities for Pyro-AI."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import imageio.v3 as iio
from PIL import Image

Pixel = tuple[int, int, int]


def read_image_pixels(path: str | Path) -> list[list[Pixel]]:
    """Read an image and return a 2D list of RGB pixels."""
    image = Image.open(path).convert("RGB")
    width, height = image.size
    pixels = list(image.getdata())
    return [pixels[row_start : row_start + width] for row_start in range(0, width * height, width)]


def read_video_frames(path: str | Path, limit: int | None = None) -> list[list[list[Pixel]]]:
    """Read video frames and return a list of frames as RGB pixels."""
    frames: list[list[list[Pixel]]] = []
    for index, frame in enumerate(_iter_video_frames(path)):
        if limit is not None and index >= limit:
            break
        frames.append(frame)
    return frames


def _iter_video_frames(path: str | Path) -> Iterable[list[list[Pixel]]]:
    for frame in iio.imiter(path):
        image = Image.fromarray(frame).convert("RGB")
        width, height = image.size
        pixels = list(image.getdata())
        yield [
            pixels[row_start : row_start + width]
            for row_start in range(0, width * height, width)
        ]
