#!/usr/bin/env python3
"""Validate Ploos Learning Standard metadata."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("top-level YAML value must be a mapping")
    return data


def load_schema(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PLS metadata")
    parser.add_argument("metadata", type=Path, help="path to pls.yaml")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schema" / "pls.schema.json",
        help="path to PLS JSON Schema",
    )
    args = parser.parse_args()

    try:
        data = load_yaml(args.metadata)
        schema = load_schema(args.schema)
    except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"PLS lint: ERROR: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.absolute_path))

    if errors:
        print("PLS lint: metadata is invalid", file=sys.stderr)
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            print(f"  - {location}: {error.message}", file=sys.stderr)
        return 1

    entry = data["pls"]["entry_level"]
    exit_ = data["pls"]["exit_level"]
    if exit_ < entry:
        print(
            f"PLS lint: ERROR: exit_level ({exit_}) must not be below entry_level ({entry})",
            file=sys.stderr,
        )
        return 1

    print(
        f"PLS lint: OK — specification {data['pls']['specification']}, "
        f"levels {entry} -> {exit_}, status {data['pls']['status']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
