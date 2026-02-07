# Pyro-AI

Pyro-AI is a starter scaffold for an AI assistant project. It includes a simple
Python package, a minimal configuration, and a tiny CLI entry point that can be
expanded into a full agent.

## Quick start

```bash
python -m pyro_ai --name "Pyro-AI"
```

## Vision capabilities

Pyro-AI includes helpers for reading raw pixels from images and video frames:

```python
from pyro_ai import PyroAI

agent = PyroAI()
image_pixels = agent.load_image_pixels("path/to/image.png")
video_frames = agent.load_video_frames("path/to/video.mp4", limit=5)
```

## Next steps

- Add prompts, tools, or model integrations in `pyro_ai/agent.py`.
- Expand the CLI in `pyro_ai/cli.py` for additional commands.
