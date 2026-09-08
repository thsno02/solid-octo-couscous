
# 260909 Collection Snapshot

This documentation records the collection work completed for `thsno02/solid-octo-couscous` on **2026-09-09**. It is the handoff contract for future humans and agents.

The snapshot covers the research background needed to study:

> knowledge self-evolution and agent governance, situated inside the wider fields of recursive self-improvement, open-ended evolution, automated research, ontology, and LLM-compiled wikis.

## Read in this order

1. [`01-mission-and-scope.md`](01-mission-and-scope.md)
2. [`02-coverage-map.md`](02-coverage-map.md)
3. [`03-source-model-and-directory-layout.md`](03-source-model-and-directory-layout.md)
4. [`04-metadata-schemas-and-identifiers.md`](04-metadata-schemas-and-identifiers.md)
5. [`05-trust-verification-and-promotion.md`](05-trust-verification-and-promotion.md)
6. [`06-collection-workflow-and-ci.md`](06-collection-workflow-and-ci.md)
7. [`07-known-gaps-and-roadmap.md`](07-known-gaps-and-roadmap.md)
8. [`08-agent-handoff-and-operating-rules.md`](08-agent-handoff-and-operating-rules.md)
9. [`09-batch-ledger.md`](09-batch-ledger.md)

## Authoritative machine-readable entry points

- `raw_data/index.yaml`
- `raw_data/manifest.yaml`
- `raw_data/manifests/*.yaml`
- `raw_data/collections/*.yaml`
- `raw_data/schemas/*.yaml`
- `raw_data/audits/*.yaml`
- `raw_data/quarantine/*.yaml`

The prose in this directory explains intent. The YAML files define the current machine-readable inventory and policy.

## Important limitation

Most arXiv records currently preserve the exact `/src/<id>` and PDF URLs, but their TeX bundles have not yet been downloaded, unpacked, hashed, and pinned. Metadata availability is not full-text acquisition.
