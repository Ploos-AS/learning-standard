# Changelog

All notable changes to the Ploos Learning Standard (PLS) are documented here.

## 0.1.0 — 2026-10-01

Initial public working release of PLS.

### Standard

- Defines the core pedagogical principle: **Start intuitively. End rigorously. Leave no hidden steps.**
- Defines PLS levels 0 through 5.
- Defines normative pedagogical requirements PLS-REQ-01 through PLS-REQ-12.
- Defines chapter, glossary, exercise, compliance, adoption, review, lifecycle, and attestation guidance.

### Metadata and validation

- Adds canonical `pls.yaml` metadata and JSON Schema validation.
- Adds the status progression `adopting -> aligned -> reviewed -> compliant`.
- Adds machine-readable `pls-review.yaml` evidence for reviewed/compliant resources.
- Adds machine-readable `pls-attestation.yaml` for narrowly scoped non-material changes.
- Adds review-path declarations and review freshness checks.

### Tooling

- Adds `tools/pls_lint.py` for metadata and review-evidence validation.
- Adds `tools/pls_staleness.py` for review freshness and attestation validation.
- Adds GitHub Actions integration templates.
- Adds automated state-machine tests covering positive and negative lifecycle cases.

### Pilot

- EduNumbers is the first PLS pilot and has reached `aligned` for PLS 0 -> 3.

### Compatibility

PLS 0.x is pre-1.0. Breaking changes remain possible between minor 0.x releases. Downstream repositories SHOULD pin an immutable release tag or exact commit rather than tracking `main`.
