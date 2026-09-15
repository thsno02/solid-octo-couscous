# Repository semantic capsule: terminusdb/terminusdb

- Commit: `57f2093baeafd65e16004e84b7b58e0c5cf72858`
- Default branch: `main`
- Description: terminusdb/terminusdb
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<img
  src="https://github.com/terminusdb/terminusdb-web-assets/blob/master/readmes/terminusdb/TerminusDB-Logo-Colour_3.png"
  alt="TerminusDB Logo"
  width="30%"
  align="center"
/>

---

[![Native Build](https://github.com/terminusdb/terminusdb/actions/workflows/native-build.yml/badge.svg?branch=main&event=push)](https://github.com/terminusdb/terminusdb/actions/workflows/native-build.yml)
[![Docker Build](https://github.com/terminusdb/terminusdb/actions/workflows/docker-images-publish.yml/badge.svg?branch=main)](https://github.com/terminusdb/terminusdb/actions/workflows/docker-images-publish.yml)

[![Issues](https://img.shields.io/github/issues/terminusdb/terminusdb)](https://github.com/terminusdb/terminusdb/issues)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Project Overview (Updated May 2026)

**TerminusDB is a distributed database with a collaboration model — git for data.**

If you find this project useful, please consider **starring the repo** ⭐

TerminusDB allows you to link JSON and JSON-LD documents in a semantic knowledge graph through a powerful [document API](https://terminusdb.org/docs/document-insertion). It's designed as a system of record, making data management collaborative, versioned, and queryable.

Now with new maintainers and an enterprise version. 

### Key Features

- **Revision Control**: Commits for every update — track changes over time
- **Diff**: Differences between commits can be interpreted as patches between states
- **Push/Pull/Clone**: Communicate diffs between nodes using familiar git-like operations
- **Time-Travel Queries**: Query any state of the database at any commit
- **Document + Knowledge Graph**: Link JSON documents in a knowledge graph
- **Multimodal**: Support for REST API, GraphQL, WOQL and with Closed World RDF
- **Goal seeking**: Built in unification, path queries, and a datalog logic engine

### What's New in Version 12

[TerminusDB 12](https://github.com/terminusdb/terminusdb/releases/tag/v12.0.5) features performance, stability and precision provided by the new [DFRNT](https://dfrnt.com?utm_source=github_terminusdb) maintainers. Now engineered for industrial and financial use cases with high precision math, temporal reasoning, and stability under load. Version 12 includes:

- **[Arbitrary Precision xsd:decimal]()**: Arbitrary rational precision xsd:decimal mathematics, including high precision JSON decimals over the wire for JSON, GraphQL and WOQL, see [ISO/IEC 21778:2017](https://www.iso.org/standard/71616.html)
- **[Allen Integer Algebra and Temporal Reasoning](https://terminusdb.org/docs/woql-interval-algebra/)**: Reason about ISO8601 date, time and durations with high precision rational math
- **[Range Queries over Succinct Data](https://terminusdb.org/docs/woql-triple-slice/)**: Extremely fast range queries with constant time retrieval over arbitrary size ordered data, which is great for knowledge graph processing over timestamp, numeric, and interval ranges; with strong temporal reasoning and classification
- **[ISO8601 Allen Interval Algebra](https://terminusdb.org/docs/woql-interval-algebra/)**: Support for temporal reasoning and storage of XSD time datatypes including temporal interval classification, storage and life cycle management with datalog reasoning
- **[JSON Git-for-Data (Linked Data)](https://terminusdb.org/docs/git-for-data-reference/)**: Git for data for JSON, JSON-LD, XML and Turtle documents with schema control (and also for deduplicated schemaless JSON documents)
- **[REST API](https://terminusdb.org/docs/rest-api)**: Use REST API as a proper graph query language with deep link discovery, path queries and linked data
- **[GraphQL Support](https://terminusdb.org/docs/graphql-basics)**: Use GraphQL as a proper graph query language with deep link discovery and path queries
- **[WOQL Datalog](https://terminusdb.org/docs/what-is-datalog)**: Use WOQL as a goal-seeking problem-solving toolbox, complete with triples across and within documents, path queries and variables unification
- **[Schema Constraints](https://terminusdb.org/docs/schema-reference-guide/)**: Use schema constraints to enforce data quality and consistency, including for advanced typing
- **`@unfoldable` Documents**: Unfold subdocuments within a frame to add all relevant data in one place
- **`@metadata` Support**: Include additional metadata in document frames, including Markdown-formatted data

## Getting Started

The easiest way to install TerminusDB as a developer is by following the [10-minutes docker getting started manual](https://terminusdb.org/docs/get-started/) with the latest [Docker TerminusDB Image](https://hub.docker.com/r/terminusdb/terminusdb-server). It can be installed locally using [Snap](https://snapcraft.io/terminusdb) as both git-for-data client and server to perform push and pull. Docker brings the server component, and snap the ability to try TerminusDB on the command line, for example for ML/Ops and AI use cases requiring deterministic symbolic AI processing.

For deployments, copy the docker-compose.yml file from the repository. For a complete modeller user interface, create an account for the [DFRNT Studio](https://studio.dfrnt.com) which can also be used to model TerminusDB on localhost! There is still the possibility to run the now deprecated (buggy) dashboard, by following a [the instructions for the TerminusDB dashboard](https://terminusdb.org/docs/dashboard).

1. Add the following to a `.env` file in the source directory:

```shell
# Database administrator's password (required)
TERMINUSDB_ADMIN_PASS=

```

Notes:
 * TERMINUSDB_ADMIN_PASS is mandatory and must be set.


1. `docker compose up`

You should be able to view TerminusDB running by default at `localhost:6363`

> If you're installing TerminusDB on Windows with Docker, follow the comprehensive guide for [TerminusDB on Windows with Docker]([https://dfrnt.com/blog/2023-02-25-run-terminusdb-on-windows-with-docker/](https://terminusdb.org/docs/install-terminusdb-docker-windows/)).

You can also install TerminusDB from [Source Code](https://terminusdb.org/docs/install-terminusdb-from-source-code).

## Usage

### Quick Start with CLI

Once installed, you can start using TerminusDB immediately. Here's a simple example creating a person with friends (or use the [Manual and more in-depth 15-minutes Getting Started Guide](https://terminusdb.org/docs/first-15-minutes/)):

```shell
terminusdb db create admin/example1
terminusdb doc insert --graph_type=schema admin/example1 <<EOF
{ "@id" : "Person",
  "@type" : "Class",
  "name" : "xsd:string",
  "occupation" : "xsd:string",
  "friends" : { "@type" : "Set",
                "@class" : "Person" }}
EOF
terminusdb doc insert admin/example1 --message='adding Gavin' <<EOF
{ "@type" : "Person","name" : "Gavin", "occupation" : "Coder"}
EOF
```

### Client Libraries

TerminusDB provides official client libraries for multiple languages:

- 🐍 **[Python Client (v12)](https://pypi.org/project/terminusdb/)**: Full-featured Python library for TerminusDB
- 🌐 **[JavaScript Client (v12)](https://www.npmjs.com/package/terminusdb)**: Browser and Node.js support
- 🦀 **[Rust Client](https://github.com/ParapluOU/terminusdb-rs)**: Full-featured Rust library for TerminusDB, community contribution
- 🔮 **[Elixir Client](https://hex.pm/packages/terminusdb_client)**: An idiomatic Elixir client, community contribution


## Documentation

Full documentation is available at **[https://terminusdb.org/docs](https://terminusdb.org/docs/get-started-with-terminusdb/)**.

### Key Resources

- **[What is TerminusDB](https://terminusdb.org/docs/terminusdb-explanation/)**: Why TerminusDB is a unique Graph Database
- **[Getting Started Guide](https://terminusdb.org/docs/get-started/)**: Complete onboarding tutorial
- **[Document API](https://terminusdb.org/docs/document-insertion)**: Working with JSON documents
- **[GraphQL Guide](https://terminusdb.org/docs/graphql-basics)**: Query your knowledge graph with GraphQL
- **[WOQL](https://terminusdb.org/docs/what-is-datalog/)**: Web Object Query Language fundamentals
- **[Release Notes](docs/RELEASE_NOTES.md)**: Latest changes and version history
- **[TerminusDB Enterprise]()**: Full JSON-LD, Turtle, and RDF/XML documents, enterprise features, very fast commit history queries, higher write performance, clustering, API for data product backup and restore (beyond command line tools) 

Found an issue in the docs? Please [open an issue or pull request](https://github.com/dfrnt-labs/terminusdb-docs-static) in our documentation repo or here.

## Community

Come visit us on **[Discord](https://discord.gg/yTJKAma)** to:

- Ask questions and get help
- Share your projects and use cases
- Contribute to discussions
- Stay updated on the latest developments

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### How to Contribute

1. **Fork the repository** and create your feature branch
2. **Run tests** to ensure everything works: `make dev && ./terminusdb test`
3. **Write clear commit messages** with descriptive titles
4. **Submit a Pull Request** to the main branch

### Development Setup

Quick start for contributors:

```bash
# Clone your fork
git clone git@github.com:[your_username]/terminusdb.git
cd terminusdb

# Build the project
make dev

# Start test server
./tests/terminusdb-test-server.sh start

# Run tests
npx mocha tests/test/*.js
```

For detailed development instructions, coding conventions, and testing guidelines, see **[CONTRIBUTING.md](docs/CONTRIBUTING.md)**.

### Reporting Issues

Found a bug? Have a feature request? Please [open an issue](https://github.com/terminusdb/terminusdb/issues) using the bug template, with:

- Clear description of the problem or suggestion
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Your environment details (OS, TerminusDB version)

## License

TerminusDB is licensed under the **Apache License 2.0**.

You may obtain a copy of the license at: http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## `Dockerfile`

# syntax=docker/dockerfile:1.3

# Community-only Docker build.
# Set the swipl version by argument (see Makefile for the default!)
ARG SWIPL_VERSION=10.0.2
ARG SKIP_TESTS=false

# Minimal SWI-Prolog
FROM swipl:${SWIPL_VERSION} AS swipl_minimal
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates

# Install the SWI-Prolog pack dependencies.
FROM swipl_minimal AS pack_installer
RUN set -eux; \
    BUILD_DEPS="git curl build-essential make libssl-dev \
    pkg-config clang ca-certificates m4 libgmp-dev \
    protobuf-compiler libprotobuf-dev"; \
    apt-get update; \
    apt-get install -y --no-install-recommends ${BUILD_DEPS}; \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app/pack
COPY distribution/Makefile.deps Makefile
RUN make

# Install Rust. Prepare to build the Rust code.
FROM swipl_minimal AS rust_builder_base
ARG CARGO_NET_GIT_FETCH_WITH_CLI=true
RUN set -eux; \
    BUILD_DEPS="git build-essential curl clang ca-certificates m4 libgmp-dev protobuf-compiler libprotobuf-dev libssl-dev pkg-config"; \
    apt-get update; \
    apt-get install -y --no-install-recommends ${BUILD_DEPS}; \
    rm -rf /var/lib/apt/lists/*
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y --profile minimal
ENV PATH="/root/.cargo/bin:${PATH}"
# Initialize the crates.io index git repo to cache it.
RUN (cargo install lazy_static 2> /dev/null || true) && (cargo install cargo-swipl || true)
WORKDIR /app/rust
COPY distribution/Makefile.rust Makefile
COPY src/rust src/rust/

# Build the community dylib.
FROM rust_builder_base AS rust_builder
ARG CARGO_NET_GIT_FETCH_WITH_CLI=true
ARG SKIP_TESTS=false
RUN make DIST=community && ([ "$SKIP_TESTS" = "true" ] || (cd src/rust && cargo swipl test --release))

# Copy the packs and dylib. Prepare to build the Prolog code.
FROM pack_installer AS base
RUN set -eux; \
    RUNTIME_DEPS="make openssl binutils ca-certificates"; \
    apt-get update; \
    apt-get upgrade -y; \
    apt-get install -y --no-install-recommends ${RUNTIME_DEPS}; \
    rm -rf /var/cache/apt/*; \
    rm -rf /var/lib/apt/lists/*
ARG TERMINUSDB_GIT_HASH=null
ENV TERMINUSDB_GIT_HASH=${TERMINUSDB_GIT_HASH}
ARG TERMINUSDB_JWT_ENABLED=true
ENV TERMINUSDB_JWT_ENABLED=${TERMINUSDB_JWT_ENABLED}
WORKDIR /app/terminusdb
COPY distribution/init_docker.sh distribution/
COPY distribution/Makefile.prolog Makefile
COPY src src/
COPY --from=rust_builder /app/rust/src/rust/librust.so src/rust/

# Build the community executable.
FROM base AS base_community
ARG SKIP_TESTS=false
COPY --from=rust_builder /app/rust/src/rust/librust.so src/rust/
RUN set -eux; \
    make DIST=community; \
    [ "$SKIP_TESTS" = "true" ] || make test

FROM swipl_minimal AS min_community
COPY --from=base_community /app/terminusdb/terminusdb /app/terminusdb/

FROM min_community
COPY --from=base_community /app/terminusdb/terminusdb /app/terminusdb/
COPY --from=base_community /app/terminusdb/src/terminus-schema /app/terminusdb/src/terminus-schema/
COPY --from=base_community /app/terminusdb/distribution/init_docker.sh /app/terminusdb/init_docker.sh

RUN set -eux; \
    RUNTIME_DEPS="make openssl binutils ca-certificates"; \
    apt-get update; \
    apt-get upgrade -y; \
    apt-get install -y --no-install-recommends ${RUNTIME_DEPS}; \
    rm -rf /var/cache/apt/*; \
    rm -rf /var/lib/apt/lists/*
COPY --from=pack_installer /usr/share/swi-prolog/pack/tus /usr/share/swi-prolog/pack/tus

WORKDIR /app/terminusdb
RUN mkdir -p storage \
    && chown -R 1000:1000 storage
ENV TERMINUSDB_PLUGINS_PATH=${TERMINUSDB_PLUGINS_PATH:-/plugins}
COPY docker/plugins/auto-optimize.pl ${TERMINUSDB_PLUGINS_PATH}/
RUN mkdir -p /app/terminusdb/dashboard/assets
COPY dashboard/src/index.html /app/terminusdb/dashboard/
COPY dashboard/src/output.css /app/terminusdb/dashboard/assets/
CMD ["/app/terminusdb/init_docker.sh"]

## `Makefile`

DIST ?= community
# Default was 9.2.9
SWIPL_VERSION ?= 10.0.2

RONN_FILE=docs/terminusdb.1.ronn
ROFF_FILE=docs/terminusdb.1
TARGET=terminusdb

################################################################################

# Build the binary.
.PHONY: default
default:
	@$(MAKE) -f distribution/Makefile.prolog

# Build the development binary (macOS-friendly, no library stripping).
# JWT is enabled by default in dev builds so integration tests work out of the box.
.PHONY: dev
dev: clean-rust generate-dev-jwks
	rm src/rust/target/release/libterminusdb_dylib.dylib || true
	rm src/rust/librust.* || true
	@TERMINUSDB_JWT_ENABLED=true $(MAKE) -f distribution/Makefile.prolog $@

# Generate the dev RSA key pair used by JWT integration tests.
# Writes dashboard/assets/test-jwks.json and /tmp/test-jwt-keypair.json.
.PHONY: generate-dev-jwks
generate-dev-jwks:
	node tests/generate-dev-jwks.js

.PHONY: restart
restart:
	tests/terminusdb-test-server.sh restart

.PHONY: server-clean
server-clean:
	tests/terminusdb-test-server.sh start --clean

# Build the Docker image for development and testing. To use the TerminusDB
# container, see: https://github.com/terminusdb/terminusdb-bootstrap
# To make with swipl 10, use: make docker SWIPL_VERSION=10.0.0
.PHONY: docker
docker: export DOCKER_BUILDKIT=1
docker: SKIP_TESTS ?= false
docker:
	docker build . \
	  --file Dockerfile \
	  --tag terminusdb/terminusdb-server:local \
	  --build-arg SWIPL_VERSION="$(SWIPL_VERSION)" \
	  --build-arg SKIP_TESTS="$(SKIP_TESTS)" \
	  --build-arg DIST="$(DIST)" \
	  --build-arg TERMINUSDB_GIT_HASH="$$(git rev-parse --verify HEAD)"

# Build the Docker image for development using local swipl-rs sources.
.PHONY: docker-debug
docker-debug: export DOCKER_BUILDKIT=1
docker-debug: SKIP_TESTS ?= true
docker-debug:
	docker build . \
	  --file docker/debug/Dockerfile \
	  --tag terminusdb/terminusdb-server:debug \
	  --build-context swipl-rs=../swipl-rs \
	  --build-arg SWIPL_VERSION="$(SWIPL_VERSION)" \
	  --build-arg DIST="$(DIST)" \
	  --build-arg SKIP_TESTS="$(SKIP_TESTS)" \
	  --build-arg TERMINUSDB_GIT_HASH="$$(git rev-parse --verify HEAD)"

# Install minimal pack dependencies.
.PHONY: install-deps
install-deps: install-tus

# Install the tus pack.
.PHONY: install-tus
install-tus:
	@$(MAKE) -f distribution/Makefile.deps $@

# Download the lint tool.
.PHONY: download-lint
download-lint:
	@$(MAKE) -f distribution/Makefile.prolog $@

# Download and run the lint tool.
.PHONY: lint
lint:
	@$(MAKE) -f distribution/Makefile.prolog $@

.PHONY: clippy
clippy:
	cargo clippy --message-format=json --all-features --manifest-path=src/rust/Cargo.toml

.PHONY: lint-mocha
lint-mocha:
	sh -c "cd tests; npx npm run check"

.PHONY: lint-mocha-fix
lint-mocha-fix:
	sh -c "cd tests; npx npm run lint"

# The 1.34.7 version is chosen as the others have a React/styled components
# dependency that is not resolved by npx, making it an issue using npx
.PHONY: lint-openapi
lint-openapi:
	sh -c "npx @redocly/cli@1.34.7 lint docs/openapi.yaml --skip-rule no-server-example.com"

# Build the dylib.
.PHONY: rust
rust:
	@$(MAKE) -f distribution/Makefile.rust

# Run unit tests in swipl; all, or just one suite.
# make test OR make test SUITE='[json,terminus_store,tables]'
.PHONY: test
test:
	@$(MAKE) -f distribution/Makefile.prolog $@

# Run the unit tests in node.
# Usage: make test-int                    # run all tests
#        make test-int SUITE=data-version # run test/data-version.js
#        make test-int SUITE="cli-*"      # run all cli tests
.PHONY: test-int
test-int: server-clean
ifdef SUITE
	sh -c "cd tests ; npx mocha 'test/$(SUITE).js'"
else
	sh -c "cd tests ; npx mocha"
endif

# Start Docker container for integration testing (no plugins).
# Rebuilds the docker image and recreates the container.
.PHONY: docker-test-server
docker-test-server: docker
	-docker stop terminusdb-sandbox-test-int 2>/dev/null
	-docker rm terminusdb-sandbox-test-int 2>/dev/null
	docker run -d --name terminusdb-sandbox-test-int \
		-p 6363:6363 \
		-e TERMINUSDB_ADMIN_PASS=root \
		-e TERMINUSDB_PLUGINS_PATH=/void \
		terminusdb/terminusdb-server:local
	@echo "Waiting for server to be ready..."
	@sleep 3
	@curl -sf http://127.0.0.1:6363/api/ok > /dev/null && echo "Docker test server ready at http://127.0.0.1:6363"

# Stop the Docker test server.
.PHONY: docker-test-server-stop
docker-test-server-stop:
	-docker stop terminusdb-sandbox-test-int 2>/dev/null
	-docker rm terminusdb-sandbox-test-int 2>/dev/null
	@echo "Docker test server stopped."

# Quick command for interactive
.PHONY: i
i:
	@$(MAKE) -f distribution/Makefile.prolog $@

# Remove the binary.
.PHONY: prolog-clean
prolog-clean:
	@$(MAKE) -f distribution/Makefile.prolog clean

# Remove everything.
.PHONY: clean
clean: realclean-rust clean-deps prolog-clean docs-clean

# Remove the dylib.
.PHONY: clean-rust
clean-rust:
	@$(MAKE) -f distribution/Makefile.rust clean

# Remove the dylib and all Rust build files.
.PHONY: realclean-rust
realclean-rust:
	@$(MAKE) -f distribution/Makefile.rust realclean

# Remove the deps
.PHONY: clean-deps
clean-deps:
	@$(MAKE) -f distribution/Makefile.deps clean-deps

.PHONY: docs-clean
docs-clean:
	@rm -f $(RONN_FILE)

# Build the documentation.
.PHONY: docs
docs: default $(ROFF_FILE)

################################################################################

# Create input for `ronn` from a template and the `terminusdb` help text.
$(RONN_FILE): docs/terminusdb.1.ronn.template $(TARGET)
	HELP="$$(./$(TARGET) help -m)" envsubst < $< > $@

# Create a man page from using `ronn`.
$(ROFF_FILE): $(RONN_FILE)
	ronn --roff $<

.PHONY: pr
pr: lint lint-mocha lint-openapi clean dev restart test test-int

## `SECURITY.md`

# Security Policy

## Reporting a Vulnerability

Check if the vulnerability is for a currently supported version of TerminusDB
listed below.

| Version | Supported          |
| ------- | ------------------ |
| >= 11.1  | :white_check_mark: |
| < 11.0  | :x:                |

Report the vulnerability to <security@dfrnt.com> (current maintainers of TerminusDB).

> :warning: Please do **not** file a public issue when reporting a
> vulnerability. This allows us to fix the issue and minimize the impact before
> the vulnerability has been widely discovered.

Include the following details in your report:

- OS name and version
- TerminusDB version
- How to reproduce the issue
- Proof of concept exploit code if possible

## `docs/README.md`

## Documentation Information

This is repository-specific documentation.

The full TerminusDB and TerminusCMS docs are [available here](https://terminusdb.com/docs).
