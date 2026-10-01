#!/usr/bin/env python3
"""Validate Ploos Learning Standard metadata and review evidence."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top-level YAML value must be a mapping")
    return data


def load_schema(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_document(data: dict, schema: dict, label: str) -> bool:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.absolute_path))
    if not errors:
        return True

    print(f"PLS lint: {label} is invalid", file=sys.stderr)
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        print(f"  - {location}: {error.message}", file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PLS metadata")
    parser.add_argument("metadata", type=Path, help="path to pls.yaml")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schema" / "pls.schema.json",
        help="path to PLS JSON Schema",
    )
    parser.add_argument(
        "--review",
        type=Path,
        help="path to pls-review.yaml; mandatory for reviewed/compliant status",
    )
    parser.add_argument(
        "--review-schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schema" / "pls-review.schema.json",
        help="path to PLS review JSON Schema",
    )
    args = parser.parse_args()

    try:
        data = load_yaml(args.metadata)
        schema = load_schema(args.schema)
    except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"PLS lint: ERROR: {exc}", file=sys.stderr)
        return 2

    if not validate_document(data, schema, "metadata"):
        return 1

    entry = data["pls"]["entry_level"]
    exit_ = data["pls"]["exit_level"]
    status = data["pls"]["status"]

    if exit_ < entry:
        print(
            f"PLS lint: ERROR: exit_level ({exit_}) must not be below entry_level ({entry})",
            file=sys.stderr,
        )
        return 1

    review_required = status in {"reviewed", "compliant"}
    if review_required and args.review is None:
        print(
            f"PLS lint: ERROR: status {status} requires --review pls-review.yaml",
            file=sys.stderr,
        )
        return 1

    if args.review is not None:
        try:
            review = load_yaml(args.review)
            review_schema = load_schema(args.review_schema)
        except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
            print(f"PLS lint: ERROR: {exc}", file=sys.stderr)
            return 2

        if not validate_document(review, review_schema, "review evidence"):
            return 1

        review_spec = review["review"]["specification"]
        if review_spec != data["pls"]["specification"]:
            print(
                "PLS lint: ERROR: review specification does not match pls.yaml",
                file=sys.stderr,
            )
            return 1

        review_result = review["review"]["result"]
        if status == "compliant" and review_result != "compliant":
            print(
                "PLS lint: ERROR: compliant status requires review.result=compliant",
                file=sys.stderr,
            )
            return 1

        if status == "reviewed" and review_result not in {"reviewed", "compliant"}:
            print(
                "PLS lint: ERROR: reviewed status requires completed review evidence",
                file=sys.stderr,
            )
            return 1

    print(
        f"PLS lint: OK — specification {data['pls']['specification']}, "
        f"levels {entry} -> {exit_}, status {status}"
    )
    if args.review is not None:
        print(
            f"PLS lint: review evidence OK — result {review['review']['result']}, "
            f"reviewer {review['reviewer']['name']}, commit {review['review']['resource_commit']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
