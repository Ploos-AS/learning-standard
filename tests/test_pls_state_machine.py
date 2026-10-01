#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LINT = ROOT / "tools" / "pls_lint.py"
STALE = ROOT / "tools" / "pls_staleness.py"
PLS_SCHEMA = ROOT / "schema" / "pls.schema.json"
REVIEW_SCHEMA = ROOT / "schema" / "pls-review.schema.json"
ATTEST_SCHEMA = ROOT / "schema" / "pls-attestation.schema.json"


def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def base_metadata(status: str = "aligned") -> dict:
    return {
        "pls": {"specification": "0.1", "entry_level": 0, "exit_level": 3, "status": status},
        "resource": {
            "title": "State Machine Fixture",
            "type": "course",
            "language": ["en"],
            "scope": "Fixture scope.",
            "prerequisites": [],
            "learning_outcomes": ["Explain the fixture concept."],
            "review_paths": ["course/**", "exercises/**"],
        },
    }


def review_data(commit: str, result: str = "reviewed") -> dict:
    return {
        "review": {
            "specification": "0.1",
            "resource_commit": commit,
            "date": "2026-10-01",
            "scope": "Fixture review.",
            "result": result,
        },
        "reviewer": {
            "name": "Independent Reviewer",
            "role": "Pedagogical reviewer",
            "independent_from_primary_author": True,
        },
        "findings": {"blocking": 0, "major": 0, "minor": 0, "note": 0},
        "evidence": {"review_record": "PLS-REVIEW.md", "checklist": "PLS-COMPLIANCE.md", "additional": []},
    }


def attestation_data(review_commit: str, through_commit: str, changed_paths: list[str]) -> dict:
    return {
        "attestation": {
            "specification": "0.1",
            "review_commit": review_commit,
            "through_commit": through_commit,
            "date": "2026-10-01",
        },
        "attestant": {"name": "Maintainer", "role": "Maintainer"},
        "assessment": {
            "non_material": True,
            "reason": "Spelling-only correction that does not change terminology, outcomes, examples, exercises, or learning meaning.",
            "changed_paths": changed_paths,
            "evidence": [],
        },
    }


class TempRepo:
    def __init__(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name)
        run("git", "init", "-q", cwd=self.path)
        run("git", "config", "user.name", "PLS Tests", cwd=self.path)
        run("git", "config", "user.email", "pls-tests@example.invalid", cwd=self.path)

    def close(self) -> None:
        self.tmp.cleanup()

    def commit(self, message: str) -> str:
        run("git", "add", "-A", cwd=self.path)
        result = run("git", "commit", "-q", "-m", message, cwd=self.path)
        if result.returncode != 0:
            raise AssertionError(result.stderr)
        return run("git", "rev-parse", "HEAD", cwd=self.path).stdout.strip()


