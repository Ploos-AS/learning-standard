# PLS Review Lifecycle and Staleness

This document defines when a completed PLS review remains valid and when it becomes stale.

## 1. Principle

A PLS review applies to the educational content and metadata that were actually reviewed. A later commit does not automatically invalidate the review merely because the repository changed.

The important question is whether the change can materially affect the declared learning path.

## 2. Review scope paths

A project that intends to use `reviewed` or `compliant` status MUST declare `resource.review_paths` in `pls.yaml`.

These are repository-relative glob patterns identifying pedagogically material content, for example:

```yaml
resource:
  review_paths:
    - "course/**"
    - "exercises/**"
    - "solutions/**"
```

The list SHOULD include all learner-facing explanations, exercises, solutions, assessments, language editions, and other files whose semantic content can affect the declared PLS scope.

## 3. Material changes

A review is stale when a commit after the reviewed revision materially changes:

- prerequisites;
- learning outcomes;
- declared entry or exit level;
- educational scope;
- core explanations or examples;
- exercises, assessments, or completion criteria;
- terminology or notation in a way that changes meaning;
- supported language-edition learning intent;
- targeted PLS specification version.

Changes to files matching `resource.review_paths` are treated conservatively as potentially material until reviewed or explicitly assessed otherwise.

## 4. Changes that normally do not invalidate review

The following changes normally do not require a new pedagogical review when they do not alter learning meaning:

- CI or build infrastructure;
- packaging and publishing automation;
- repository administration;
- formatting-only changes;
- spelling or punctuation fixes that do not change meaning;
- link repairs;
- generated artifacts;
- non-educational tooling.

Path-based CI cannot reliably distinguish semantic from formatting-only changes. A project MAY therefore perform a documented maintainer assessment for a change inside `review_paths` and advance the review baseline without a full re-review when the change is demonstrably non-material.

## 5. Baseline

`pls-review.yaml` records the commit whose educational state was reviewed in `review.resource_commit`.

For `reviewed` or `compliant` status, CI SHOULD compare later commits against that baseline.

If no pedagogically material file has changed since the baseline, the review remains current.

If a pedagogically material file has changed, the review becomes stale until one of these occurs:

1. a new or follow-up human review covers the change; or
2. a documented maintainer assessment establishes that the change is non-material and updates the review evidence baseline.

## 6. Status while stale

A project MUST NOT present a stale review as current.

When a review becomes stale, the project SHOULD either:

- return `pls.status` to `aligned`; or
- complete the necessary review before merging the material change.

A project MUST NOT retain `compliant` status while its supporting review is stale.

## 7. CI behavior

PLS staleness tooling SHOULD:

- run only for `reviewed` and `compliant` projects;
- require `resource.review_paths`;
- require a valid `pls-review.yaml`;
- verify that `review.resource_commit` exists in repository history;
- list files changed since the reviewed commit;
- fail when any changed file matches a declared review path;
- ignore changes outside the declared pedagogical review paths.

The CI result is conservative evidence of freshness. It is not a substitute for human judgment about pedagogical meaning.

## 8. History availability

Staleness checks require Git history reaching the reviewed commit. CI integrations SHOULD therefore use a full checkout (`fetch-depth: 0`) or otherwise fetch the reviewed revision before running the staleness check.

## 9. PLS version changes

Changing the targeted PLS specification version always requires explicit review assessment. A review against PLS 0.1 cannot silently establish review status against a later specification.
