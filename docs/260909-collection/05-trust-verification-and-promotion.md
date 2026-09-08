
# Trust, Verification, and Promotion

## Three independent questions

Every pipeline must distinguish:

1. **Authenticity** — did this content come from the claimed source?
2. **Conformance** — does the record satisfy the declared schema or shape?
3. **Epistemic support** — does the evidence support the claim as written?

Passing one does not imply the others.

## Source verification states

- `verified` — canonical identity and selected metadata were checked against a primary source;
- `partially_verified` — some important fields remain unresolved;
- `pending` — discovered but not verified;
- `quarantined` — retained for lineage but blocked from trusted use;
- `deprecated` — superseded record or alias;
- `retracted` — source has a formal retraction or equivalent withdrawal.

## Evidence levels

The collection distinguishes conceptual arguments, simulations, benchmarks, reproduction, field deployment, and independent replication. A popular repository or highly cited paper is not automatically field validation.

## Knowledge promotion states

The future claim layer should use:

```text
raw
→ parsed
→ candidate
→ corroborated
→ trusted
```

with side paths:

```text
candidate → contested
any state → quarantined
trusted → superseded
trusted → retracted
```

The future wiki page layer uses different states:

```text
draft → review → published → stale → deprecated
```

A published page may contain contested claims if disagreement is represented correctly. Page publication and claim truth status are therefore separate.

## Minimum promotion gates

A factual claim cannot enter the trusted layer unless it has:

- stable subject and predicate identity;
- explicit assertion kind;
- one or more evidence selectors;
- source and source revision;
- temporal and contextual scope where relevant;
- contradiction search;
- reviewer or evaluator identity;
- promotion decision and timestamp;
- rollback or supersession path.

High-risk, exceptional, or action-triggering claims require multiple independent sources or an explicit waiver.

## Circularity rule

A wiki page, generated answer, model output, or derivative mirror does not constitute independent corroboration of its own upstream content. The pipeline must trace citations to external canonical sources and detect self-citation loops.

## Retraction and deletion

When a source is removed or retracted:

1. do not erase its history;
2. mark the source state;
3. identify dependent claims;
4. downgrade or contest affected claims;
5. rebuild affected pages and context packs;
6. preserve the before/after diff;
7. record the review and rollback decision.
