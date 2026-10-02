# Ploos Learning Standard 0.1

## 1. Purpose

The Ploos Learning Standard (PLS) defines a shared pedagogical baseline for Ploos educational material.

The core principle is:

> Start intuitively. End rigorously. Leave no hidden steps.

PLS does not reduce the academic level of a subject. It reduces unnecessary barriers to reaching that level.

## 2. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** describe requirement strength within this specification.

## 3. Core requirements

### PLS-REQ-01 — Explicit prerequisites

A learning resource MUST state its assumed subject knowledge. Hidden prerequisites are not permitted.

When a prerequisite is taught in another Ploos resource, the resource SHOULD identify where it can be learned.

### PLS-REQ-02 — Intuition before formalism

When a concept admits a useful intuitive model, the resource SHOULD introduce that model before or alongside formal notation and definitions.

The intuitive model MUST NOT be presented as more exact than it is.

### PLS-REQ-03 — Explain notation

Every new symbol, operator, abbreviation, and specialized term MUST be explained at first pedagogically significant use.

### PLS-REQ-04 — No hidden reasoning steps

Reasoning steps necessary for the declared learner level MUST NOT be omitted merely because they are conventional within the discipline.

Phrases such as "obviously", "trivially", or "it is easy to see" MUST NOT substitute for an explanation.

### PLS-REQ-05 — Concrete to abstract

Where appropriate, instruction SHOULD progress through concrete examples, useful representations, abstraction, and formalization.

### PLS-REQ-06 — Why as well as how

A resource SHOULD explain why a method works and when it is useful, not only how to execute it.

### PLS-REQ-07 — Authentic terminology

A resource MUST teach the real terminology of the field. Simplification MAY be used as a bridge, but MUST NOT permanently replace the correct term.

### PLS-REQ-08 — Multiple representations

Where they materially improve understanding, a resource SHOULD combine complementary representations such as prose, diagrams, equations, tables, code, physical experiments, simulations, or worked examples.

### PLS-REQ-09 — Active learning

A substantial learning resource MUST include activities requiring the learner to do something with the material: predict, calculate, build, modify, test, debug, compare, derive, explain, or solve.

### PLS-REQ-10 — Progressive rigor

Informal explanations MAY precede formal treatment. When an informal model has limitations that matter at the declared exit level, those limitations MUST be made explicit and the model refined or replaced.

### PLS-REQ-11 — Misconceptions

Known high-value misconceptions SHOULD be addressed explicitly.

### PLS-REQ-12 — Explain-back

Major concepts SHOULD include at least one opportunity for the learner to explain the concept in their own words, justify a result, or otherwise demonstrate conceptual understanding rather than mechanical recall alone.

## 4. Recommended learning sequence

A concept SHOULD, when appropriate, follow this pedagogical progression:

1. Question or problem
2. Intuition
3. Concrete example
4. Visualization or alternate representation
5. Exploration
6. Notation
7. Formal definition
8. Derivation or justification
9. Worked example
10. Application
11. Common mistakes and misconceptions
12. Practice
13. Explain-back or conceptual check
14. Connection to what comes next

This sequence is a pedagogical model, not a mandatory set of visible section headings.

## 5. Entry and exit levels

Resources SHOULD declare both entry and target competence using the level system in `LEVELS.md`.

Example:

```text
PLS: 0 -> 3
```

The declared levels apply to the stated scope of the resource, not to an entire discipline.

## 6. Completeness over speed

A resource MUST NOT create artificial simplicity by silently skipping concepts that are necessary to meet its stated learning outcomes.

A shorter explanation is preferred only when it preserves understanding.

## 7. Accessibility of difficulty

Difficulty itself is not a defect. Unexplained difficulty is.

Advanced material MAY be advanced, technical, abstract, or mathematically rigorous while remaining PLS-compliant if the path to that material is explicit and adequately scaffolded.

## 8. Language editions

Different language editions SHOULD preserve equivalent learning outcomes, examples, terminology coverage, exercise intent, and declared PLS levels.

Literal sentence-by-sentence translation is not required when a better pedagogical explanation exists in the target language.

## 9. Conformance

A project claiming PLS alignment SHOULD use `COMPLIANCE.md` during review and SHOULD state the PLS version against which it was reviewed.

Example:

```text
PLS: 0 -> 3
PLS specification: 0.1
```

## 10. AI-assisted development transparency

### PLS-REQ-13 — AI disclosure and human responsibility

When artificial intelligence has materially assisted the creation of a Ploos learning resource, the published resource MUST disclose that use in clear language.

The disclosure SHOULD identify the general kinds of assistance involved, such as ideation, structuring, language editing, or technical quality assurance. It MUST NOT imply that AI is the author or bears editorial responsibility when that is not the case.

A named human author or responsible editor MUST review the published content and retain editorial responsibility for it. AI assistance MUST NOT replace the human pedagogical review required for `reviewed` or `compliant` PLS status.

The standard Ploos publishing colophon SHOULD be used when applicable so that disclosure remains consistent across language editions and publication formats.

## 11. Version status

PLS 0.1 is experimental and may change incompatibly before PLS 1.0.
