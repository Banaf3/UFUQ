"""Repository-local entry point for the non-packaged oracle project."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from ufuq_astronomy_reference import (  # noqa: E402
    build_environment_manifest,
    canonical_bytes,
    generate_fixture,
    sha256_bytes,
)


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as source:
        value = json.load(source)
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must contain a JSON object.")
    return value


def _write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def _environment(output: Path) -> None:
    _write(output, canonical_bytes(build_environment_manifest(PROJECT_ROOT)))


def _fixture(
    input_path: Path,
    environment_path: Path,
    output_path: Path,
    hash_path: Path,
) -> None:
    document = generate_fixture(
        _read_json(input_path), _read_json(environment_path)
    )
    output = canonical_bytes(document)
    _write(output_path, output)
    _write(hash_path, (sha256_bytes(output) + "\n").encode("ascii"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate UFUQ synthetic-only astronomy oracle evidence."
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    environment = subcommands.add_parser("environment")
    environment.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "environment-manifest.json",
    )

    fixture = subcommands.add_parser("fixture")
    fixture.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "fixtures" / "synthetic-input.v1.json",
    )
    fixture.add_argument(
        "--environment",
        type=Path,
        default=PROJECT_ROOT / "environment-manifest.json",
    )
    fixture.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "fixtures" / "synthetic-output.v1.json",
    )
    fixture.add_argument(
        "--hash-output",
        type=Path,
        default=PROJECT_ROOT / "fixtures" / "synthetic-output.v1.sha256",
    )

    args = parser.parse_args()
    if args.command == "environment":
        _environment(args.output)
    else:
        _fixture(args.input, args.environment, args.output, args.hash_output)


if __name__ == "__main__":
    main()
