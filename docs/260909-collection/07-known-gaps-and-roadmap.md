
# Known Gaps and Roadmap

## P0 — collection integrity

1. Migrate every legacy metadata file to the common schema.
2. Materialize and hash P0 arXiv source archives.
3. Verify every GitHub license, canonical owner, release, and head commit.
4. Introduce first-class dataset and benchmark records.
5. Introduce retraction, failed-replication, and incident records.
6. Build reciprocal paper–code–dataset–benchmark links.

## P0 — knowledge architecture

1. Define canonical entity resolution, merge, and split governance.
2. Materialize claim, observation, evidence, contradiction, and uncertainty records.
3. Implement semantic diffs and dependency-aware impact analysis.
4. Define source removal and retraction propagation.
5. Define action permissions for propose, approve, merge, supersede, retract, and rollback.

## P0 — LLM Wiki construction

1. Build a small gold wiki from the P0 corpus.
2. Store page frontmatter under the wiki page schema.
3. Store every generated edit as a wiki change proposal.
4. Add paragraph-level citations and atomic support for high-risk claims.
5. Add deterministic link, source, schema, and dependency validation.
6. Add factuality, citation, contradiction, neutrality, and staleness evaluation.
7. Test a complete rollback and source-retraction rebuild.

## P1

- calibrated probabilistic knowledge;
- causal and counterfactual knowledge;
- units, measurements, and instruments;
- multilingual terminology and citation fidelity;
- semantic federation and data spaces;
- multi-agent concurrent edits and merge conflicts;
- privacy and right-to-erasure propagation;
- million-document routing and incremental compilation;
- institutional consensus, dissent, authority, and jurisdiction.

## Explicit non-goals for the next iteration

- building a polished end-user UI before the data and change contracts work;
- treating vector search quality as the primary wiki success metric;
- automatically merging agent-generated schema changes;
- rewriting every raw source as a summary;
- optimizing page count or link density without task-based evaluation.
