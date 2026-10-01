# Ploos Learning Standard (PLS)

**Start intuitively. End rigorously. Leave no hidden steps.**

Ploos Learning Standard (PLS) is the shared pedagogical standard for Ploos educational books, courses, and learning projects.

PLS is not about making subjects shallow. It is about making difficult subjects accessible without removing the real terminology, methods, notation, or rigor.

A PLS-compliant learning resource should:

- state prerequisites explicitly;
- introduce intuition before formalism when pedagogically appropriate;
- explain every new symbol, operator, abbreviation, and term;
- avoid hidden reasoning steps;
- move from concrete examples toward abstraction and formal definitions;
- teach why as well as how;
- use authentic subject terminology;
- combine representations when useful: text, diagrams, mathematics, code, tables, experiments;
- require active learning rather than passive reading;
- make limitations of intuitive models explicit;
- address common misconceptions;
- require learners to explain concepts in their own words.

## Version

Current development version: **PLS 0.1**

This repository is the canonical specification for the standard.

## Core documents

- [`STANDARD.md`](STANDARD.md) — normative pedagogical principles and requirements
- [`LEVELS.md`](LEVELS.md) — PLS progression levels
- [`CHAPTER-TEMPLATE.md`](CHAPTER-TEMPLATE.md) — recommended learning-unit structure
- [`COMPLIANCE.md`](COMPLIANCE.md) — checklist for declaring PLS alignment
- [`GLOSSARY.md`](GLOSSARY.md) — terminology and glossary rules
- [`EXERCISES.md`](EXERCISES.md) — common exercise taxonomy
- [`ADOPTION.md`](ADOPTION.md) — how other repositories adopt and declare PLS
- [`REVIEW.md`](REVIEW.md) — human pedagogical review requirements
- [`LIFECYCLE.md`](LIFECYCLE.md) — review freshness, material changes, and re-review rules
- [`ATTESTATION.md`](ATTESTATION.md) — controlled non-material change attestations
- [`PILOT.md`](PILOT.md) — checklist for the first real-world adoption

## Machine-readable metadata

PLS resources declare their pedagogical contract in a repository-level `pls.yaml` file.

The canonical schema is [`schema/pls.schema.json`](schema/pls.schema.json). A validated example is available in [`examples/pls.yaml`](examples/pls.yaml), and a copy-ready starting point is in [`templates/pls.yaml`](templates/pls.yaml).

Projects preparing for `reviewed` or `compliant` status also declare `resource.review_paths`, identifying the educational files whose semantic changes can invalidate a review.

Example:

```yaml
pls:
  specification: "0.1"
  entry_level: 0
  exit_level: 3
  status: adopting

resource:
  title: "Example resource"
  type: book
  language: [en]
  scope: "The stated subject scope."
  prerequisites: []
  learning_outcomes:
    - "Explain the central concepts using correct terminology."
  review_paths:
    - "course/**"
    - "exercises/**"
```

Validate metadata with:

```sh
python tools/pls_lint.py pls.yaml
```

`pls-lint` validates both the schema and PLS-specific rules such as `exit_level >= entry_level`. For `reviewed` and `compliant` status it also requires valid machine-readable review evidence.

## Review evidence, freshness, and attestations

Completed human reviews are recorded in `pls-review.yaml` and normally accompanied by a human-readable `PLS-REVIEW.md`.

For reviewed resources, freshness can be checked with:

```sh
python tools/pls_staleness.py pls.yaml pls-review.yaml --repo-root .
```

The checker compares the reviewed commit with the current repository state. Changes inside declared `review_paths`, or semantic changes to PLS scope, prerequisites, outcomes, levels, languages, or specification version, make the review stale until assessed or re-reviewed.

Build, CI, packaging, and other non-pedagogical repository changes do not by themselves invalidate a review.

A clearly non-material change inside `review_paths` MAY be covered by a machine-readable `pls-attestation.yaml`. The attestation must reference the original review baseline, identify the exact changed pedagogical paths, name an attestant, explain why learning meaning is unchanged, and cover a specific `through_commit`.

Attestations cannot override material PLS metadata changes or substantive pedagogical changes. When in doubt, re-review.

## Adoption status

PLS uses a progressive adoption model:

```text
adopting -> aligned -> reviewed -> compliant
```

- **adopting** — PLS integration is in progress;
- **aligned** — structure and machine-readable integration are complete;
- **reviewed** — human pedagogical review has been completed and remains current;
- **compliant** — all applicable PLS MUST requirements are satisfied for the declared scope and the supporting review remains current.

Machine validation MUST NOT by itself grant `reviewed` or `compliant` status.

## Level notation

Learning resources may declare an entry and exit level, for example:

```text
PLS: 0 -> 3
```

This means that the resource assumes approximately PLS-0 subject knowledge at entry and aims to bring the learner to PLS-3 competence for its stated scope.

## CI

This repository validates the reference metadata in GitHub Actions. Ploos Edu repositories can copy [`templates/validate-pls.yml`](templates/validate-pls.yml) to `.github/workflows/validate-pls.yml` to validate their own PLS integration.

The CI template uses full Git history so reviewed projects can compare HEAD with the commit recorded in `pls-review.yaml`. If `pls-attestation.yaml` exists, the lifecycle checker validates that it covers the complete pedagogically scoped change range and that no later scoped changes remain uncovered.

Machine validation complements pedagogical review; it does not replace the human compliance review described in `COMPLIANCE.md` and `REVIEW.md`.

## Scope

PLS is intended for all Ploos educational material, including mathematics, computer engineering, electronics, programming, operating systems, compilers, retro-computing courses, and future disciplines.

## Status

PLS 0.1 is an initial working specification. Requirements may change before PLS 1.0.
