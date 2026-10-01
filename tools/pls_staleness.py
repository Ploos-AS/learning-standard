#!/usr/bin/env python3
"""Check whether PLS review evidence is stale relative to repository HEAD."""

from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
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


def validate_document(data: dict, schema: dict, label: str) -> None:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.absolute_path))
    if errors:
        detail = []
        for error in errors:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            detail.append(f"{location}: {error.message}")
        raise ValueError(f"{label} is invalid: " + "; ".join(detail))


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def git_is_ancestor(repo: Path, older: str, newer: str) -> bool:
    result = subprocess.run(
        ["git", "-C", str(repo), "merge-base", "--is-ancestor", older, newer],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode == 0:
        return True
    if result.returncode == 1:
        return False
    raise RuntimeError(result.stderr.strip() or "git merge-base failed")


def changed_files(repo: Path, older: str, newer: str) -> list[str]:
    return [
        line.strip()
        for line in git(repo, "diff", "--name-only", f"{older}..{newer}").splitlines()
        if line.strip()
    ]


def material_metadata(data: dict) -> dict:
    return {
        "specification": data["pls"]["specification"],
        "entry_level": data["pls"]["entry_level"],
        "exit_level": data["pls"]["exit_level"],
        "resource": {
            "language": data["resource"]["language"],
            "scope": data["resource"]["scope"],
            "prerequisites": data["resource"]["prerequisites"],
            "learning_outcomes": data["resource"]["learning_outcomes"],
            "review_paths": data["resource"].get("review_paths", []),
        },
    }


def matching_material_files(paths: list[str], patterns: list[str]) -> list[str]:
    return sorted(
        path for path in paths if any(fnmatch.fnmatch(path, pattern) for pattern in patterns)
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Check PLS review freshness")
    parser.add_argument("metadata", type=Path, help="path to pls.yaml")
    parser.add_argument("review", type=Path, help="path to pls-review.yaml")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument(
        "--attestation",
        type=Path,
        help="optional pls-attestation.yaml for a documented non-material change assessment",
    )
    parser.add_argument(
        "--attestation-schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schema" / "pls-attestation.schema.json",
        help="path to PLS attestation JSON Schema",
    )
    args = parser.parse_args()

    try:
        current = load_yaml(args.metadata)
        status = current["pls"]["status"]
    except (OSError, ValueError, KeyError, yaml.YAMLError) as exc:
        print(f"PLS staleness: ERROR: {exc}", file=sys.stderr)
        return 2

    if status not in {"reviewed", "compliant"}:
        print(f"PLS staleness: SKIP — status {status} does not require freshness checking")
        return 0

    try:
        review = load_yaml(args.review)
        baseline = review["review"]["resource_commit"]
        review_paths = current["resource"].get("review_paths", [])
        if not review_paths:
            raise ValueError("resource.review_paths is required for reviewed/compliant status")

        git(args.repo_root, "cat-file", "-e", f"{baseline}^{{commit}}")
        baseline_yaml = git(args.repo_root, "show", f"{baseline}:pls.yaml")
        baseline_data = yaml.safe_load(baseline_yaml)
        if not isinstance(baseline_data, dict):
            raise ValueError("baseline pls.yaml is not a mapping")
    except (OSError, ValueError, KeyError, RuntimeError, yaml.YAMLError) as exc:
        print(f"PLS staleness: ERROR: {exc}", file=sys.stderr)
        return 2

    if material_metadata(baseline_data) != material_metadata(current):
        print(
            f"PLS staleness: STALE — material PLS metadata changed since review baseline {baseline}",
            file=sys.stderr,
        )
        print("  - non-material attestations cannot override material metadata changes", file=sys.stderr)
        return 1

    try:
        material_files = matching_material_files(
            changed_files(args.repo_root, baseline, "HEAD"), review_paths
        )
    except RuntimeError as exc:
        print(f"PLS staleness: ERROR: {exc}", file=sys.stderr)
        return 2

    if not material_files:
        print(
            f"PLS staleness: CURRENT — review baseline {baseline} still covers declared pedagogical scope"
        )
        return 0

    if args.attestation is None:
        print(
            f"PLS staleness: STALE — review baseline {baseline} no longer covers HEAD",
            file=sys.stderr,
        )
        print("  - pedagogically scoped files changed: " + ", ".join(material_files), file=sys.stderr)
        print("  - provide a new review or a valid non-material attestation", file=sys.stderr)
        return 1

    try:
        attestation = load_yaml(args.attestation)
        attestation_schema = load_schema(args.attestation_schema)
        validate_document(attestation, attestation_schema, "attestation")

        att = attestation["attestation"]
        if att["specification"] != current["pls"]["specification"]:
            raise ValueError("attestation specification does not match pls.yaml")
        if att["review_commit"].lower() != baseline.lower():
            raise ValueError("attestation review_commit does not match review baseline")

        through = att["through_commit"]
        git(args.repo_root, "cat-file", "-e", f"{through}^{{commit}}")
        if not git_is_ancestor(args.repo_root, baseline, through):
            raise ValueError("attestation through_commit is not descended from review baseline")
        if not git_is_ancestor(args.repo_root, through, "HEAD"):
            raise ValueError("attestation through_commit is not an ancestor of HEAD")

        covered_material = matching_material_files(
            changed_files(args.repo_root, baseline, through), review_paths
        )
        declared_paths = sorted(attestation["assessment"]["changed_paths"])
        if declared_paths != covered_material:
            raise ValueError(
                "attestation changed_paths must exactly match pedagogically scoped files "
                "changed between review_commit and through_commit"
            )

        later_material = matching_material_files(
            changed_files(args.repo_root, through, "HEAD"), review_paths
        )
        if later_material:
            raise ValueError(
                "new pedagogically scoped changes exist after attested through_commit: "
                + ", ".join(later_material)
            )
    except (OSError, ValueError, KeyError, RuntimeError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"PLS staleness: STALE — attestation does not preserve freshness", file=sys.stderr)
        print(f"  - {exc}", file=sys.stderr)
        return 1

    print(
        "PLS staleness: CURRENT BY ATTESTATION — "
        f"review baseline {baseline}, non-material changes attested through {through} by "
        f"{attestation['attestant']['name']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
