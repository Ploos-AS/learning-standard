# PLS Adoption Standard

This document defines how a Ploos educational repository adopts the Ploos Learning Standard (PLS).

## 1. Required adoption files

A repository claiming PLS alignment MUST contain:

- `pls.yaml` at the repository root;
- a README section declaring the PLS version and entry/exit levels;
- a link to the canonical PLS specification;
- a passing PLS metadata validation job in CI.

A repository claiming full PLS compliance MUST additionally demonstrate pedagogical review against `COMPLIANCE.md`.

## 2. Status vocabulary

Repositories SHOULD use one of these statuses:

- `not-adopted` — PLS has not been applied;
- `adopting` — metadata and structure are being introduced;
- `aligned` — metadata validates and the resource is intentionally structured around PLS;
- `reviewed` — pedagogical review against the declared PLS version has been completed;
- `compliant` — all MUST requirements for the declared scope have been reviewed and satisfied.

Automated validation MUST NOT by itself grant `reviewed` or `compliant` status.

## 3. Required README declaration

A repository SHOULD include a short section similar to:

```markdown
## Ploos Learning Standard

This project follows the Ploos Learning Standard.

- PLS specification: 0.1
- Entry level: PLS-0
- Exit level: PLS-3
- Status: aligned
```

## 4. Required metadata

The canonical metadata file is `pls.yaml`.

Its structure MUST validate against `schema/pls.schema.json` from the declared PLS specification.

## 5. CI

A PLS-adopting repository MUST validate `pls.yaml` on pushes and pull requests that affect educational content, metadata, or PLS integration.

CI validation establishes machine-readable conformance only. It does not replace pedagogical review.

## 6. Badge

Repositories MAY display a PLS badge.

The badge MUST communicate the actual adoption state and MUST NOT use `compliant` unless the project has completed human pedagogical review.

Recommended badge labels:

- `PLS 0.1 | adopting`
- `PLS 0.1 | aligned`
- `PLS 0.1 | reviewed`
- `PLS 0.1 | compliant`

## 7. Version pinning

A repository MUST declare the PLS specification version it targets.

Upgrading to a newer PLS version is an explicit project change and SHOULD be reviewed like any other normative dependency change.

## 8. Scope

PLS status applies only to the educational scope declared in `pls.yaml`.

A repository containing unrelated tooling, build scripts, or infrastructure does not need to claim PLS compliance for those components.

## 9. Pilot adoption

Before organization-wide rollout, at least one representative educational project SHOULD be used as a pilot. The pilot SHOULD include real prose, exercises, prerequisites, glossary usage, and CI validation so weaknesses in the standard are discovered before broad adoption.
