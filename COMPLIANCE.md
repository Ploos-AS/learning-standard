# PLS Compliance Checklist

This checklist is intended for authors, reviewers, and CI tooling evaluating a learning resource against a declared PLS version.

A project SHOULD record:

```text
PLS: <entry> -> <exit>
PLS specification: 0.1
```

## A. Scope and prerequisites

- [ ] The scope of the resource is stated.
- [ ] Entry PLS level is declared.
- [ ] Exit PLS level is declared.
- [ ] Required prior subject knowledge is stated explicitly.
- [ ] External prerequisites are linked or otherwise identifiable where practical.
- [ ] No important hidden prerequisite has been identified during review.

## B. Concepts and terminology

- [ ] Major concepts are introduced with an accessible first explanation.
- [ ] Correct field terminology is taught.
- [ ] Simplified language is used only as a bridge, not as a permanent substitute.
- [ ] Every new symbol, operator, abbreviation, and specialized term is explained.
- [ ] Important notation can be traced to its first pedagogically significant introduction.

## C. Reasoning and rigor

- [ ] Necessary reasoning steps are visible for the declared learner level.
- [ ] "Obviously", "trivially", "clearly", or equivalent wording is not used as a substitute for explanation.
- [ ] Informal models are marked as simplified where relevant.
- [ ] Limitations of simplified models are resolved before they matter at the declared exit level.
- [ ] Formal definitions and methods are accurate for the target level.
- [ ] The resource reaches its promised level without hiding essential complexity.

## D. Learning design

- [ ] The learner encounters motivation, a question, or a meaningful problem where appropriate.
- [ ] Concrete examples support important abstractions.
- [ ] Alternative representations are used where they materially improve understanding.
- [ ] The learner performs active work rather than only reading.
- [ ] Practice progresses beyond simple recall where appropriate.
- [ ] Major concepts include conceptual checks, explanation, justification, or transfer.
- [ ] Common misconceptions or high-value mistakes are addressed.

## E. Outcomes

- [ ] Learning outcomes are explicit enough to review.
- [ ] Content supports every declared learning outcome.
- [ ] Exercises or checks provide evidence for the most important outcomes.
- [ ] The exit PLS level matches what the learner is actually expected to demonstrate.
- [ ] Completion criteria do not rely only on mechanical reproduction of procedures.

## F. Language editions

For multi-language material:

- [ ] Editions target equivalent learning outcomes.
- [ ] Editions cover equivalent key terminology.
- [ ] Exercises preserve equivalent learning intent.
- [ ] PLS entry and exit declarations are consistent unless a difference is intentional and documented.
- [ ] Pedagogical adaptation is preferred over awkward literal translation where needed.

## G. Project declaration

A project reviewed against PLS MAY include a declaration such as:

```markdown
## Learning standard

This resource targets **PLS 0 -> 3** and is reviewed against
**Ploos Learning Standard 0.1**.
```

## Compliance status

Suggested project statuses during the 0.x period:

- **PLS-aligned** — designed using PLS principles, but not fully reviewed;
- **PLS-reviewed** — checklist reviewed against a named PLS version;
- **PLS-experimental** — exploring a PLS practice or extension not yet standardized.

PLS 0.1 does not define a formal certification program.

## CI opportunities

Some requirements can later be partially automated. Candidate checks include:

- presence of PLS metadata;
- valid entry/exit level range;
- prerequisite section present;
- learning outcomes present;
- glossary or terminology metadata present when required;
- exercise/checkpoint presence;
- detection of discouraged unexplained-language patterns;
- broken cross-references;
- consistency between language editions.

Automated checks MUST NOT be treated as sufficient evidence of pedagogical quality. Human review remains necessary.
