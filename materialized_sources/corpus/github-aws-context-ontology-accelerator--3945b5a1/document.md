# Repository semantic capsule: aws/context-ontology-accelerator

- Commit: `e265573df26eefd6a8b51683d7555ceffbe26ab7`
- Default branch: `main`
- Description: aws/context-ontology-accelerator
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# ✦ Context Ontology Accelerator

An open-source semantic context layer for AWS that combines knowledge graphs, formal ontologies, and rule-based systems with modern AI — enabling agents to retrieve context, validate it against business logic, and determine correct actions.

## Architecture

The system follows a **Scan → Model → Serve** workflow:

- **Scan** — Connect data sources, discover schemas, enrich metadata, ingest unstructured documents
- **Model** — Induce and manage ontologies, define metrics, build a unified semantic graph
- **Serve** — Query via SPARQL federation (VKG), traverse the knowledge graph, serve context to AI agents via MCP

Access is governed by namespace isolation and role-based access control: namespace-scoped roles (owner, maintainer, data-steward, data-analyst) plus **platform-level roles** (`platform-admin`, `platform-viewer`) that apply across all namespaces. See the [control-plane docs](packages/control-plane/README.md) for the grants and authorization model.

## Quick Start

### Prerequisites

- Python 3.12, Node.js 22+, Docker
- [pnpm](https://pnpm.io/) (Node package manager — installed via `mise` or `npm install -g pnpm`)
- Java 17+ and Gradle (for Smithy codegen)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Setup

> **Use a release, not the tip of `main`.** We recommend starting from a tagged
> release — [github.com/aws/context-ontology-accelerator/releases](https://github.com/aws/context-ontology-accelerator/releases).
> `main` tracks ongoing development.

```bash
# Clone at the latest release tag (replace <tag> with a release from the link above)
git clone --branch <tag> https://github.com/aws/context-ontology-accelerator.git
cd context-ontology-accelerator

make setup      # install Python + CDK TypeScript dependencies
make format     # auto-format code
make lint       # check linting
make test       # run unit tests
```

**Full developer guide:** [external-docs/content/getting-started.md](external-docs/content/getting-started.md)

## Repository Structure

```
semantic-context/
├── models/              # Smithy API models (source of truth for API contracts)
├── smithy-generated/    # Auto-generated from Smithy (OpenAPI, Python interfaces, TS client)
├── infra/               # AWS CDK (TypeScript) — foundation + per-service stacks
├── packages/
│   ├── control-plane/           # Control Plane APIs
│   ├── data-layer/              # Data Layer APIs (query, retrieval, traversal)
│   ├── sources/                 # Unified data source ingestion (database + documents)
│   ├── ontology-engine/         # Ontology induction, reasoning (HermiT/ELK)
│   ├── metric-service/          # Metric authoring and resolution
│   ├── vkg/                     # Virtual Knowledge Graph (Ontop)
│   ├── mcp-server/              # MCP tools for AI agents
│   ├── context-manager/         # Serve layer Context Manager (query orchestration, upstream clients)
│   └── web-app/                 # React + Cloudscape frontend
├── libs/common/         # Shared Python config, logging, exceptions
├── libs/ts-shared/      # Shared TypeScript interfaces and constants
├── connectors/          # Athena federation connectors: toolkit, reference connector, Databricks
├── scripts/             # CI-agnostic build/test/deploy scripts
└── external-docs/       # Published documentation (getting-started, deployment guides)
```

## Tech Stack

| Layer                  | Technology                                               |
| ---------------------- | -------------------------------------------------------- |
| Languages              | Python 3.12, TypeScript                                  |
| API Contracts          | Smithy → OpenAPI + Python interfaces + TypeScript client |
| IaC                    | AWS CDK (TypeScript)                                     |
| Frontend               | React + Cloudscape Design System                         |
| Package Management     | uv (Python), pnpm (TypeScript)                           |
| Monorepo Orchestration | Nx                                                       |
| Testing                | pytest (unit + integ)                                    |
| Linting                | ruff, mypy (strict)                                      |
| Codegen                | Smithy CLI (Java 17 + Gradle)                            |

## Contributing

This repository is published as a read-only mirror. We are not accepting pull requests at this time. You are welcome to report bugs and share feedback through GitHub Issues. See [CONTRIBUTING.md](CONTRIBUTING.md) for details including direction for Amazon employees.

## External Dependencies

This package depends on and may incorporate or retrieve a number of third-party
software packages (such as open source packages) at install-time or build-time
or run-time ("External Dependencies"). The External Dependencies are subject to
license terms that you must accept in order to use this package. If you do not
accept all of the applicable license terms, you should not use this package. We
recommend that you consult your company’s open source approval policy before
proceeding.

Provided below is a list of External Dependencies and the applicable license
identification as indicated by the documentation associated with the External
Dependencies as of Amazon's most recent review.

THIS INFORMATION IS PROVIDED FOR CONVENIENCE ONLY. AMAZON DOES NOT PROMISE THAT
THE LIST OR THE APPLICABLE TERMS AND CONDITIONS ARE COMPLETE, ACCURATE, OR
UP-TO-DATE, AND AMAZON WILL HAVE NO LIABILITY FOR ANY INACCURACIES. YOU SHOULD
CONSULT THE DOWNLOAD SITES FOR THE EXTERNAL DEPENDENCIES FOR THE MOST COMPLETE
AND UP-TO-DATE LICENSING INFORMATION.

YOUR USE OF THE EXTERNAL DEPENDENCIES IS AT YOUR SOLE RISK. IN NO EVENT WILL
AMAZON BE LIABLE FOR ANY DAMAGES, INCLUDING WITHOUT LIMITATION ANY DIRECT,
INDIRECT, CONSEQUENTIAL, SPECIAL, INCIDENTAL, OR PUNITIVE DAMAGES (INCLUDING
FOR ANY LOSS OF GOODWILL, BUSINESS INTERRUPTION, LOST PROFITS OR DATA, OR
COMPUTER FAILURE OR MALFUNCTION) ARISING FROM OR RELATING TO THE EXTERNAL
DEPENDENCIES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, EVEN
IF AMAZON HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. THESE LIMITATIONS
AND DISCLAIMERS APPLY EXCEPT TO THE EXTENT PROHIBITED BY APPLICABLE LAW.

| External Dependency | License | Source |
| ------------------- | ------- | ------ |
| owlready2 | LGPL-3.0 | https://pypi.org/project/owlready2/ |

## License

This project is licensed under the Apache License 2.0 — see [LICENSE](LICENSE) for details.

## `CONTRIBUTING.md`

# Contributing to Context Ontology Accelerator

Thank you for your interest in Context Ontology Accelerator!

## Reporting Bugs/Feature Requests

At this time, we are not accepting pull requests for this repository and it is instead maintained by an AWS development team.

However, we welcome you to use the GitHub issue tracker to report bugs or suggest features.

- **Bug reports:** Open a [GitHub issue](https://github.com/aws/context-ontology-accelerator/issues) describing what you expected, what happened, and how to reproduce it.
- **Feature requests and feedback:** Open a [GitHub issue](https://github.com/aws/context-ontology-accelerator/issues) describing your use case.

We read every issue and use them to shape the roadmap. We may accept pull requests in the future.

## Code of Conduct

This project has adopted the [Amazon Open Source Code of Conduct](CODE_OF_CONDUCT.md).

## Security issue notifications

Do not report security issues through GitHub Issues. Follow the process in [SECURITY.md](SECURITY.md).

## Licensing

See the [LICENSE](LICENSE) file for our project's licensing. We will ask you to confirm the licensing of your contribution.

## Amazon employees

If you are an Amazon employee, contribute through the internal project following the contribution guidance at group level. See [DEVELOPMENT.md](DEVELOPMENT.md) for the monorepo build and development workflow.

## `Makefile`

.PHONY: setup generate format lint test test-unit test-integ build load-test load-test-slow load-test-teardown deploy-dev deploy-serve deploy-example-connector destroy-dev preflight docs web-dev vkg-dev version version-check

setup: generate
	./scripts/setup-dev.sh

generate:
	./scripts/smithy-generate.sh

format:
	uv run ruff format .
	uv run ruff check --fix .
	pnpm nx run-many -t format

## Propagate the repo-root VERSION into every package manifest. Bump VERSION,
## then run this — never edit a package's version by hand.
version:
	@python3 scripts/sync_version.py

## Fail if any package manifest has drifted from VERSION (runs as part of lint).
version-check:
	@python3 scripts/sync_version.py --check

lint: version-check
	pnpm nx run-many -t lint

test: test-unit

## Per-package unit tests (Nx) plus the repo-level suite in tests/unit, which
## covers cross-package concerns (version sync, NOTICE generation, doc accuracy)
## and belongs to no single Nx project.
test-unit:
	pnpm nx run-many -t test
	uv run pytest tests/unit -q
	uv run pytest scripts/agents -q

coverage:
	@python3 scripts/coverage-summary.py

## Run integration tests against all packages with deployed stacks.
## Optional env vars (all auto-resolved if not set):
##   AWS_DEFAULT_REGION  — AWS region (default: us-east-1)
##   ENV_NAME            — environment name (default: dev)
##   INTEG_SECRET_ARN    — skip user provisioning, use this Secrets Manager ARN
##   API_ENDPOINT        — skip CloudFormation lookup, use this API Gateway URL
##   INTEG_NAMESPACE_ID  — reuse an existing namespace (skip create)
test-integ:
	@if ls packages/*/tests/integ/ >/dev/null 2>&1; then \
		uv run pytest packages/*/tests/integ/ -m integ -v --tb=short --import-mode=importlib; \
	else echo "⚠ integ tests not available (stripped from public mirror)"; fi

## Load test: validates the pipeline at scale (50 → 50k tables).
## `make load-test` runs the non-billable smoke rung only ('not slow').
## `make load-test-slow RUNG=500` opts into billable 500+ rungs.
## Crash recovery: make load-test-teardown RUN_ID=<id>
load-test:
	@if [ -d tests/integ/load ]; then \
		uv run pytest tests/integ/load/ -q -m "not slow" --rung $(or $(RUNG),50); \
	else echo "⚠ load tests not available (stripped from public mirror)"; fi

load-test-slow:
	@if [ -d tests/integ/load ]; then \
		uv run pytest tests/integ/load/ -q -m slow --rung $(or $(RUNG),500); \
	else echo "⚠ load tests not available (stripped from public mirror)"; fi

load-test-teardown:
	@if [ -f tests/integ/load/teardown_orphan.py ]; then \
		uv run python tests/integ/load/teardown_orphan.py $(RUN_ID); \
	else echo "⚠ load tests not available (stripped from public mirror)"; fi
build: notice
	pnpm nx run-many -t build

## Regenerate the root NOTICE (third-party attribution, ORR PAK-A-3) from the
## resolved environment. Run as part of `make build`; commit the result if it
## changes so the checked-in NOTICE stays current with the dependency set.
notice:
	uv run python -m scripts.supply_chain.cli notice

preflight:
	./scripts/preflight-deploy.sh

deploy-dev:
	./scripts/deploy.sh dev

deploy-serve:
	./scripts/deploy-serve.sh dev

## Deploy the example Athena federation connector (connectors/) into a dev account,
## giving integration tests a federated source to query. Separate from deploy-dev on
## purpose: it stands in for something a customer deploys in their own account, and it
## must run AFTER COA — it reads COA's serve and discovery role ARNs from SSM.
## Optional env vars: SCL_PREFIX (default: coa — matches the CDK app),
## FUNCTION_NAME_PREFIX (default <prefix>-<env>-), EXAMPLE_BULK_ROWS /
## EXAMPLE_BULK_ROW_BYTES to size the fixture past Athena's 6 MB limit and exercise spill.
deploy-example-connector:
	./scripts/deploy-example-connector.sh dev

## Tear down all dev stacks in one command. Deletes AgentCore Runtimes,
## waits for their ENIs to detach (and stops if they do not),
## deletes VKG's ECS services, force-deletes the DataZone domain (cascades
## to RETAINed child resources CFN can't clear on its own), deletes every connector
## stack (separate CDK apps, so `cdk destroy --all` never sees them), then runs
## `cdk destroy --all` and verifies no stacks remain (see #660, #661, #707).
## Optional env vars: SCL_PREFIX (default: coa — matches the CDK app), SCL_DESTROY_YES=1 to skip
## the confirmation prompt (e.g. in CI), and the wait budgets
## SCL_ENI_WAIT_MAX_SECONDS (600), SCL_ECS_WAIT_MAX_SECONDS (300),
## SCL_DOMAIN_WAIT_MAX_SECONDS (300), SCL_CLOUDMAP_WAIT_MAX_SECONDS (180),
## SCL_CONNECTOR_DELETE_WAIT_MAX_SECONDS (600).
destroy-dev:
	make generate
	pnpm install
	./scripts/destroy.sh dev

docs:
	@if [ -d docs ]; then cd docs && mkdocs serve; \
	else echo "⚠ docs/ not available (stripped from public mirror); see external-docs/"; fi

web-dev:
	cd packages/web-app && pnpm install && pnpm dev

vkg-dev:
	docker build -t vkg-local packages/vkg/
	docker run --rm -p 8080:8080 -e ONTOLOGY_BUCKET=local -e NAMESPACE=default -e VERSION=latest vkg-local

## `package.json`

{
  "name": "coa",
  "private": true,
  "scripts": {
    "build": "nx run-many -t build",
    "test": "nx run-many -t test",
    "lint": "nx run-many -t lint",
    "format": "nx run-many -t format"
  },
  "devDependencies": {
    "nx": "20.8.0",
    "pnpm": "10.34.5"
  },
  "version": "0.3.1"
}

## `pyproject.toml`

[project]
name = "coa"
# Single source of truth is the repo-root VERSION file. Do not edit by hand —
# bump VERSION and run `make version` (verified by `make lint`).
version = "0.3.1"
description = "Context Ontology Accelerator for AWS"
requires-python = ">=3.12"
license = {text = "Apache-2.0"}

[dependency-groups]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
    "pytest-cov>=6.0",
    "pytest-xdist>=3.0",
    "ruff>=0.8",
    "mypy==1.20.1",
    "types-requests>=2.32.0",
    "types-PyYAML>=6.0",
    "boto3-stubs>=1.35",
    "moto[dynamodb,sqs]>=5.0",
    # Real-PDF unit tests for the sources preprocessing module (parse + render)
    "pypdfium2>=4.30.0",
    "pillow>=10.4.0",
]

[tool.uv.workspace]
members = [
    "packages/control-plane",
    "packages/context-manager",
    "packages/data-layer",
    "packages/ontology-engine",
    "packages/metric-service",
    "packages/vkg",
    "packages/mcp-server",
    "packages/sources",
    "libs/common",
    "smithy-generated/control-plane-python-server",
    "smithy-generated/data-layer-python-server",
]

[tool.pytest.ini_options]
pythonpath = ["."]
asyncio_mode = "auto"
markers = [
    "unit: Unit tests",
    "integ: Integration tests",
    "security: Security integration tests (authentication, authorization, input validation, SQL firewall)",
    "slow: Billable load-test rungs (500+) — manual only",
    # Also registered in packages/sources/pyproject.toml, which is the rootdir nx
    # uses. Declared here too so running the trees together (a common local
    # invocation) does not warn about an unknown mark.
    "real_glue_ownership: Opt out of the sources conftest's Glue ownership stub and exercise the real check",
]

[tool.mypy]
plugins = ["pydantic.mypy"]
# Print a traceback on mypy internal errors so transient crashes (e.g. under
# concurrent `nx run-many` lint) are diagnosable instead of just emitting the
# generic "INTERNAL ERROR" banner with no location.
show_traceback = true

[tool.coverage.run]
source = ["packages", "libs"]
omit = [
    "**/tests/**",
    "**/__pycache__/**",
    "**/demo/**",
]

[tool.coverage.report]
show_missing = true
skip_empty = true

[tool.coverage.html]
directory = "htmlcov"