class PLSStateMachineTests(unittest.TestCase):
    def lint(self, repo: Path, review: bool = False) -> subprocess.CompletedProcess[str]:
        args = ["python", str(LINT), "pls.yaml", "--schema", str(PLS_SCHEMA), "--review-schema", str(REVIEW_SCHEMA)]
        if review:
            args += ["--review", "pls-review.yaml"]
        return run(*args, cwd=repo)

    def stale(self, repo: Path, attestation: bool = False) -> subprocess.CompletedProcess[str]:
        args = ["python", str(STALE), "pls.yaml", "pls-review.yaml", "--repo-root", ".", "--attestation-schema", str(ATTEST_SCHEMA)]
        if attestation:
            args += ["--attestation", "pls-attestation.yaml"]
        return run(*args, cwd=repo)

    def make_reviewed_repo(self, result: str = "reviewed") -> tuple[TempRepo, str]:
        repo = TempRepo()
        write_yaml(repo.path / "pls.yaml", base_metadata("aligned"))
        (repo.path / "course").mkdir()
        (repo.path / "course" / "01.md").write_text("# Lesson\nOriginal meaning.\n", encoding="utf-8")
        baseline = repo.commit("baseline educational state")
        data = base_metadata("reviewed" if result == "reviewed" else "compliant")
        write_yaml(repo.path / "pls.yaml", data)
        write_yaml(repo.path / "pls-review.yaml", review_data(baseline, result))
        (repo.path / "PLS-REVIEW.md").write_text("Reviewed.\n", encoding="utf-8")
        (repo.path / "PLS-COMPLIANCE.md").write_text("Checklist complete.\n", encoding="utf-8")
        repo.commit("record review")
        return repo, baseline

    def test_adopting_and_aligned_validate_without_review(self) -> None:
        for status in ("adopting", "aligned"):
            with self.subTest(status=status):
                repo = TempRepo()
                try:
                    write_yaml(repo.path / "pls.yaml", base_metadata(status))
                    result = self.lint(repo.path)
                    self.assertEqual(result.returncode, 0, result.stderr)
                finally:
                    repo.close()

    def test_reviewed_requires_review_evidence(self) -> None:
        repo = TempRepo()
        try:
            write_yaml(repo.path / "pls.yaml", base_metadata("reviewed"))
            result = self.lint(repo.path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("requires --review", result.stderr)
        finally:
            repo.close()

    def test_compliant_requires_compliant_review_result(self) -> None:
        repo = TempRepo()
        try:
            write_yaml(repo.path / "pls.yaml", base_metadata("compliant"))
            write_yaml(repo.path / "pls-review.yaml", review_data("0123456789abcdef0123456789abcdef01234567", "reviewed"))
            result = self.lint(repo.path, review=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("review.result=compliant", result.stderr)
        finally:
            repo.close()

    def test_reviewed_current_when_only_infrastructure_changes(self) -> None:
        repo, _ = self.make_reviewed_repo()
        try:
            (repo.path / ".github" / "workflows").mkdir(parents=True)
            (repo.path / ".github" / "workflows" / "ci.yml").write_text("name: CI\n", encoding="utf-8")
            repo.commit("infrastructure only")
            result = self.stale(repo.path)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("CURRENT", result.stdout)
        finally:
            repo.close()

    def test_review_becomes_stale_after_material_file_change(self) -> None:
        repo, _ = self.make_reviewed_repo()
        try:
            (repo.path / "course" / "01.md").write_text("# Lesson\nChanged learning meaning.\n", encoding="utf-8")
            repo.commit("change lesson meaning")
            result = self.stale(repo.path)
            self.assertEqual(result.returncode, 1)
            self.assertIn("STALE", result.stderr)
            self.assertIn("course/01.md", result.stderr)
        finally:
            repo.close()

    def test_valid_non_material_attestation_preserves_freshness(self) -> None:
        repo, baseline = self.make_reviewed_repo()
        try:
            (repo.path / "course" / "01.md").write_text("# Lesson\nOriginal meaning!\n", encoding="utf-8")
            through = repo.commit("punctuation correction")
            write_yaml(repo.path / "pls-attestation.yaml", attestation_data(baseline, through, ["course/01.md"]))
            repo.commit("record non-material attestation")
            result = self.stale(repo.path, attestation=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("CURRENT BY ATTESTATION", result.stdout)
        finally:
            repo.close()

    def test_attestation_fails_when_changed_paths_are_incomplete(self) -> None:
        repo, baseline = self.make_reviewed_repo()
        try:
            (repo.path / "course" / "01.md").write_text("# Lesson\nOriginal meaning!\n", encoding="utf-8")
            (repo.path / "exercises").mkdir()
            (repo.path / "exercises" / "01.md").write_text("Question.\n", encoding="utf-8")
            through = repo.commit("two scoped changes")
            write_yaml(repo.path / "pls-attestation.yaml", attestation_data(baseline, through, ["course/01.md"]))
            repo.commit("incomplete attestation")
            result = self.stale(repo.path, attestation=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("exactly match", result.stderr)
        finally:
            repo.close()

    def test_attestation_cannot_override_material_metadata_change(self) -> None:
        repo, baseline = self.make_reviewed_repo()
        try:
            data = yaml.safe_load((repo.path / "pls.yaml").read_text(encoding="utf-8"))
            data["resource"]["learning_outcomes"].append("New outcome.")
            write_yaml(repo.path / "pls.yaml", data)
            (repo.path / "course" / "01.md").write_text("# Lesson\nOriginal meaning!\n", encoding="utf-8")
            through = repo.commit("change outcomes and lesson")
            write_yaml(repo.path / "pls-attestation.yaml", attestation_data(baseline, through, ["course/01.md"]))
            repo.commit("attempt invalid attestation")
            result = self.stale(repo.path, attestation=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("material PLS metadata changed", result.stderr)
        finally:
            repo.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
