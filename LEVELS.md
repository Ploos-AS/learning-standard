# PLS Levels

PLS levels describe competence within the stated scope of a learning resource. They are not global labels for a person.

A resource may declare an entry and exit level, for example:

```text
PLS: 0 -> 3
```

## PLS-0 — No assumed subject knowledge

The learner is assumed to have no meaningful prior knowledge of the subject itself.

The resource:

- establishes vocabulary and motivation;
- introduces the first mental models;
- explains notation from first principles;
- avoids relying on discipline-specific conventions without explanation.

General literacy, basic numeracy, or tool use may still be required, but such assumptions MUST be stated when material.

## PLS-1 — Foundational understanding

The learner can recognize and explain the main concepts at an introductory level.

Typical outcomes include:

- define key terms in ordinary language;
- identify basic structures or components;
- follow simple worked examples;
- perform elementary operations with guidance;
- connect representations such as words, diagrams, notation, or code.

## PLS-2 — Practical application

The learner can use the concepts independently in standard situations.

Typical outcomes include:

- solve routine problems;
- choose among basic methods;
- construct or modify small examples;
- detect common mistakes;
- explain why a standard method is appropriate.

## PLS-3 — Formal subject competence

The learner can work with the formal language and standard methods of the field within the stated scope.

Typical outcomes include:

- use formal definitions and notation correctly;
- derive or justify important results at the expected level;
- solve non-trivial problems;
- transfer knowledge to unfamiliar but related situations;
- explain limitations, assumptions, and trade-offs.

For many introductory university-level resources, PLS-3 is a natural target.

## PLS-4 — Advanced analysis and synthesis

The learner can combine ideas, evaluate alternatives, and handle substantially less structured problems.

Typical outcomes include:

- compare competing methods or models;
- analyze edge cases and failure modes;
- synthesize multiple concepts into larger solutions;
- reason independently from assumptions to conclusions;
- critique implementations, proofs, experiments, or designs.

## PLS-5 — Deep specialization and further-study readiness

The learner has a level of mastery suitable for advanced study, specialist practice, or engagement with primary technical or academic material within the scope.

Typical outcomes include:

- read advanced literature with limited scaffolding;
- work with high abstraction or technical depth;
- formulate and investigate new problems;
- connect the topic to adjacent advanced disciplines;
- distinguish established results from open questions, conventions, or active areas of research.

## Levels are not age bands

PLS levels do not correspond to age, school year, degree level, or intelligence.

A ten-year-old and an experienced engineer may both be PLS-0 when entering a genuinely new subject.

## Levels are scope-specific

A learner may be PLS-4 in digital electronics and PLS-0 in abstract algebra. Therefore every level declaration MUST be interpreted relative to the learning outcomes and scope of the specific resource.

## Entry level versus exit level

The entry level describes what the learner is expected to know before beginning. The exit level describes the intended competence after successfully completing the resource.

Examples:

```text
PLS: 0 -> 2
```

An accessible practical introduction.

```text
PLS: 1 -> 3
```

A course that assumes basic familiarity and reaches formal competence.

```text
PLS: 3 -> 5
```

An advanced specialist resource.
