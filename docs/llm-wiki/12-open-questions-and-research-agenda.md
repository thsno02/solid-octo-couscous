
# Open Questions and Research Agenda

## Knowledge compilation

- What should be compiled ahead of time when future queries are unknown?
- How should materiality, novelty, and expected utility influence retention?
- When is a Markdown page better than a graph neighborhood or context pack?
- How can the system avoid recursive lossy summarization?

## Claim and page relationship

- What is the right atomicity for claims?
- How should one claim support several pages without drift?
- Can page regeneration preserve deliberate human rhetoric and pedagogy?
- How should editorial framing be represented without pretending it is evidence?

## Contradiction and consensus

- How should implicit contradiction be detected across thousands of pages?
- When should a conflict become a debate page, a qualifier, or a supersession?
- How should due weight be measured?
- How can consensus be recorded without erasing dissent?

## Freshness and deletion

- How should source change significance be estimated?
- What is the correct rebuild boundary?
- How should source retraction affect derived claims and summaries?
- Can right-to-erasure be propagated through claims, embeddings, pages, and model caches?

## Evaluation

- Which tasks demonstrate that a wiki improves understanding rather than only retrieval?
- How should citation entailment be measured across TeX, tables, figures, and code?
- How do we evaluate narrative organization without rewarding verbosity?
- How can evaluator gaming and self-preference be detected?
- What does independent replication mean for a generated knowledge page?

## Multi-agent governance

- How are concurrent edits merged semantically?
- Which roles require independent agents or humans?
- How are reviewer reputation and domain expertise represented?
- Can an agent improve prompts and schemas without changing the objective of knowledge promotion?
- How should audit samples be selected?

## Ontology and identity

- How can ontology changes trigger safe page migration?
- How should entity merge/split proposals be benchmarked?
- What mappings are equivalence, close match, or contextual alignment?
- How should unknown, no-value, false, and undisclosed states appear in prose?

## Scale

- What replaces a single `index.md` at 100,000 or one million sources?
- How should maps of content be generated and reviewed?
- Can community detection discover useful structure without reifying noise?
- How should build cost, query cost, and maintenance cost be jointly optimized?

## Initial experiments

1. Compare raw-source RAG, compiled wiki, and wiki-plus-source access on a fixed research question set.
2. Remove one key source and measure unsupported-text cleanup.
3. Introduce a contradictory source and measure conflict preservation.
4. Change an ontology identity criterion and measure impact detection.
5. Ask two agents to edit the same comparison page and evaluate semantic merge.
6. Evaluate page usefulness before and after claim-level provenance.
7. Test whether saved query answers create circular support.
