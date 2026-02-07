"""Command-line interface for Pyro-AI."""

from __future__ import annotations

import argparse

from pyro_ai.agent import PyroAI


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Pyro-AI CLI")
    parser.add_argument("--name", default="Pyro-AI", help="Name of the AI assistant.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    agent = PyroAI(name=args.name)
    print(agent.greet())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
