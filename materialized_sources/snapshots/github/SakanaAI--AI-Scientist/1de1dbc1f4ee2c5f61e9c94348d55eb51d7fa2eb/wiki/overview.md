---
uid: wiki-page:repo-sakanaai--ai-scientist-overview-1de1dbc1f4ee
title: SakanaAI/AI-Scientist — repository overview
slug: repos/sakanaai--ai-scientist/overview
page_type: system
status: review
summary: 📚 <a href="https://arxiv.org/abs/2408.06292">[Paper]</a> |
aliases: []
ontology_refs:
- github-repository
claim_refs: []
source_refs:
- github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
page_refs: []
outgoing_links: []
sections: []
temporal:
  created_at: '2026-09-09T00:00:00Z'
  updated_at: '2026-09-09T00:00:00Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-09T00:00:00Z'
provenance:
  build_id: repo-capsule:SakanaAI--AI-Scientist:1de1dbc1f4ee
  generated_by_agent: scripts/materialize_pipeline.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-repo-capsule-v1
  compiled_from_revisions:
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
  created_at: '2026-09-09T00:00:00Z'
  updated_at: '2026-09-09T00:00:00Z'
  manual_edits_preserved: true
review:
  state: automated_checks_only
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Requires semantic review.
freshness:
  status: fresh
  checked_at: '2026-09-09T00:00:00Z'
  max_age_days: 30
  source_dependencies:
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 📚 <a href="https://arxiv.org/abs/2408.06292">[Paper]</a> |
    short: 📚 <a href="https://arxiv.org/abs/2408.06292">[Paper]</a> |
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# SakanaAI/AI-Scientist

📚 <a href="https://arxiv.org/abs/2408.06292">[Paper]</a> |

- Frozen commit: `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb`
- Indexed paths: 2326
- Evidence excerpts: 4

## README outline
- Table of Contents — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L38`
- Introduction — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L57`
- Requirements — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L61`
- Installation — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L65`
- Install pdflatex — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L70`
- Install PyPI requirements — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L73`
- Supported Models and API Keys — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L79`
- OpenAI API (GPT-4o, GPT-4o-mini, o1 models) — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L83`
- Anthropic API (Claude Sonnet 3.5) — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L87`
- Claude Models via Bedrock — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L91`
- Claude Models via Vertex AI — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L103`
- DeepSeek API (deepseek-chat, deepseek-reasoner) — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L121`
- OpenRouter API (Llama3.1) — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L124`
- Google Gemini — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L128`
- Semantic Scholar API (Literature Search) — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L135`
- OpenAlex API (Literature Search Alternative) — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L146`
- Setting Up the Templates — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L160`
- NanoGPT Template — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L164`
- 2D Diffusion Template — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L188`
- Grokking Template — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L213`
- Run AI Scientist Paper Generation Experiments — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L235`
- Run the paper generation. — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L241`
- Getting an LLM-Generated Paper Review — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L248`
- Load paper from PDF file (raw text) — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L257`
- Get the review dictionary — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L260`
- Inspect review results — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L271`
- Making Your Own Template — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L284`
- Community-Contributed Templates — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L297`
- Template Resources — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L311`
- Citing The AI Scientist — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L321`
- Frequently Asked Questions — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L334`
- Containerization — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L370`
- Endpoint Script — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L377`
- Interactive — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L385`
- ⚖️ License & Responsible Use — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L391`
- Star History — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L400`
