# PLS Release and Pinning Policy

This document defines how Ploos Learning Standard releases are prepared and how downstream repositories should consume them.

## 1. Versioning

PLS uses semantic-style version identifiers.

During the pre-1.0 period:

- `0.x.0` may contain breaking changes to schemas, metadata, tooling, or normative requirements;
- `0.x.y` patch releases should remain compatible with the corresponding `0.x.0` contract unless correcting a defect that made the documented contract impossible to implement correctly.

PLS 1.0 will establish the first long-term stable compatibility contract.

## 2. Release identifiers

Canonical release tags use:

```text
vMAJOR.MINOR.PATCH
```

The first planned release is:

```text
v0.1.0
```

A release tag MUST identify one immutable commit containing the exact schemas, tooling, templates, tests, and documentation for that release.

## 3. Release gate

A release MUST NOT be tagged unless:

- the standard's own CI is green;
- state-machine tests pass;
- canonical schemas and templates validate;
- `CHANGELOG.md` describes the release;
- README version information matches the intended release;
- downstream integration instructions do not depend on `main`.

## 4. Downstream pinning

Production or reviewed PLS integrations MUST NOT depend on `main`.

Preferred pinning order:

1. exact immutable commit SHA for maximum reproducibility;
2. immutable release tag such as `v0.1.0` for readability and normal project use.

A moving branch such as `main` MAY be used only while experimentally adopting unreleased PLS changes.

Example GitHub Actions checkout:

```yaml
- name: Check out PLS specification
  uses: actions/checkout@v4
  with:
    repository: Ploos-AS/learning-standard
    ref: v0.1.0
    path: .pls-standard
```

For stronger supply-chain reproducibility, a downstream repository MAY replace the tag with the exact commit SHA behind the release.

## 5. Upgrade policy

Changing the pinned PLS release is an explicit dependency upgrade.

A project moving between PLS versions SHOULD:

- read the changelog;
- validate `pls.yaml` against the new schema;
- run the full PLS CI integration;
- assess whether normative pedagogical requirements changed;
- perform re-review when required by `LIFECYCLE.md`.

A project MUST NOT silently change the PLS specification version while retaining review evidence from a different specification version.

## 6. Release process

For each release:

1. freeze intended normative and tooling changes;
2. run self-CI and the state-machine tests;
3. update `CHANGELOG.md` and README version information;
4. create the immutable release tag;
5. publish release notes matching the changelog;
6. update downstream templates/projects to use the release tag or exact commit;
7. verify at least one pilot project against the released version.

## 7. Main branch

`main` remains the development head of PLS. It may move ahead of the latest release and therefore MUST NOT be interpreted as equivalent to a published PLS version.
