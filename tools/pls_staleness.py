#!/usr/bin/env python3
"""Check whether PLS review evidence is stale relative to repository HEAD."""

from __future__ import annotations

import argparse
import fnmatch
import subprocess
import sys
from pathlib import Path

import yaml


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top-level YAML value must be a mapping")
    return data


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


def main() -> int:
    parser = argparse.ArgumentParser(description="Check PLS review freshness")
    parser.add_argument("metadata", type=Path, help="path to pls.yaml")
    parser.add_argument("review", type=Path, help="path to pls-review.yaml")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
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
        changed = [
            line.strip()
            for line in git(args.repo_root, "diff", "--name-only", f"{baseline}..HEAD").splitlines()
            if line.strip()
        ]

        baseline_yaml = git(args.repo_root, "show", f"{baseline}:pls.yaml")
        baseline_data = yaml.safe_load(baseline_yaml)
        if not isinstance(baseline_data, dict):
            raise ValueError("baseline pls.yaml is not a mapping")
    except (OSError, ValueError, KeyError, RuntimeError, yaml.YAMLError) as exc:
        print(f"PLS staleness: ERROR: {exc}", file=sys.stderr)
        return 2

    stale_reasons: list[str] = []

    if material_metadata(baseline_data) != material_metadata(current):
        stale_reasons.append("material PLS metadata changed since the reviewed commit")

    material_files = sorted(
        path
        for path in changed
        if any(fnmatch.fnmatch(path, pattern) for pattern in review_paths)
    )
    if material_files:
        stale_reasons.append(
            "pedagogically material files changed: " + ", ".join(material_files)
        )

    if stale_reasons:
        print(
            f"PLS staleness: STALE — review baseline {baseline} no longer covers HEAD",
            file=sys.stderr,
        )
        for reason in stale_reasons:
            print(f"  - {reason}", file=sys.stderr)
        return 1

    print(
        f"PLS staleness: CURRENT — review baseline {baseline} still covers declared pedagogical scope"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
