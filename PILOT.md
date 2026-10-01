# PLS Pilot Checklist

Use this checklist when applying PLS to the first representative educational repository.

## Phase A — Declare

- [ ] Add `pls.yaml` at repository root.
- [ ] Pin the PLS specification version.
- [ ] Declare educational scope.
- [ ] Declare entry and exit levels.
- [ ] List explicit prerequisites.
- [ ] State measurable learning outcomes.
- [ ] Declare language editions.
- [ ] Set status to `adopting`.

## Phase B — Integrate

- [ ] Add README PLS section.
- [ ] Add PLS validation workflow.
- [ ] Ensure metadata validation passes.
- [ ] Add or normalize glossary handling.
- [ ] Classify exercises using the PLS exercise taxonomy.
- [ ] Confirm chapter structure supports intuition-to-rigor progression.

## Phase C — Review

- [ ] Review the resource against `STANDARD.md`.
- [ ] Review against `COMPLIANCE.md`.
- [ ] Check for hidden prerequisites.
- [ ] Check all symbols and specialist terms at first significant use.
- [ ] Check for unexplained reasoning jumps.
- [ ] Check intuitive models for stated limitations.
- [ ] Check misconceptions and common failure modes.
- [ ] Check explain-back/conceptual activities.
- [ ] Verify language editions preserve learning outcomes.

## Phase D — Promote status

- [ ] `adopting` -> `aligned` after structural and CI integration.
- [ ] `aligned` -> `reviewed` after documented human pedagogical review.
- [ ] `reviewed` -> `compliant` only when all applicable MUST requirements are satisfied for the declared scope.

## Pilot feedback to PLS

The pilot SHOULD record any problems found in the standard itself, including:

- requirements that are ambiguous;
- metadata that is missing or overly rigid;
- exercise categories that do not fit real material;
- glossary rules that are impractical;
- CI checks that produce false confidence;
- chapter guidance that conflicts with good pedagogy in a specific discipline.

Pilot findings SHOULD result in changes to PLS before broad organization-wide adoption when appropriate.
