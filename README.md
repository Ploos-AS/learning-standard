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

## Machine-readable metadata

PLS resources can declare their pedagogical contract in a repository-level `pls.yaml` file.

The canonical schema is [`schema/pls.schema.json`](schema/pls.schema.json), with a minimal example in [`examples/pls.yaml`](examples/pls.yaml).

Example:

```yaml
pls:
  specification: "0.1"
  entry_level: 0
  exit_level: 3
  status: draft

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

## Level notation

Learning resources may declare an entry and exit level, for example:

```text
PLS: 0 -> 3
```

This means that the resource assumes approximately PLS-0 subject knowledge at entry and aims to bring the learner to PLS-3 competence for its stated scope.

## CI

This repository validates the reference metadata in GitHub Actions. Ploos Edu repositories may reuse the schema and validator to enforce their own `pls.yaml` metadata in CI.

Machine validation complements pedagogical review; it does not replace the human compliance review described in `COMPLIANCE.md`.

## Scope

PLS is intended for all Ploos educational material, including mathematics, computer engineering, electronics, programming, operating systems, compilers, retro-computing courses, and future disciplines.

## Status

PLS 0.1 is an initial working specification. Requirements may change before PLS 1.0.
