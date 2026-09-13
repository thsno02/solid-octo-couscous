# Repository semantic capsule: gavischneider/awesome-llm-wiki

- Commit: `4f3ce87f2cb9c5696bd3df3f4d76bef5690ba563`
- Default branch: `main`
- Description: gavischneider/awesome-llm-wiki
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

![Awesome LLM Wiki](https://github.com/user-attachments/assets/f6e4ba61-06cc-4384-b7c4-dba987b8d6a9)

# Awesome LLM Wiki [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last-Commit](https://img.shields.io/github/last-commit/gavischneider/awesome-llm-wiki) [![Join the Discussion](https://img.shields.io/badge/Reddit-r/LLM_Wiki-orange)](https://reddit.com/r/LLM_Wiki) [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/gavischneider/awesome-llm-wiki) [![Stars](https://img.shields.io/github/stars/gavischneider/awesome-llm-wiki)](https://github.com/gavischneider/awesome-llm-wiki)

> A curated list of foundational blueprints, functional frameworks, and technical guides for building compounding, AI-compiled knowledge bases.

Inspired by a paradigm shift in software development engineering, this architecture treats large language models not as ephemeral chat engines, but as stateful knowledge compilers. Instead of parsing fragmented document partitions dynamically at runtime via traditional RAG loops, these systems leverage autonomous agents to read static source files and systematically construct an interlinked, persistent Markdown knowledge topology.

---

## Contents

- [Foundations](#foundations)
- [GitHub Gists](#github-gists)
- [Articles and Guides](#articles-and-guides)
  - [Conceptual Primers and Foundations](#conceptual-primers-and-foundations)
  - [Comparative Analyses (Wiki vs. RAG)](#comparative-analyses-wiki-vs-rag)
  - [Codebase and Developer Context](#codebase-and-developer-context)
  - [Digital Gardens and Public Notes](#digital-gardens-and-public-notes)
  - [Scaling and Enterprise Systems](#scaling-and-enterprise-systems)
  - [Tutorials and Setup Guides](#tutorials-and-setup-guides)
  - [Case Studies and Retrospectives](#case-studies-and-retrospectives)
- [Books and Ebooks](#books-and-ebooks)
- [Specifications and Standards](#specifications-and-standards)
- [Tools and Plugins](#tools-and-plugins)
  - [Libraries and Frameworks](#libraries-and-frameworks)
  - [Applications and Desktop Clients](#applications-and-desktop-clients)
  - [Editor Extensions and Plugins](#editor-extensions-and-plugins)
  - [General-Purpose Wiki Compilers](#general-purpose-wiki-compilers)
  - [Codebase and Documentation Builders](#codebase-and-documentation-builders)
  - [Graph Compilation and Semantic Link Analyzers](#graph-compilation-and-semantic-link-analyzers)
  - [Ingestion and Synchronization Utilities](#ingestion-and-synchronization-utilities)
  - [MCP Servers and Integrations](#mcp-servers-and-integrations)
  - [Hosting and Infrastructure Platforms](#hosting-and-infrastructure-platforms)
  - [Agent Skills and System Rules](#agent-skills-and-system-rules)
  - [Starter Templates and Boilerplates](#starter-templates-and-boilerplates)
- [Live Implementations and Reference Vaults](#live-implementations-and-reference-vaults)
- [Research and Papers](#research-and-papers)
- [Academic Courses and Lectures](#academic-courses-and-lectures)
- [Videos](#videos)
- [Podcasts](#podcasts)
  - [Build With AI](#build-with-ai)
  - [Microsoft Cloud IT Pro Podcast](#microsoft-cloud-it-pro-podcast)
  - [Working Code Podcast](#working-code-podcast)
- [Forums and Discussions](#forums-and-discussions)

## Foundations

*Foundational material from Andrej Karpathy that introduced and defined the LLM Wiki architecture.*

- [Andrej Karpathy's First Post on LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595) - The original post by Andrej Karpathy introducing the concept of using LLMs to compile and maintain persistent, file-based knowledge bases over traditional RAG.
- [Andrej Karpathy's Follow-up Post on the LLM Wiki Idea File](https://x.com/karpathy/status/2040470801506541998) - The follow-up post by Andrej Karpathy publishing the formal LLM Wiki gist and conceptual framework for autonomous knowledge compilation.
- [Andrej Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) - The foundational idea file laying out the core pattern, operations, and architecture for compounding AI knowledge bases.

## GitHub Gists

*Community blueprints, proof-of-concept system schemas, and architectural experiments published as GitHub Gists.*

- [Farza's Personal Wiki Skill](https://gist.github.com/farzaa/c35ac0cfbeb957788650e36aabea836d) - A functional blueprint for implementing an LLM wiki compiler using Claude Code skills, including commands for ingestion, absorption, and automated cleanup.
- [graphwiki: an LLM Wiki pattern for graph databases](https://gist.github.com/lucianfialho/44034e0d02a2bfccca2ad6358bde1dff) - A conceptual blueprint mapping the LLM Wiki pattern to a property graph (Neo4j) with entity resolution benchmarks.
- [LLM Wiki v2](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) - An architectural extension of Karpathy's blueprint focused on scale, memory lifecycles, confidence decay, and typed knowledge graphs.
- [LLM Wiki v3: A State-Space Knowledge System](https://gist.github.com/HousamKak/ba96124547d1b7c68d270c293106fe53) - An architectural specification extending the LLM Wiki pattern into a probabilistic state-space model where the LLM extracts structured observations, a belief engine updates evidence states, and markdown wiki pages are rendered as deterministic views of underlying truth graphs.
- [LLM Wiki V3: Segmentation](https://gist.github.com/ahumanft/6c96385be6ca4af578cc9b20e0f79e66) - A scaling specification addressing context drift and schema overload in LLM Wikis. Proposes segmenting systems into specialized roles (Ingestor, Librarian, Linter), dual ingestion modes ('restricted section' deep curation vs. 'open stacks' shallow indexing), explicit schema triggers to minimize drifting implicit instructions, and cache rewarming to prevent multi-agent navigation bias.

## Articles and Guides

*Technical examinations, exhaustive architectural deep-dives, and detailed workflow overviews.*

### Conceptual Primers and Foundations

*High-level conceptual breakdowns, foundational ideas, and introductory guides to the LLM Wiki concept.*

- [Andrej Karpathy Wiki: LLM Wiki Concept Guide](https://andrej-karpathy.com/#/concepts/llm-wiki.md) - A conceptual breakdown embedded inside the live Karpathy encyclopedia detailing the explicit operating models, file structures, and automated compilation loops that define a production-grade LLM Wiki setup.
- [Andrej Karpathy's LLM Knowledge Bases Explained (Mehul Gupta on Medium)](https://medium.com/data-science-in-your-pocket/andrej-karpathys-llm-knowledge-bases-explained-2d9fd3435707) - A conceptual primer explaining the LLM Wiki pattern. Contrasts standard vector RAG (where the model remains a "tourist") with Karpathy's compiled knowledge approach (where the model acts as a "compiler"), detailing the workflow steps of collection, compilation, maintenance, and querying.
- [Andrej Karpathy’s LLM Wiki: Full Breakdown and How to Build Your Own (Hari Krishna on Tech in General Substack)](https://nandigamharikrishna.substack.com/p/andrej-karpathys-llm-wiki-full-breakdown) - A comprehensive conceptual primer detailing the limitations of stateless RAG, explaining the three-layer architecture (immutable raw sources, LLM-generated markdown notes, and system schema configuration), outlining the three core operations (Ingest, Query, Lint), and connecting the pattern to Vannevar Bush's Memex.
- [Building an 'Agent Only' Obsidian Vault (The Thinkers Club)](https://www.thethinkers.club/p/building-an-agent-only-obsidian-vault) - A technical architectural guide defining a human-agent sandbox paradigm. Details a methodology for isolating autonomous AI writers inside a dedicated secondary vault to compile a self-organizing wiki of consumed data, preventing context contamination and layout drift in human-authored notes.
- [Building Self-Correcting Memory in OpenWiki (LangChain Blog)](https://www.langchain.com/blog/self-correcting-memory-openwiki) - A technical
  primer exploring how OpenWiki manages memory staleness and drift for evolving codebases. Details the use of a
  "claims runtime" that connects wiki assertions to versioned code evidence, allowing agents to detect, track, and
  correct stale knowledge without rebuilding vaults from scratch.
- [Commonplace](https://zby.github.io/commonplace/) - A technical framework establishing the theory of deploy-time learning for bounded AI observers, detailing semantic distillation operations, and providing automated CLI workspace management skills.
- [Compounding Knowledge with LLMs: Karpathy's Wiki Pattern in Action](https://pub.towardsai.net/compounding-knowledge-with-llms-karpathys-wiki-pattern-in-action-d01db84d5b8b) - An architectural analysis connecting Andrej Karpathy's LLM Wiki pattern to Vannevar Bush's historical vision of the Memex. Discusses how LLMs resolve the bottleneck of active knowledge maintenance, detailing layout models, indexing processes, and scalable retrieval strategies for multi-agent environments.
- [Create Your AI Brain Today](https://saranfn.substack.com/p/create-your-ai-brain-today) - The final part of a structural context trilogy pinpointing why knowledge management setups fail at the content layer. Focuses on content architecture optimization, detailing how to engineer high-signal markdown nodes, construct type-safe frontmatter blocks for explicit entity tracking, and implement strict data compression filters to protect agent context windows from token bloat.
- [Evaluating OpenWiki with WikiBench (LangChain Blog)](https://www.langchain.com/blog/evaluating-openwiki-with-wikibench) - An evaluation
  overview introducing WikiBench, a benchmark running inside the Harbor framework to measure wiki usefulness for
  agents. Demonstrates that pairing a generated wiki with codebase access yields higher task correctness and lower
  token costs than querying raw source code alone.
- [Give Your AI Unlimited Updated Context](https://saranfn.substack.com/p/give-your-ai-unlimited-updated-context) - An operational architecture guide exploring decoupled, portable text vaults. Outlines the strategic benefits of maintaining plain text markdown knowledge graphs over proprietary, model-siloed memories, detailing how to utilize root configuration files (`CLAUDE.md`) and automated background agent loops to keep cross-functional context updated natively.
- [Inside the LLM Wiki Movement: Build Knowledge That Won't Betray You (Allen on AFFiNE Blog)](https://affine.pro/blog/llm-wiki) - A deep conceptual primer examining the LLM Wiki movement, contrasting the four core architectures (single-file, multi-file vault, code-based, and RAG-augmented), discussing hallucination mitigation via confidence tagging, and reviewing platform trade-offs.
- [Introducing OpenWiki Brains, general-purpose wiki memory for agents (LangChain Blog)](https://www.langchain.com/blog/introducing-openwiki-brains-general-purpose-wiki-memory-for-agents) - The official announcement of OpenWiki Brains, detailing how agents use flat-file local wikis as proactive long-term memory.
- [Karpathy shares 'LLM Knowledge Base' architecture (VentureBeat)](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an) - The foundational tech journalism coverage analyzing Andrej Karpathy's autonomous archive philosophy. Details the engineering advantages of substituting dense vector RAG with an evolving, AI-maintained local Markdown wiki to prevent context-limit lobotomies in developer prompt streams.
- [Karpathy's LLM Wiki as Agent Memory](https://aaif.io/blog/karpathys-llm-wiki-as-agent-memory/) - A conceptual framework published by the Agentic AI Foundation mapping the LLM Wiki pattern to cognitive agent memory architectures. Explains how directory boundaries transform flat markdown files into distinct functional memory layers—mapping schemas to procedural execution rules, logs to episodic records, and cross-linked entity directories to semantic graph memory.
- [Karpathy's LLM Wiki: A Knowledge Base That Compounds (AI Builder Club)](https://www.aibuilderclub.com/blog/karpathy-llm-wiki) - An architectural breakdown of the LLM Wiki pattern contrasting it with standard RAG pipelines, defining the three-layer structure and three operations.
- [Karpathy's LLM Wiki: The Complete Guide (Agentpedia Codes)](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file) - An exhaustive breakdown analyzing the three-layer architecture, comparing static compilation vs. traditional RAG, and detailing prompt configurations.
- [LLM Markdown Wiki: A Personal Second Brain Without the Maintenance (Kiryl Bahdanovich on WAVEPILLARS)](https://wavepillars.com/learn/ai/llm-markdown-wiki-knowledge-base/) - A conceptual guide detailing how an LLM-maintained markdown wiki cuts knowledge maintenance overhead. Explores the raw/wiki/schema architecture, Obsidian graph-based hierarchy reviews, Cursor agent sync workflows, and utilizing frontmatter-first agent searches to optimize token usage.
- [LLM Wiki: Karpathy's Idea for AI Knowledge Bases (Denser.ai)](https://denser.ai/blog/llm-wiki-karpathy-knowledge-base/) - An analysis of Karpathy's LLM Wiki pattern, reviewing top implementations, product principles, and RAG integration.
- [LLM Wiki: The Compounding Knowledge Base, Explained (Mikko Lehtimäki on Softlandia Blog)](https://softlandia.com/articles/llm-wiki-the-compounding-knowledge-base-explained) - A conceptual primer explaining how LLM Wikis function as self-updating knowledge bases for AI agents. Compares link-based traversal against vector RAG models, outlining the minimal operational structure (sources/, wiki/, index.md, and system instructions) needed to enable compounding context.
- [Personal Knowledge Management Is Missing a Step (Scribelet Blog)](https://scribelet.app/blog/personal-knowledge-management) - An article analyzing the lifecycle of personal knowledge management systems (Zettelkasten, PARA, digital gardens).
  Argues that standard pipelines neglect knowledge decay and outlines how automated agentic verification loops
  serve as a maintenance layer to keep flat-file notes grounded and accurate.
- [Pinecone Nexus: The Knowledge Engine for Agents (Pinecone Blog)](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/) - An announcement of Pinecone Nexus, a knowledge engine that compiles raw data into task-optimized markdown artifacts.
- [Self-Authoring LLM Knowledge Bases](https://www.ricardodecal.com/projects/self-authoring-llm-knowledge-base/) - A technical conceptualization extending the compilation loop to live developer conversations, transforming ephemeral terminal and editor interactions into structured, persistent memory.
- [The Benefits of Using an LLM Wiki for Your AI Chatbot (Nick Kirtley on 99helpers)](https://99helpers.com/blog/benefits-llm-wiki-for-your-ai-chatbot) - A conceptual breakdown outlining the structural advantages of using compiled Markdown wikis to ground AI chatbots, covering setup simplicity, response speed, contextual consistency, and cost metrics compared to vector RAG setups.
- [The Designer's LLM Wiki (Fanny on AI Product + Design)](https://medium.com/ai-product-design/the-designers-llm-wiki-fcf499354457) - An essay exploring the value of personal, queryable LLM Wikis for product designers. Highlights the challenge of design insights scattered across Figma, Notion, and Slack, proposing a markdown context layer to let models synthesize design learnings and onboarding flows across multi-product histories.
- [The Four Pillars of a Company Brain (Femke Plantinga on X)](https://x.com/femke_plantinga/status/2092918452423983363) - A post
  comparing nine different implementations to extract the four pillars of agent memory: gathering signals,
  remembering, dreaming & pruning (updating/purging knowledge), and retrieving & speaking.
- [The Goal is Curation, not Compilation (LLM Wiki) (Steven Thompson)](https://medium.com/a-voice-in-the-conversation/the-goal-is-curation-not-compilation-llm-wiki-6f90f829b15d) - An essay analyzing the tension
  between machine compilation and human curation in LLM Wikis. Argues that a knowledge vault should serve as a
  "biography of understanding" rather than a database, suggesting that humans must retain responsibility for weighing
  ideas and tracking perspective changes.
- [The Real Second Brain: An Autonomous Knowledge Engine](https://vasileioszografos.substack.com/p/the-real-second-brain-an-autonomous) - An architectural essay defining the paradigm shift from ephemeral chat interfaces to persistent, agent-driven local wikis. It details how flat-file markdown vaults serve as a deterministic long-term memory layer for autonomous daemons, allowing collaborative, human-in-the-loop knowledge compilation and state management.
- [The State of Agent Wikis (Mem0 Blog on X)](https://x.com/mem0ai/status/2079585032587694582) - An overview by the Mem0 team analyzing the emerging landscape of model-maintained markdown vaults.
- [Three Answers to Karpathy's Question: Google OKF, Tencent WeKnora, and LangChain OpenWiki (Bailing Zhang on LinkedIn)](https://www.linkedin.com/pulse/three-answers-karpathys-question-google-okf-tencent-weknora-zhang-l8f9c/) - A comparative primer examining three architectural responses to Karpathy's LLM Wiki pattern: Google's Open Knowledge Format (OKF) specification, Tencent's layout-aware WeKnora framework, and LangChain's OpenWiki engine. Explores how each manages persistent knowledge, document parsing, and agent memory.
- [What Is an LLM Knowledge Base? (Emily Winks on Atlan Blog)](https://atlan.com/know/what-is-an-llm-knowledge-base/) - A foundational primer defining the architecture and component layers of external LLM knowledge stores. Distinguishes between vector, graph, and context-window models (such as Karpathy's), diagnoses the main reasons enterprise RAG systems fail (lossy source audits, conflicting schemas), and outlines best practices for upstream metadata enrichment.
- [What Is an LLM Wiki — and Should You Build One? (Floatboat Blog)](https://floatboat.ai/blog/what-is-llm-wiki) - A high-level primer introducing the LLM Wiki concept, detailing the three-layer architecture, highlighting Farza's personal wiki case study, and suggesting lighter alternatives for solo operators.
- [What Is an LLM Wiki? A Simple Guide to Karpathy's Personal Knowledge System (Nick Kirtley on 99helpers)](https://99helpers.com/blog/what-is-an-llm-wiki) - An introductory conceptual guide explaining the core model of LLM Wikis, contrasting their pre-compiled markdown approach with vector-only RAG pipelines, and detailing formatting best practices (one-idea notes, header summaries).
- [What Is Andrej Karpathy's LLM Knowledge Base Architecture? The Compiler Analogy Explained (MindStudio Blog)](https://www.mindstudio.ai/blog/karpathy-llm-knowledge-base-architecture-compiler-analogy) - An architectural breakdown explaining the compiler analogy for LLM Wikis, comparing raw sources to source code.
- [What is LLM Wiki Pattern? Persistent Knowledge with LLM Wikis](https://medium.com/@tahirbalarabe2/what-is-llm-wiki-pattern-persistent-knowledge-with-llm-wikis-3227f561abc1) - A structural guide defining the core filesystem architecture and ingestion loops of the LLM Wiki pattern. Outlines the read/write boundaries between raw source directories and compiled wiki spaces, detailing a 5-step compilation pipeline and contrasting the pre-compiled text routing method against traditional single-pass vector RAG pipelines.
- [What Is the LLM Knowledge Base Index File? How Agents Navigate Without Vector Search (MindStudio Blog)](https://www.mindstudio.ai/blog/llm-knowledge-base-index-file-no-vector-search) - An article explaining the design, formatting, and structural benefits of using an index.md navigation map in LLM Wikis.
- [Your Personal Brain: A Practical Guide for Leaders, Practitioners, and Enthusiasts (Nufar Gaspar LinkedIn)](https://www.linkedin.com/pulse/your-personal-brain-practical-guide-leaders-nufar-gaspar-8oajf/) - A management playbook exploring how to establish a "dump-and-housekeep" maintenance cycle for agent memory.

### Comparative Analyses (Wiki vs. RAG)

*Deep technical comparisons, comparative benchmarks, and evaluations of compiled memory systems against standard vector RAG pipelines.*

- [Andrej Karpathy Killed RAG. Or Did He? The LLM Wiki Pattern (Mandar Karhade)](https://pub.towardsai.net/andrej-karpathy-killed-rag-or-did-he-the-llm-wiki-pattern-7824d876e790) - An architectural analysis comparing traditional vector RAG pipelines against the compiled, static LLM Wiki pattern.
- [Better Models Won’t Save Your Agent (Pinecone Blog)](https://www.pinecone.io/blog/introducing-nexus-knowledge-engine/) - A technical analysis on why vector search loops fail for agents, advocating for a pre-compiled context engineering layer.
- [Beyond RAG: How Andrej Karpathy's LLM Wiki Pattern Builds Knowledge That Actually Compounds (Plaban Nayak in Level Up Coding)](https://levelup.gitconnected.com/beyond-rag-how-andrej-karpathys-llm-wiki-pattern-builds-knowledge-that-actually-compounds-31a08528665e) - A conceptual breakdown of the compilation loop model in LLM Wikis. Explains why stateless RAG pipelines fail to accumulate learning over time, comparing vector search to an "amnesic assistant" and detailing the three-layer layout (raw, wiki, schema) required to support self-maintaining agent knowledge bases.
- [Beyond RAG: Knowledge That Compiles (Bailing Zhang on LinkedIn)](https://www.linkedin.com/pulse/beyond-rag-knowledge-compiles-bailing-zhang-vaumc/) - A conceptual primer examining the limits of stateless vector search and the necessity of compiled knowledge for complex agent behaviors. Reflects on a review of thirty-nine agent builds, showing that while plain RAG handles descriptive lookups, multi-step workflows require a structured, self-maintaining Markdown knowledge layer to prevent context decay.
- [From Agentic RAG to Compiled Knowledge: Why Karpathy's Wiki Idea Is Spreading (Dotzlaw Consulting)](https://dotzlaw.com/insights/ai-02-agentic-rag-to-compiled-knowledge/) - An architectural analysis of the industry convergence on compiled knowledge engines over expensive agentic RAG loops.
- [Karpathy's LLM Wiki Pattern: When Compiled Knowledge Beats RAG (Particula Tech)](https://particula.tech/blog/karpathy-llm-wiki-compiled-knowledge-vs-rag) - An architectural analysis contrasting runtime vector RAG pipelines against ahead-of-time LLM knowledge compilation. Explores how pre-compiled markdown structures eliminate chunk-boundary errors and embedding drift, proposing a hybrid enterprise architecture that routes stable core knowledge to a compiled wiki and volatile high-scale data to vector search.
- [LLM Wiki Is Not a RAG Replacement - It's a Synthesis-Time Decision (Ranjan Kumar on Personal Blog)](https://ranjankumar.in/llm-wiki-synthesis-time-decision-rag-agentic-memory) - An architectural deep-dive analyzing why the LLM Wiki pattern does not replace vector RAG, but rather shifts the synthesis timeline. Explains the difference between ingest-time synthesis (compiling) and query-time synthesis (interpreting), outlines the "Synthesis Horizon" scaling cliff, and proposes a stratified corpus model.
- [LLM Wiki vs RAG: The Karpathy Concept and Enterprise Reality (Emily Winks on Atlan Blog)](https://atlan.com/know/llm-wiki-vs-rag-knowledge-base/) - A comparative analysis of Karpathy's LLM Wiki approach against enterprise RAG systems. Discusses the trade-offs in token efficiency, access control, concurrency, and data freshness pipelines, outlining the additions (such as role-based permissions and transactional layers) needed to scale markdown-based memory vaults for team collaboration.
- [LLM Wiki: Understanding the New AI Knowledge Architecture (Dario Radečić on DataCamp Blog)](https://www.datacamp.com/blog/llm-wiki) - A conceptual primer contrasting traditional retrieval-first systems (vector RAG) with compilation-first systems (LLM Wikis), explaining the three-layer pipeline architecture, key tradeoffs (freshness, accuracy, maintenance, scalability), and real-world agent memory benefits.
- [Obsidian: Your AI Second Brain isn't Memory (Roan Brasil Monteiro)](https://medium.com/@roanmonteiro/obsidian-your-ai-second-brain-isnt-memory-and-here-s-the-architecture-that-actually-is-bf944929e144) - A deep-dive system design guide mapping out the engineering mechanics of an active knowledge compiler loop over passive vector RAG. Formulates why standard semantic search layers cause context decay, providing a clean blueprint for building deterministic, git-backed file topologies in plain Markdown.
- [RAG vs. Agent Memory vs. LLM Wiki: A Practical Comparison (visrow Medium)](https://medium.com/@visrow/rag-vs-agent-memory-vs-llm-wiki-a-practical-comparison-41a9a0dc4dec) - A comparative analysis of stateless vector RAG, stateful agent memory, and pre-compiled LLM Wikis.
- [RAG, LLM Wiki, Agentic Search: Differences, Costs and Use Cases (2026) (Pasquale Pillitteri)](https://pasqualepillitteri.it/en/news/1496/rag-llm-wiki-agentic-search-differences-costs-2026) - A comparative analysis of RAG, LLM Wikis, and agentic search architectures. Details their technical evolution from 2022 to 2026, compares build/operational cost structures ($15k–$200k for enterprise RAG/agents vs. $200–$500 compilation cost for wikis), and maps out specific enterprise use cases.
- [RAG, LLM Wiki, or Gbrain? How Your Agent Remembers Changes Everything (Yanli Liu on GOPUBBY)](https://ai.gopubby.com/rag-llm-wiki-or-gbrain-how-your-agent-remembers-changes-everything-56829e66725c) - A comparative architecture analysis contrasting traditional runtime RAG, compiled LLM Wikis, and Garry Tan's workflow-centric Gbrain framework to guide the choice of agent-optimized knowledge substrates.
- [Why Karpathy is Right: RAG is Dead, Long Live the Agentic Wiki (Epsilla Blog)](https://www.epsilla.com/blogs/karpathy-agentic-wiki-beyond-rag-enterprise-memory) - An enterprise analysis comparing flat-file Markdown wikis against database semantic graphs for corporate memory.
- [Wiki Memory (LangChain Blog)](https://www.langchain.com/blog/wiki-memory) - An architectural examination of the emerging wiki memory pattern, comparing file-based compilation against RAG loops.
- [Your RAG Has Amnesia — and Another Vector Store Won't Cure It (Roan Brasil Monteiro)](https://medium.com/@roanmonteiro/your-rag-has-amnesia-and-another-vector-store-wont-cure-it-8b1d1eb77470) - An article analyzing why
  traditional RAG pipelines fail to compile compounding knowledge. Proposes a persistent markdown memory layer
  inspired by the LLM Wiki pattern to support stateful context and trace provenance.

### Codebase and Developer Context

*Architectural articles exploring how to design, customize, and route codebase-specific context for AI coding agents.*

- [A Home for Personal Context (Duncan Davidson on O'Reilly Radar)](https://www.oreilly.com/radar/a-home-for-personal-context/) - An architectural essay on the hosting substrates and design principles of user-controlled agent memory. Analyzes the trade-offs of storing context vaults locally (flat-file Markdown/Git), on the web (REST/MCP over Cloudflare Workers), and on mobile devices (SwiftUI/iCloud), outlining seven core principles for durable, interoperable personal context.
- [Andrej Karpathy's Fix for LLM Memory Works on Code Too (Yanli Liu on Medium)](https://medium.com/ai-all-in/andrej-karpathys-fix-for-llm-memory-works-on-code-too-9a9e38b18b4e) - An article analyzing the extension of the LLM Wiki pattern to software repositories. Discusses compiling codebase structure into SQLite databases via tree-sitter AST parsing and exposing symbol relationship graphs to coding agents over MCP servers.
- [Build a Second Brain for Your AI Coding Agents (Rick Hightower on Spillwave)](https://pub.spillwave.com/build-a-second-brain-for-your-ai-coding-agents-create-self-improving-loops-and-master-graph-64a874a7ba88) - An architectural guide on structuring persistent codebase memory for coding agents. Details harness engineering, deterministic write boundaries, tiered context disclosure, and graph-based self-improving loops to eliminate decision re-litigation and quality collapse.
- [LLM Wiki vs RAG for Internal Codebase Memory: Which Approach Should You Use? (MindStudio Blog)](https://www.mindstudio.ai/blog/llm-wiki-vs-rag-internal-codebase-memory) - A comparative guide analyzing the tradeoffs between RAG and flat-file LLM Wikis for codebase memory and agent context routing.
- [OpenWiki 0.2 brings OKF to codebase documentation (LangChain Blog)](https://www.langchain.com/blog/openwiki-0-2-adds-okf-support) - The official announcement of OpenWiki 0.2, detailing its integration of the Open Knowledge Format (OKF) specification.
- [Your AI Agent Needs a Map: LLM Wiki vs README-Driven Documentation (Roman Dykyi on Medium)](https://medium.com/@dykyi.roman/your-ai-agent-needs-a-map-llm-wiki-vs-readme-driven-documentation-747e683c9ab4) - A comparative analysis examining how developers feed context to AI coding agents, contrasting project-mapping files (like README.md and CLAUDE.md) with compounding knowledge layers (LLM Wikis), and exploring token management, drift risks, and file-linking topologies.

### Digital Gardens and Public Notes

*Notes, digital gardens, and public wiki entries from personal knowledge bases detailing real-world implementations and critiques of the LLM Wiki pattern.*

- [LLM Wiki (DeveloPassion Digital Garden)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Wiki) - A digital garden
  note summarizing the LLM Wiki pattern. Covers the three-layer architecture, core operations (Ingest, Query, Lint),
  and outlines Steven Thompson's critique on compilation versus curation.
- [LLM Wiki (Kamenik Solutions)](https://kameniksolutions.com/garden/llm-wiki/) - A digital garden note summarizing the LLM Wiki pattern. Explains when to use compiled vaults over dynamic vector RAG, outlines the three core layers (raw sources, structured wiki, instruction schemas), and notes its trial as an organizational technique for agent-curated vaults.

### Scaling and Enterprise Systems

*Articles exploring scaling limits, context-window optimizations, concurrency, access governance, and enterprise architectures.*

- [Karpathy's LLM Wiki v2: What to Keep](https://theaioperator.io/p/karpathys-llm-wiki-v2-what-to-keep) - A critical architectural teardown outlining the evolution of the LLM Wiki design pattern. Details the necessary shift from manual workflows to parallel background agent pipelines, explains how to replace heavy index rewrites with vector mapping arrays, and demonstrates how to implement a targeted JSON pre-routing layer to keep API context costs minimal as local vaults grow past thousands of nodes.
- [LLM Wiki: The Self-Updating AI Knowledge Base (Tericsoft Blog)](https://www.tericsoft.com/blogs/llm-wiki) - A conceptual primer analyzing the scaling of the LLM Wiki pattern to enterprise teams, detailing the compute cost tradeoffs (compile-time vs. query-time RAG), scheduled linting loops, access governance, version control integration, and agent memory architectures.
- [Reimagining Karpathy's LLM Knowledge Base for enterprise teams (Christophe Pasquier on X)](https://x.com/Christophepas/status/2049855798226907502) - An architectural essay examining the requirements for adapting Karpathy's personal LLM knowledge base pattern to enterprise organizations, detailing multi-source automated ingestion, factual verification layers, and self-healing staleness detection.
- [The LLM Wiki at Scale: From Personal Research Tool to Production RAG (Michal Nasternak on Medium)](https://michalnasternak.medium.com/the-llm-wiki-at-scale-from-personal-research-tool-to-production-rag-247710a1284c) - An architectural analysis examining how to scale the LLM Wiki pattern to enterprise production. Details the bottlenecks of single index files once vaults grow past hundreds of pages, proposing session-level on-demand wiki compilation and per-user persistent knowledge layers to optimize synthesis quality, cost efficiency, and debuggability over traditional vector RAG.
- [The Missing Data Layer in LLM Knowledge Bases (Claudiu Dascalescu on Xata Blog)](https://xata.io/blog/llm-knowledge-bases) - An architectural primer proposing a dual-layer structure that pairs PostgreSQL (for transactional data/metrics) with a Markdown wiki (for qualitative context), detailing saved SQL queries, database branching, and agent skill configurations.
- [What Karpathy's LLM Wiki is Missing (And How to Fix It)](https://dev.to/penfieldlabs/what-karpathys-llm-wiki-is-missing-and-how-to-fix-it-1988) (Penfield Labs) - A deep architectural critique outlining solutions for token scaling limits in file-based context stores, featuring code patterns for semantic deduplication and pre-commit syntax hooks to protect structural integrity.

### Tutorials and Setup Guides

*Practical setup walkthroughs, implementation blueprints, and step-by-step guides for constructing personal vaults.*

- [Andrej Karpathy's LLM Wiki: Create your own knowledge base (Urvil Joshi on Medium)](https://medium.com/@urvvil08/andrej-karpathys-llm-wiki-create-your-own-knowledge-base-8779014accd5) - A step-by-step setup guide for building a personal LLM Wiki, outlining the three-layer vault architecture (raw sources, wiki nodes, and CLAUDE.md guidelines) managed via the Claude Code terminal agent and visualized in Obsidian.
- [Automate AI Second Brain (LLM Wiki Pattern) With Claude Code and Obsidian](https://medium.com/@tahirbalarabe2/automate-ai-second-brain-llm-wiki-pattern-with-claude-code-and-obsidian-38bc07c9214e) - An advanced guide transitioning the LLM Wiki pattern from interactive commands into an automated background operating system. Details how to orchestrate automated morning briefings and evening debriefs using Anthropic Cloud Routines, steer background agents with structured priority maps, and integrate live external context using Google Calendar and Gmail MCP servers.
- [Beyond Catastrophic Forgetting: How to Build an LLM Wiki for the Long Game (Part 1 of 3)](https://medium.com/artificial-intel-ligence-playground/beyond-catastrophic-forgetting-how-to-build-an-llm-wiki-for-the-long-game-8cea92f3868c) - A step-by-step guide to building a persistent, compounding markdown wiki using Claude Code and Obsidian on Windows. Outlines schema rules, ingestion pathways, and automated maintenance loops.
- [Beyond RAG: How I built a serverless AI LLM Wiki engine using OKF and AWS RODA (visrow Medium)](https://medium.com/@visrow/beyond-rag-how-i-built-a-serverless-ai-llm-wiki-engine-using-okf-and-aws-roda-straight-in-the-064a17c11489) - A guide on building a browser-based, serverless OKF wiki compiler using WebLLM and AWS Registry of Open Data.
- [Build an AI Second Brain (LLM Wiki Pattern) With Claude Code and Obsidian](https://medium.com/@tahirbalarabe2/build-an-ai-second-brain-llm-wiki-pattern-with-claude-code-and-obsidian-fc41cc213d50) - A practical implementation blueprint executing the LLM Wiki pattern using Claude Code as a vault maintainer. Demonstrates how to configure text-based slash commands (`/ingest`, `/query`, `/lint`, `/log`) to manage the boundary lines between raw input stores and compiled concept nodes while establishing hard citation tracking across file line coordinates.
- [Build an LLM Wiki for Your AI Agents with myKG and Obsidian](https://medium.com/@senol.isci/build-an-llm-wiki-for-your-ai-agents-b993af38d7c4) - An implementation guide introducing the open-source `myKG` library to enforce type-safe ontologies in local vaults. Demonstrates how to run automated pipeline integrations for Claude Code using terminal skill configurations, establish explicit source traceability records, and configure numerical confidence tracking metrics to eliminate silent agent hallucinations.
- [Building an LLM Wiki, Part 1 (Erik Evenson Blog)](https://www.erikevenson.net/building-an-llm-wiki-part-1.html) - A guide explaining how to implement the basic Karpathy pattern using Obsidian, its Local REST API, and Claude Code.
- [Building an LLM Wiki, Part 2 (Erik Evenson Blog)](https://www.erikevenson.net/building-an-llm-wiki-part-2.html) - An article detailing schema linting, staleness detection, contradiction handling, and search testing for LLM Wikis.
- [Compiling knowledge, not retrieving it (Roan Brasil Monteiro)](https://medium.com/@roanmonteiro/compiling-knowledge-not-retrieving-it-a-hands-on-deep-dive-into-llm-wiki-compiler-a495523a8085) - A code-level implementation guide detailing the software architecture of the `llm-wiki-compiler` engine. Walks through the step-by-step orchestration of a multi-model text compilation loop, local workspace linting rules, and inline source-provenance tracking without vector databases.
- [How Row-Bot Uses a Local Knowledge Graph for Private AI Memory (Syd Sachar)](https://x.com/SydSachar/status/2067205476421341647) - A technical guide explaining how Row-Bot compiles local-first memory into an Obsidian-compatible wiki graph.
- [How to Build a Second Brain You Can Actually Trust Using myKG and Obsidian (Senol Isci on Medium)](https://medium.com/@senol.isci/how-to-build-a-second-brain-you-can-actually-trust-52ac621188b7) - A guide addressing facts and hallucination risks when extracting knowledge graphs with LLMs. Introduces myKG configurations using confidence-scoring metrics, strict source attributions, pre-extraction schema validation gates, and tunable trust thresholds to build verifiable personal Obsidian wikis.
- [How to Build an AI Brain That Never Forgets](https://saranfn.substack.com/p/how-to-build-an-ai-brain-that-never) - A practical implementation blueprint detailing how to build an air-gapped, local Obsidian memory vault. Walks through extracting conversational data streams from proprietary web platforms, configuring root-level orchestration instructions (`CLAUDE.md`), and deploying background automation scripts to sync data sources and log daily workflow progress.
- [How to build an AI second brain that doesn't go stale (Scribelet Blog)](https://scribelet.app/blog/ai-second-brain-setup) - A guide adapting the CODE and PARA frameworks for AI workflows, highlighting knowledge decay, semantic auto-linking, and Model Context Protocol (MCP) integrations.
- [How to Build an LLM Knowledge Base (DAIR.AI)](https://academy.dair.ai/blog/how-to-build-an-llm-knowledge-base) - A practical workshop guide defining a standard local directory architecture and outlining repeatable agentic compiler patterns.
- [How to Build Karpathy's LLM Wiki: The Complete Guide to AI-Maintained Knowledge Bases (Dylan Boudro on Starmorph)](https://blog.starmorph.com/blog/karpathy-llm-wiki-knowledge-base-guide) - A comprehensive setup walkthrough detailing the three-layer LLM Wiki architecture, outlining the ingest/query/lint workflows, and providing a production-ready CLAUDE.md schema template for Obsidian and Claude Code integration.
- [How to Build Your Agentic Knowledge Base (after 16 months of running my own) (Chris Lettieri on Bits of Chris Substack)](https://bitsofchris.com/p/how-to-build-your-agentic-knowledge) - A practical implementation guide outlining a three-layer folder structure (inbox, notes, map) to let a knowledge vault taxonomy emerge organically, detailing the standard eight components of agentic vaults and the scaling progression path.
- [LLM Knowledge Bases (DAIR.AI)](https://academy.dair.ai/blog/llm-knowledge-bases-karpathy) - A detailed breakdown of the four-phase compilation pipeline (Ingest, Compile, Query, Lint) with architecture diagrams and implementation workflows.
- [LLM Wiki 1: Building a Minimal LLM Wiki (Ken Moriwaki)](https://medium.com/@ken.moriwaki/building-a-minimal-llm-wiki-19a2fb0e9ac7) - A three-part implementation series on building a minimal Markdown knowledge base and maintaining it with agents.
- [LLM Wiki 2: Visualising an LLM Wiki in Obsidian (Ken Moriwaki)](https://medium.com/@ken.moriwaki/visualising-an-llm-wiki-in-obsidian-0e9ec9a4fb04) - The second part of a practical series exploring how to visualize and inspect compiled Markdown wikis inside Obsidian.
- [LLM Wiki 3: From LLM Wiki to Agentic Knowledge Maintenance (Ken Moriwaki)](https://medium.com/@ken.moriwaki/from-llm-wiki-to-agentic-knowledge-maintenance-8a71500aabb9) - The third part of a series outlining how to transition static Markdown wikis to autonomous agentic maintenance workflows.
- [LLM Wiki for Notion: Building a Claude-Powered Second Brain with a 3D Knowledge Graph (IVGraph)](https://ivgraph.com/journal/second-brain-llm-notion-claude-code/) - A guide on building a Claude-powered LLM Wiki from Notion databases using MCP and 3D knowledge graph visualizations.
- [LLM Wiki Local (Local LLM) (Part 2 of 3)](https://medium.com/artificial-intel-ligence-playground/llm-wiki-local-locall-llm-part-2-88ecfa2cf6c2) - A tutorial on configuring a fully local-first LLM Wiki using llama.cpp and Opencode on Windows. Demonstrates manual environment wiring, setting up AGENTS.md instructions as standard operating procedures, and deploying custom scripting gates to manage local data compilations.
- [LLM Wiki Local: The Hybrid Engine and the PDF Bridge (Part 3 of 3)](https://medium.com/artificial-intel-ligence-playground/llm-wiki-part-3-the-hybrid-engine-and-the-pdf-bridge-2ece8d831b5f) - A tutorial on constructing a hybrid ingestion engine for local LLM Wikis on Windows. Focuses on resolving formatting issues with large PDF documents using a custom Python script (the PDF Bridge) and routing local traffic via the Bifrost gateway.
- [Standardizing Agent Memory: Building a Self-Updating Codebase Knowledge Graph with Google’s OKF (Udaykiran Estari on Medium)](https://medium.com/data-science-collective/stop-wasting-llm-tokens-building-a-self-updating-codebase-knowledge-graph-with-okf-20284060c1b1) - A configuration guide detailing how to build a git-hook-triggered pipeline to keep an OKF knowledge graph in sync. Demonstrates how to automatically compile, link, and lint repository context with every commit to serve pre-warmed context to agents.
- [Supercharging LLM Wiki with Knowledge Graphs: Build a Self-Evolving Research System](https://support.noduslabs.com/hc/en-us/articles/26724863249180-Supercharging-LLM-Wiki-with-Knowledge-Graphs-Build-a-Self-Evolving-Research-System) ([Video](https://www.youtube.com/watch?v=yYSTsKo8moU)) - A guide and video tutorial detailing how to integrate network analysis and knowledge graphs into an LLM Wiki. Uses InfraNodus and Obsidian to identify conceptual clusters, map structural gaps, and direct agents (via custom skills in Claude Code) to formulate research questions that resolve disconnected topics.
- [The Enterprise LLM Wiki: Scaling Karpathy's Pattern to Your Org (Falconer Guides)](https://falconer.com/guides/enterprise-llm-wiki-karpathy/) - A guide on scaling the LLM Wiki pattern to organizations, detailing tool-native ingestion and drift detection.
- [Turning Karpathy's LLM Wiki Idea into a Kiro Setup (AWS Builder Center)](https://builder.aws.com/content/3DDSTQuCtKJgJg0GMhAaaY9RTUj/turning-karpathys-llm-wiki-idea-into-kiro-setup) - A configuration guide detailing how to implement Andrej Karpathy's LLM Wiki pattern in the Kiro AI IDE. Explores configuring three-layer vault directories, defining system steering instructions, automating raw source ingestion via fileCreated event hooks, and running one-click health linting to prevent structural drift.
- [What Is Andrej Karpathy's LLM Wiki? How to Build a Personal Knowledge Base With Claude Code (MindStudio Blog)](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code) - A beginner-friendly tutorial for setting up a local Obsidian vault and querying it using the Claude Code terminal client.
- [Your Second Brain Is a Graveyard. Make It Agent Memory. (Decoding AI)](https://www.decodingai.com/p/llm-wiki-agent-memory) - A guide on building an AI Research OS memory layer to compile notes and web sources into a queryable wiki for agents.

### Case Studies and Retrospectives

*In-depth case studies, domain-specific retrospectives, and personal audits of active wiki setups in production.*

- [A Voice-First Extension of Karpathy's LLM Wiki (Kieran Adair)](https://medium.com/@kieran_adair/a-voice-first-extension-of-karpathys-llm-wiki-8aa61a38657a) - A case study outlining a voice-first
  ingestion pipeline for the LLM Wiki pattern. Details how to utilize mobile audio recordings, Whisper API
  transcriptions, and local LLM processing to transcribe spoken thoughts and automatically compile them into a
  structured Obsidian wiki.
- [Adding Quality Control to Andrej Karpathy's LLM Wiki (Mick Yates on Yatesweb)](https://www.yatesweb.com/adding-quality-control-to-andrej-karpathys-llm-wiki/) - A case study and methodology guide introducing a quality-control 'immune system' to an Obsidian LLM Wiki. Borrows from the NUSAP epistemic framework to implement a 5-column pedigree matrix (Provenance, Rigour, Coherence, Relevance Anchors, Claim Differentiation) in YAML frontmatter, ensuring agent ingestion loops distinguish rigorous peer-reviewed papers from unverified thought experiments.
- [An LLM wiki changed how I work (Casey Newton on Platformer)](https://www.platformer.news/karpathy-llm-wiki-journalism-productivity/) - A case study by tech journalist Casey Newton detailing his experience building a personal "beat wiki" inspired by Andrej Karpathy. Explores how using an LLM to process and synthesize source materials into a structured, self-updating Obsidian-compatible Markdown wiki serves as a valuable research assistant, streamlining beat reporting and productivity.

## `AGENTS.md`

# Repository Schema

- File Standard: All curated lists must reside in `README.md`.
- Line Formatting: Maximum 120 characters per line for prose.
- Link Standard: Strict awesome-lint Markdown conventions.


## `CONTRIBUTING.md`

# Contributing Guidelines

Thank you for taking the time to contribute to the Awesome LLM Wiki list! We prioritize high-signal curation to keep this repository incredibly valuable for the developer community.

## Submission Rules

- **Strict Curation:** We only accept resources directly related to static LLM knowledge base compilation, architectural blueprints, or specialized agent skill schemas. Generic RAG libraries or basic note-taking apps will be excluded.
- **Formatting Standard:** All additions to the main list must strictly follow the `-[Name](URL) - Concise description.` token structure.
- **Style Rules:** Resource descriptions must begin with a capital letter and terminate with a period. Avoid promotional hyperbole, marketing buzzwords, or subjective claims.
- **Alphabetical Order:** Ensure your resource is inserted into the appropriate section in strict alphabetical order by its Project Name.

## How to Submit

1. Fork this repository to your own GitHub account.
2. Create a descriptive topic branch for your asset.
3. Verify your syntax locally using the validation workspace: `npm run test`.
4. Submit a clear Pull Request targeting the primary main branch.

## `package.json`

{
  "name": "awesome-llm-wiki",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "npx awesome-lint README.md"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "devDependencies": {
    "awesome-lint": "^2.3.0"
  }
}
