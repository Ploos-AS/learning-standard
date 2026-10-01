# PLS Pedagogical Review Standard

This document defines the human review process required to move a learning resource from `aligned` to `reviewed` under Ploos Learning Standard (PLS) 0.1.

## 1. Purpose

Machine validation can confirm metadata and structural rules. It cannot establish pedagogical quality.

A PLS review therefore evaluates whether the declared learning path is actually supported by the educational material.

## 2. Reviewer independence

A `reviewed` declaration MUST include at least one named human reviewer who is not the sole primary author of the reviewed material.

The reviewer MAY be:

- another Ploos contributor;
- a subject-matter expert;
- an educator;
- an experienced practitioner able to assess the declared scope and learner level.

The reviewer does not need to be external to Ploos, but SHOULD be sufficiently independent to challenge assumptions made by the author.

Self-review is encouraged during development but MUST NOT by itself grant `reviewed` status.

## 3. Review scope

The review MUST identify:

- repository and revision reviewed;
- PLS specification version;
- declared PLS entry and exit levels;
- educational scope included in the review;
- language editions included;
- known exclusions.

The review applies only to that declared scope and revision.

## 4. Required review areas

The reviewer MUST evaluate all applicable sections of `COMPLIANCE.md`:

1. scope and prerequisites;
2. concepts and terminology;
3. reasoning and rigor;
4. learning design;
5. outcomes;
6. language-edition equivalence where applicable;
7. project declaration and metadata consistency.

The review MUST include direct inspection of real learning content and exercises. Reviewing only metadata, README files, generated tables of contents, or CI output is insufficient.

## 5. Sampling versus complete review

A review MAY use representative sampling for repeated structural patterns, but MUST inspect all high-risk areas relevant to the declared scope.

High-risk areas include:

- prerequisite boundaries;
- first introduction of core notation;
- concepts known to generate common misconceptions;
- major transitions from intuitive to formal treatment;
- declared exit-level material;
- final assessments or capstone work;
- differences between language editions.

The review record MUST state where sampling was used.

## 6. Findings

Each material finding SHOULD be classified as:

- `blocking` — prevents `reviewed` or `compliant` status;
- `required` — must be corrected before `compliant` status;
- `recommended` — worthwhile improvement but not a PLS MUST failure;
- `observation` — informational note.

A project MUST NOT claim `reviewed` while unresolved `blocking` findings remain.

A project MAY claim `reviewed` with unresolved `required` findings if the review itself is complete and those findings are recorded. Such a project MUST NOT claim `compliant`.

## 7. Evidence

A `reviewed` project MUST retain both human-readable and machine-readable review evidence.

The preferred human-readable artifact is:

```text
PLS-REVIEW.md
```

The canonical machine-readable artifact is:

```text
pls-review.yaml
```

`pls-review.yaml` MUST validate against `schema/pls-review.schema.json` for the declared PLS version.

The human-readable evidence MUST record at least:

- reviewer name or stable identity;
- review date;
- reviewed commit or tag;
- PLS version;
- declared PLS range;
- scope and languages reviewed;
- checklist result;
- findings and their disposition;
- overall review conclusion.

The machine-readable evidence MUST identify the reviewed revision, reviewer, date, scope, review result, finding counts, and stable evidence paths.

A `pls-review.yaml` file represents a completed review. Draft or pending review data SHOULD remain in `PLS-REVIEW.md` or another working artifact and MUST NOT be represented as valid completed review evidence.

## 8. Status transition

A project may move from `aligned` to `reviewed` only when:

- PLS metadata validation passes;
- the pedagogical review described here is complete;
- `PLS-REVIEW.md` or equivalent human-readable evidence is retained;
- valid `pls-review.yaml` evidence is retained;
- no unresolved blocking finding remains;
- README and `pls.yaml` are updated consistently.

CI MUST reject a `reviewed` or `compliant` status when valid review evidence is absent.

`reviewed` means that the resource has completed a traceable human review against the declared PLS version. It does not automatically mean that every PLS MUST requirement is satisfied.

## 9. Transition to compliant

A `reviewed` project may move to `compliant` only when:

- every applicable PLS MUST requirement is satisfied for the declared scope;
- all required findings from the review have been resolved or explicitly shown not to apply;
- review evidence identifies the revision for which compliance is claimed;
- `pls-review.yaml` records `review.result: compliant`;
- metadata and CI validation pass;
- language-equivalence requirements are satisfied where applicable.

PLS 0.1 compliance is a project declaration backed by review evidence. It is not third-party certification.

## 10. Re-review

A new pedagogical review SHOULD be performed when a change materially affects:

- prerequisites;
- learning outcomes;
- declared PLS level;
- curriculum structure;
- core explanations;
- assessment strategy;
- a supported language edition;
- the targeted PLS specification version.

Minor typo, formatting, build, or infrastructure changes do not normally invalidate an existing review.
