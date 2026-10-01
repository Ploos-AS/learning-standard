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
- [`PILOT.md`](PILOT.md) — checklist for the first real-world adoption

## Machine-readable metadata

PLS resources declare their pedagogical contract in a repository-level `pls.yaml` file.

The canonical schema is [`schema/pls.schema.json`](schema/pls.schema.json). A validated example is available in [`examples/pls.yaml`](examples/pls.yaml), and a copy-ready starting point is in [`templates/pls.yaml`](templates/pls.yaml).

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
```

Validate metadata with:

```sh
python tools/pls_lint.py pls.yaml
```

`pls-lint` validates both the schema and PLS-specific rules such as `exit_level >= entry_level`.

## Adoption status

PLS uses a progressive adoption model:

```text
adopting -> aligned -> reviewed -> compliant
```

- **adopting** — PLS integration is in progress;
- **aligned** — structure and machine-readable integration are complete;
- **reviewed** — human pedagogical review has been completed;
- **compliant** — all applicable PLS MUST requirements are satisfied for the declared scope.

Machine validation MUST NOT by itself grant `reviewed` or `compliant` status.

## Level notation

Learning resources may declare an entry and exit level, for example:

```text
PLS: 0 -> 3
```

This means that the resource assumes approximately PLS-0 subject knowledge at entry and aims to bring the learner to PLS-3 competence for its stated scope.

## CI

This repository validates the reference metadata in GitHub Actions. Ploos Edu repositories can copy [`templates/validate-pls.yml`](templates/validate-pls.yml) to `.github/workflows/validate-pls.yml` to validate their own `pls.yaml`.

Machine validation complements pedagogical review; it does not replace the human compliance review described in `COMPLIANCE.md`.

## Scope

PLS is intended for all Ploos educational material, including mathematics, computer engineering, electronics, programming, operating systems, compilers, retro-computing courses, and future disciplines.

## Status

PLS 0.1 is an initial working specification. Requirements may change before PLS 1.0.
