# PLS Non-Material Change Attestation

This document defines the narrow exception that allows a reviewed or compliant PLS resource to remain current after a change inside `resource.review_paths` when the change is demonstrably non-material to learning meaning.

## 1. Purpose

Path-based review freshness is intentionally conservative. A spelling correction inside a course chapter and a rewritten explanation both touch pedagogical files, but they do not have the same review impact.

A non-material attestation records a human assessment that a specific set of changes does not alter the reviewed learning state.

An attestation is not a replacement for pedagogical review.

## 2. Canonical artifact

The canonical machine-readable artifact is:

```text
pls-attestation.yaml
```

It MUST validate against `schema/pls-attestation.schema.json` for the declared PLS version.

## 3. When attestation MAY be used

Attestation MAY be used for changes such as:

- spelling, grammar, or punctuation corrections;
- formatting changes;
- link repairs;
- wording changes that preserve the same pedagogical meaning;
- equivalent localization corrections;
- code or example formatting that does not change behavior or interpretation.

The attestant MUST inspect the actual diff and determine that the reviewed learning intent is unchanged.

## 4. When attestation MUST NOT be used

Attestation MUST NOT be used to bypass re-review for changes to:

- PLS specification version;
- declared entry or exit level;
- educational scope;
- prerequisites;
- learning outcomes;
- supported language set;
- core conceptual meaning;
- notation or terminology meaning;
- examples where the reasoning or result changes;
- exercises, solutions, assessments, or completion criteria where learner expectations change;
- misconception treatment where meaning changes;
- any change that could reasonably alter whether a PLS MUST requirement is satisfied.

Material PLS metadata changes always require review assessment and cannot be overridden by attestation.

## 5. Required fields

An attestation MUST identify:

- the PLS specification version;
- the original reviewed commit;
- the last commit covered by the attestation (`through_commit`);
- the assessment date;
- the attestant name and role;
- a substantive reason explaining why the change is non-material;
- the exact pedagogically scoped files changed in the covered range.

The reason MUST describe the educational impact, not merely say that the change is "small".

## 6. Commit-range semantics

`review_commit` MUST equal the baseline recorded in `pls-review.yaml`.

`through_commit` MUST:

- descend from the reviewed commit;
- exist in the current branch history;
- cover every pedagogically scoped change being attested.

The `changed_paths` list MUST exactly match files under `resource.review_paths` changed between `review_commit` and `through_commit`.

If any pedagogically scoped file changes after `through_commit`, the previous attestation no longer covers HEAD.

## 7. Attestant

The attestant MAY be a maintainer or reviewer capable of assessing the educational impact of the change.

Unlike a full `reviewed` transition, attestation does not require a new independent reviewer. However, the attestant SHOULD escalate uncertain cases to pedagogical re-review rather than self-attest.

For `compliant` resources, maintainers SHOULD use a particularly conservative threshold because the attestation preserves a compliance claim.

## 8. Evidence

The attestation MAY link additional evidence such as:

- a pull request;
- a diff review;
- an issue documenting the correction;
- a language-equivalence check.

The repository history plus the machine-readable attestation form the minimum traceable record.

## 9. CI behavior

PLS lifecycle tooling SHOULD:

1. check ordinary review freshness first;
2. fail on material metadata changes regardless of attestation;
3. validate `pls-attestation.yaml` when present;
4. verify its review baseline and commit ancestry;
5. verify `changed_paths` against the actual Git diff;
6. verify that no later pedagogically scoped changes exist;
7. report `CURRENT BY ATTESTATION` only when all checks pass.

## 10. Prefer re-review when uncertain

Attestation exists to prevent needless full reviews for clearly non-material edits. It MUST NOT become a mechanism for gradually changing educational content while preserving an obsolete review baseline.

When there is reasonable doubt about pedagogical impact, perform a follow-up review and update `pls-review.yaml` instead.
