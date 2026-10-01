# PLS Glossary Rules

A PLS resource SHOULD maintain a glossary when it introduces specialized terminology beyond a small number of terms.

## Requirements

1. A technical term MUST be explained at first pedagogically significant use.
2. The glossary MUST NOT be the only place where a term is explained.
3. Simplified bridge language MAY precede the authentic term, but the authentic term MUST be introduced.
4. Synonyms and competing terminology SHOULD be noted when learners are likely to encounter them elsewhere.
5. Symbols and notation SHOULD be included when they function as vocabulary within the discipline.
6. Language editions SHOULD preserve equivalent conceptual coverage even when literal translations differ.

## Recommended entry format

```markdown
### Eigenvector

**Plain-language bridge:** A direction that a linear transformation does not turn away from itself.

**Formal meaning:** A non-zero vector `v` for which `Av = λv` for some scalar `λ`.

**Related:** eigenvalue, linear transformation, basis

**Common misconception:** An eigenvector is not generally unchanged; its magnitude may change and its direction may reverse.
```

## Review questions

- Is the learner likely to meet this word before it is explained?
- Is the bridge explanation useful without being misleading?
- Is the formal meaning appropriate for the declared exit level?
- Are important alternate terms included?
- Are known misconceptions called out?
