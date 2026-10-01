# Pilot: EduNumbers

## Repository

`Ploos-AS/EduNumbers`

## Purpose

EduNumbers is the first real-world pilot of the Ploos Learning Standard (PLS) 0.1.

The pilot tests whether the standard can be adopted by an existing bilingual educational project without disrupting its publication, build, or CI structure.

## Declared contract

- Specification: PLS 0.1
- Entry level: PLS-0
- Exit level: PLS-3
- Adoption status: adopting
- Languages: Norwegian and English
- Resource type: course

## Existing pedagogical strengths

EduNumbers already follows a strong chapter-level teaching loop:

`PREDICT -> STEP -> OBSERVE -> EXPLAIN`

This maps naturally to the PLS requirements for active learning, explicit reasoning, multiple representations, and explain-back.

The curriculum also progresses from first principles into practical systems work, including number representation, binary and hexadecimal, integer formats, bit operations, memory, endianness, floating point, assembly notation, programming languages, hardware registers, networking, file formats, debugging, and reverse engineering.

## Pilot changes

The EduNumbers repository now contains:

- a repository-level `pls.yaml` pedagogical contract;
- a `Validate PLS` GitHub Actions workflow;
- README documentation showing the active PLS version, entry level, target level, and adoption status.

The existing build and publication pipeline remains independent of PLS validation.

## Findings

### PLS-FINDING-001 — Existing teaching models can coexist with PLS

PLS should define outcomes and pedagogical requirements without replacing useful project-specific teaching cycles such as EduNumbers' `PREDICT -> STEP -> OBSERVE -> EXPLAIN` model.

### PLS-FINDING-002 — Project metadata needs one canonical contract

A single repository-level `pls.yaml` is useful even when a project has separate course, book, website, and interactive outputs, provided they share the same pedagogical scope.

If outputs later diverge materially in scope or level, PLS should support per-resource contracts rather than overloading one declaration.

### PLS-FINDING-003 — Machine validation is necessary but insufficient

Schema validation can verify declared structure, levels, languages, prerequisites, and outcomes. It cannot determine whether explanations are pedagogically sound or whether hidden reasoning steps remain in the content.

Human pedagogical review therefore remains required before `compliant` status.

### PLS-FINDING-004 — Adoption should not require publication changes

PLS adoption must remain orthogonal to HTML, EPUB, PDF, Kindle, Pages, and other publication pipelines. Educational projects should be able to adopt PLS incrementally.

## Next review gate

EduNumbers remains `adopting` until a content review verifies at minimum:

- explicit prerequisites and learning outcomes;
- notation introduced before use;
- no unexplained conceptual jumps at the declared learner level;
- adequate active-learning exercises;
- misconception handling where relevant;
- explain-back/conceptual checks for major concepts;
- equivalent pedagogical intent across Norwegian and English editions.

After these checks, the project may progress to `aligned`, then `reviewed`, and finally `compliant` according to `ADOPTION.md`.
