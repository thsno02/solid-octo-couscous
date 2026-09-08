---
uid: wiki-page:repo-getzep--graphiti-interfaces-and-operations-3ff5c160c57c
title: getzep/graphiti — interfaces and operations
slug: repos/getzep--graphiti/interfaces-and-operations
page_type: method
status: review
summary: Candidate operating surface of getzep/graphiti.
aliases: []
ontology_refs:
- github-repository
claim_refs: []
source_refs:
- github:getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b
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
  build_id: repo-capsule:getzep--graphiti:3ff5c160c57c
  generated_by_agent: scripts/materialize_pipeline.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-repo-capsule-v1
  compiled_from_revisions:
  - github:getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b
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
  - github:getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Candidate operating surface of getzep/graphiti.
    short: Candidate operating surface of getzep/graphiti.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# Interfaces and operations

- `pip install graphiti-core` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L181`
- `uv add graphiti-core` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L187`
- `pip install graphiti-core[falkordb]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L195`
- `# or with uv` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L197`
- `uv add graphiti-core[falkordb]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L198`
- `# or embedded version (requires Python 3.12+)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L200`
- `pip install graphiti-core[falkordblite]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L201`
- `# or with uv` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L202`
- `uv add graphiti-core[falkordblite]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L203`
- `pip install graphiti-core[kuzu]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L216`
- `# or with uv` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L218`
- `uv add graphiti-core[kuzu]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L219`
- `pip install graphiti-core[neptune]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L227`
- `# or with uv` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L229`
- `uv add graphiti-core[neptune]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L230`
- `# Install with Anthropic support` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L236`
- `pip install graphiti-core[anthropic]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L237`
- `# Install with Groq support` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L239`
- `pip install graphiti-core[groq]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L240`
- `# Install with Google Gemini support` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L242`
- `pip install graphiti-core[google-genai]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L243`
- `# Install with multiple providers` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L245`
- `pip install graphiti-core[anthropic,groq,google-genai]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L246`
- `# Install with FalkorDB and LLM providers` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L248`
- `pip install graphiti-core[falkordb,anthropic,google-genai]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L249`
- `# Install with Amazon Neptune` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L251`
- `pip install graphiti-core[neptune]` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L252`
- `docker compose up` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L297`
- `docker compose --profile falkordb up` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L305`
- `from graphiti_core import Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L353`
- `from graphiti_core.driver.neo4j_driver import Neo4jDriver` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L354`
- `# Create a Neo4j driver with custom database name` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L356`
- `driver = Neo4jDriver(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L357`
- `uri="bolt://localhost:7687",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L358`
- `user="neo4j",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L359`
- `password="password",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L360`
- `database="my_custom_database"  # Custom database name` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L361`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L362`
- `# Pass the driver to Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L364`
- `graphiti = Graphiti(graph_driver=driver)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L365`
- `from graphiti_core import Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L371`
- `from graphiti_core.driver.falkordb_driver import FalkorDriver` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L372`
- `# Create a FalkorDB driver with custom database name` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L374`
- `driver = FalkorDriver(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L375`
- `host="localhost",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L376`
- `port=6379,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L377`
- `username="falkor_user",  # Optional` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L378`
- `password="falkor_password",  # Optional` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L379`
- `database="my_custom_graph"  # Custom database name` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L380`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L381`
- `# Or use embedded FalkorDB Lite (requires Python 3.12+)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L383`
- `# from redislite.async_falkordb_client import AsyncFalkorDB` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L384`
- `# falkordb_client = AsyncFalkorDB(dbfilename='/path/to/database.db')` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L385`
- `# driver = FalkorDriver(falkor_db=falkordb_client)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L386`
- `# Pass the driver to Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L388`
- `graphiti = Graphiti(graph_driver=driver)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L389`
- `from graphiti_core import Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L399`
- `from graphiti_core.driver.kuzu_driver import KuzuDriver` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L400`
- `# Create a Kuzu driver` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L402`
- `driver = KuzuDriver(db="/tmp/graphiti.kuzu")` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L403`
- `# Pass the driver to Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L405`
- `graphiti = Graphiti(graph_driver=driver)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L406`
- `from graphiti_core import Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L412`
- `from graphiti_core.driver.neptune_driver import NeptuneDriver` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L413`
- `# Create a Neptune driver` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L415`
- `driver = NeptuneDriver(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L416`
- `host='<NEPTUNE_ENDPOINT>',` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L417`
- `aoss_host='<AMAZON_OPENSEARCH_SERVERLESS_HOST>',` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L418`
- `port=8182,      # Optional, defaults to 8182` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L419`
- `aoss_port=443,  # Optional, defaults to 443` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L420`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L421`
- `# Pass the driver to Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L423`
- `graphiti = Graphiti(graph_driver=driver)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L424`
- `from openai import AsyncOpenAI` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L436`
- `from graphiti_core import Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L437`
- `from graphiti_core.llm_client.azure_openai_client import AzureOpenAILLMClient` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L438`
- `from graphiti_core.llm_client.config import LLMConfig` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L439`
- `from graphiti_core.embedder.azure_openai import AzureOpenAIEmbedderClient` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L440`
- `# Initialize Azure OpenAI client using the standard OpenAI client` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L442`
- `# with Azure's v1 API endpoint` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L443`
- `azure_client = AsyncOpenAI(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L444`
- `base_url="https://your-resource-name.openai.azure.com/openai/v1/",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L445`
- `api_key="your-api-key",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L446`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L447`
- `# Create LLM and Embedder clients` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L449`
- `llm_client = AzureOpenAILLMClient(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L450`
- `azure_client=azure_client,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L451`
- `config=LLMConfig(model="gpt-5-mini", small_model="gpt-5-mini")  # Your Azure deployment name` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L452`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L453`
- `embedder_client = AzureOpenAIEmbedderClient(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L454`
- `azure_client=azure_client,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L455`
- `model="text-embedding-3-small"  # Your Azure embedding deployment name` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L456`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L457`
- `# Initialize Graphiti with Azure OpenAI clients` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L459`
- `graphiti = Graphiti(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L460`
- `"bolt://localhost:7687",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L461`
- `"neo4j",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L462`
- `"password",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L463`
- `llm_client=llm_client,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L464`
- `embedder=embedder_client,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L465`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L466`
- `# Now you can use Graphiti with Azure OpenAI` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L468`
- `uv add "graphiti-core[google-genai]"` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L488`
- `# or` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L490`
- `pip install "graphiti-core[google-genai]"` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L492`
- `from graphiti_core import Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L496`
- `from graphiti_core.llm_client.gemini_client import GeminiClient, LLMConfig` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L497`
- `from graphiti_core.embedder.gemini import GeminiEmbedder, GeminiEmbedderConfig` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L498`
- `from graphiti_core.cross_encoder.gemini_reranker_client import GeminiRerankerClient` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L499`
- `# Google API key configuration` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L501`
- `api_key = "<your-google-api-key>"` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L502`
- `# Initialize Graphiti with Gemini clients` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L504`
- `graphiti = Graphiti(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L505`
- `"bolt://localhost:7687",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L506`
- `"neo4j",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L507`
- `"password",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L508`
- `llm_client=GeminiClient(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L509`
- `config=LLMConfig(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L510`
- `api_key=api_key,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L511`
- `model="gemini-2.0-flash"` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L512`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L513`
- `),` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L514`
- `embedder=GeminiEmbedder(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L515`
- `config=GeminiEmbedderConfig(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L516`
- `api_key=api_key,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L517`
- `embedding_model="embedding-001"` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L518`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L519`
- `),` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L520`
- `cross_encoder=GeminiRerankerClient(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L521`
- `config=LLMConfig(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L522`
- `api_key=api_key,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L523`
- `model="gemini-2.5-flash-lite"` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L524`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L525`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L526`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L527`
- `# Now you can use Graphiti with Google Gemini for all components` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L529`
- `ollama pull deepseek-r1:7b # LLM` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L549`
- `ollama pull nomic-embed-text # embeddings` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L550`
- `from graphiti_core import Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L554`
- `from graphiti_core.llm_client.config import LLMConfig` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L555`
- `from graphiti_core.llm_client.openai_generic_client import OpenAIGenericClient` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L556`
- `from graphiti_core.embedder.openai import OpenAIEmbedder, OpenAIEmbedderConfig` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L557`
- `from graphiti_core.cross_encoder.openai_reranker_client import OpenAIRerankerClient` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L558`
- `# Configure Ollama LLM client` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L560`
- `llm_config = LLMConfig(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L561`
- `api_key="ollama",  # Ollama doesn't require a real API key, but some placeholder is needed` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L562`
- `model="deepseek-r1:7b",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L563`
- `small_model="deepseek-r1:7b",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L564`
- `base_url="http://localhost:11434/v1",  # Ollama's OpenAI-compatible endpoint` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L565`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L566`
- `llm_client = OpenAIGenericClient(config=llm_config)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L568`
- `# Initialize Graphiti with Ollama clients` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L570`
- `graphiti = Graphiti(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L571`
- `"bolt://localhost:7687",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L572`
- `"neo4j",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L573`
- `"password",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L574`
- `llm_client=llm_client,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L575`
- `embedder=OpenAIEmbedder(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L576`
- `config=OpenAIEmbedderConfig(` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L577`
- `api_key="ollama",  # Placeholder API key` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L578`
- `embedding_model="nomic-embed-text",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L579`
- `embedding_dim=768,` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L580`
- `base_url="http://localhost:11434/v1",` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L581`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L582`
- `),` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L583`
- `cross_encoder=OpenAIRerankerClient(client=llm_client, config=llm_config),` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L584`
- `)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L585`
- `# Now you can use Graphiti with local Ollama models` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L587`
- `export GRAPHITI_TELEMETRY_ENABLED=false` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L668`
- `# For bash users (~/.bashrc or ~/.bash_profile)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L674`
- `echo 'export GRAPHITI_TELEMETRY_ENABLED=false' >> ~/.bashrc` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L675`
- `# For zsh users (~/.zshrc)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L677`
- `echo 'export GRAPHITI_TELEMETRY_ENABLED=false' >> ~/.zshrc` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L678`
- `import os` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L684`
- `os.environ['GRAPHITI_TELEMETRY_ENABLED'] = 'false'` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L686`
- `# Then initialize Graphiti as usual` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L688`
- `from graphiti_core import Graphiti` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L689`
- `graphiti = Graphiti(...)` — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L691`

Commands are syntactically extracted and unverified.
