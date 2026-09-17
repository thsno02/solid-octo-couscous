# Repository semantic capsule: treeverse/lakeFS

- Commit: `4bb11638e95637e853d9680abf072b14f09e32fb`
- Default branch: `master`
- Description: lakeFS
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

<p align="center">
  <img src=".github/assets/logo_large.png"/>
</p>
<p align="center">
	<a href="https://raw.githubusercontent.com/treeverse/lakeFS/master/LICENSE" >
		<img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="Apache License" /></a>
	<a href="https://github.com/treeverse/lakeFS/actions/workflows/test.yaml?query=branch%3Amaster">
		<img src="https://github.com/treeverse/lakeFS/workflows/Test/badge.svg?branch=master" alt="Go tests status" /></a>
	<a href="https://github.com/treeverse/lakeFS/actions/workflows/node.yaml?query=branch%3Amaster" >
		<img src="https://github.com/treeverse/lakeFS/workflows/Node/badge.svg?branch=master" alt="Node tests status" /></a>
	<a href="https://github.com/treeverse/lakeFS/actions/workflows/esti.yaml?query=branch%3Amaster">
		<img src="https://github.com/treeverse/lakeFS/workflows/Esti/badge.svg?branch=master" alt="Integration tests status" /></a>
	<a href="https://artifacthub.io/packages/search?repo=lakefs">
		<img src="https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/lakefs" alt="Artifact HUB" /></a>
	<a href="CODE_OF_CONDUCT.md">
		<img src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg" alt="code of conduct"></a>
</p>

## lakeFS is Data Version Control (Git for Data)

lakeFS is an open-source tool that transforms your object storage into a Git-like repository. It enables you to manage your data lake the way you manage your code.

With lakeFS you can build repeatable, atomic, and versioned data lake operations - from complex ETL jobs to data science and analytics.

lakeFS supports AWS S3, Azure Blob Storage, and Google Cloud Storage as its underlying storage service. It is API compatible with S3 and works seamlessly with all modern data frameworks such as Spark, Hive, AWS Athena, DuckDB, and Presto.

For more information, see the [documentation](https://docs.lakefs.io/).

## Getting Started

You can spin up a standalone sandbox instance of lakeFS:

```bash
pip install lakefs
python -m lakefs.quickstart
```

Once you've got lakeFS running, open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

### Getting Started with Docker

Alternatively, you can run lakeFS a server using Docker:

```bash
docker run --pull always \
		   --name lakefs \
		   -p 8000:8000 \
		   treeverse/lakefs:latest \
		   run --quickstart
```

### Quickstart

**👉🏻 For a hands-on walk through of the core functionality in lakeFS head over to [the quickstart](https://docs.lakefs.io/quickstart/) to jump right in!**

Make sure to also have a look at the [lakeFS samples](https://github.com/treeverse/lakeFS-samples). These are a rich resource of examples of end-to-end applications that you can build with lakeFS.

## Why Do I Need lakeFS?

### ETL Testing with Isolated Dev/Test Environment

When working with a data lake, it’s useful to have replicas of your production environment. These replicas allow you to test these ETLs and understand changes to your data without impacting downstream data consumers.

Running ETL and transformation jobs directly in production without proper ETL Testing is a guaranteed way to have data issues flow into dashboards, ML models, and other consumers sooner or later. The most common approach to avoid making changes directly in production is to create and maintain multiple data environments and perform ETL testing on them. Dev environment to develop the data pipelines and test environment where pipeline changes are tested before pushing it to production. With lakeFS you can create branches, and get a copy of the full production data, without copying anything. This enables a faster and easier process of ETL testing.

### Reproducibility

Data changes frequently. This makes the task of keeping track of its exact state over time difficult. Oftentimes, people maintain only one state of their data––its current state.

This has a negative impact on the work, as it becomes hard to:
* Debug a data issue.
* Validate machine learning training accuracy (re-running a model over different data gives different results).
Comply with data audits.

In comparison, lakeFS exposes a Git-like interface to data that allows keeping track of more than just the current state of data. This makes reproducing its state at any point in time straightforward.

### Write-Audit-Publish

Data pipelines feed processed data from data lakes to downstream consumers like business dashboards and machine learning models. As more and more organizations rely on data to enable business critical decisions, data reliability and trust are of paramount concern. Thus, it’s important to ensure that production data adheres to the data governance policies of businesses. These data governance requirements can be as simple as a file format validation, schema check, or an exhaustive PII(Personally Identifiable Information) data removal from all of organization’s data.

Thus, to ensure the quality and reliability at each stage of the data lifecycle, data quality gates need to be implemented. That is, we need to run quality and correctness tests on the data, and only if data governance requirements are met can the data can be published to production for business use.

Everytime there is an update to production data, the best practice would be to run tests and then publish (deploy) the data to production. With lakeFS you can create hooks that make sure that only data that passed these tests will become part of production.

### Rollback

A rollback operation is used to to fix critical data errors immediately.

What is a critical data error? Think of a situation where erroneous or misformatted data causes a signficant issue with an important service or function. In such situations, the first thing to do is stop the bleeding.

Rolling back returns data to a state in the past, before the error was present. You might not be showing all the latest data after a rollback, but at least you aren’t showing incorrect data or raising errors. Since lakeFS provides versions of the data without making copies of the data, you can time travel between versions and roll back to the version of the data before the error was presented.

## Community

Stay up to date and get lakeFS support via:

- Share your lakeFS experience and get support on [our Slack](https://go.lakefs.io/JoinSlack).
- Follow us and join the conversation on [Twitter](https://twitter.com/lakeFS).
- Learn from video tutorials on [our YouTube channel](https://lakefs.io/youtube).
- Read more on data versioning and other data lake best practices in [our blog](https://lakefs.io/blog/data-version-control/).
- Feel free to [contact us](https://lakefs.io/contact-us/) about anything else.

## More information

- Read the [documentation](https://docs.lakefs.io/).
- See the [contributing guide](https://docs.lakefs.io/project/contributing/).
- Take a look at our [roadmap](https://docs.lakefs.io/project/) to peek into the future of lakeFS.

## Licensing

lakeFS is completely free and open-source and licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

Treeverse considers that any sharing of source code with an AI agent, and any output an AI agent generates based on our source code, without the appropriate notices or attribution requirements, violates the terms of the Apache 2.0 license to which this source code is subject. 
We also do not consider AI provider guardrails as sufficient to prevent copyright infringement. Treeverse reserves all of its rights to pursue legal action against any party that inputs LakeFS code into an AI agent.

## Who Uses lakeFS?

lakeFS is used by numerous companies, including those below. _If you use lakeFS and would like to be included here please open a PR._

* AirAsia
* APEX Global
* AppsFlyer
* Auburn University
* BAE Systems
* Bureau of Labor Statistics
* Cambridge Consultants
* Connor, Clark & Lunn Financial Group
* Context Labs Bv
* Daimler Truck
* Enigma
* EPCOR
* Ford Motor Company
* Generali
* Giesecke+Devrient
* greehill
* Karius
* Luxonis
* Mixpeek
* Netflix
* Paige
* PETRONAS
* Pollinate
* Proton Technologies AG
* ProtonMail
* Renaissance Computing Institute
* RHEA Group 
* RMS
* Sensum
* Similarweb
* State Street Global Advisors
* Terramera
* Tredence
* Volvo Cars
* Webiks
* Windward
* Woven by Toyota

## `Dockerfile`

# syntax=docker/dockerfile:1
ARG VERSION=dev

ARG BUILD_REPO=golang
ARG BUILD_TAG=1.26-alpine
ARG BUILD_PACKAGES="build-base ca-certificates"

ARG IMAGE_REPO=alpine
ARG IMAGE_TAG=3.24
ARG IMAGE_PACKAGES=ca-certificates

ARG ADD_PACKAGES="apk add -U --no-cache"


FROM --platform=$BUILDPLATFORM $BUILD_REPO:$BUILD_TAG AS build
ARG ADD_PACKAGES BUILD_PACKAGES

WORKDIR /build
RUN $ADD_PACKAGES $BUILD_PACKAGES
COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg go mod download
COPY . ./

FROM build AS build-lakefs
ARG VERSION TARGETOS TARGETARCH ADD_PACKAGES BUILD_PACKAGES
RUN --mount=type=cache,target=/root/.cache/go-build \
    --mount=type=cache,target=/go/pkg \
    GOOS=$TARGETOS GOARCH=$TARGETARCH \
    go build -ldflags "-X github.com/treeverse/lakefs/pkg/version.Version=${VERSION}" -o lakefs ./cmd/lakefs

FROM build AS build-lakectl
ARG VERSION TARGETOS TARGETARCH ADD_PACKAGES BUILD_PACKAGES
RUN --mount=type=cache,target=/root/.cache/go-build \
    --mount=type=cache,target=/go/pkg \
    GOOS=$TARGETOS GOARCH=$TARGETARCH \
    go build -ldflags "-X github.com/treeverse/lakefs/pkg/version.Version=${VERSION}" -o lakectl ./cmd/lakectl

FROM $IMAGE_REPO:$IMAGE_TAG AS lakectl
ARG ADD_PACKAGES IMAGE_PACKAGES
WORKDIR /app
ENV PATH=/app:$PATH
COPY --from=build-lakectl /build/lakectl /app/
RUN $ADD_PACKAGES $IMAGE_PACKAGES
RUN addgroup -S lakefs && adduser -S lakefs -G lakefs
USER lakefs
WORKDIR /home/lakefs
ENTRYPOINT ["/app/lakectl"]

FROM lakectl AS lakefs
COPY ./scripts/wait-for /app/
COPY --from=build-lakefs /build/lakefs /app/
EXPOSE 8000/tcp
ENTRYPOINT ["/app/lakefs"]
CMD ["run"]

## `Makefile`

GOCMD=$(or $(shell which go), $(error "Missing dependency - no go in PATH"))
DOCKER=$(or $(shell which docker), $(error "Missing dependency - no docker in PATH"))
GOBINPATH=$(shell $(GOCMD) env GOPATH)/bin
NPM=$(or $(shell which npm), $(error "Missing dependency - no npm in PATH"))

UID_GID := $(shell id -u):$(shell id -g)

CLIENT_JARS_BUCKET="s3://treeverse-clients-us-east/"

# https://openapi-generator.tech
OPENAPI_GENERATOR_IMAGE=treeverse/openapi-generator-cli:v7.0.1.4
OPENAPI_GENERATOR=$(DOCKER) run -e JAVA_OPTS="-Dlog.level=error" --user $(UID_GID) --rm -v $(shell pwd):/mnt $(OPENAPI_GENERATOR_IMAGE)
PY_OPENAPI_GENERATOR=$(DOCKER) run -e JAVA_OPTS="-Dlog.level=error" -e PYTHON_POST_PROCESS_FILE="/mnt/clients/python-static/pydantic.sh" --user $(UID_GID) --rm -v $(shell pwd):/mnt $(OPENAPI_GENERATOR_IMAGE)

OPENAPI_RUST_GENERATOR_IMAGE=openapitools/openapi-generator-cli:v7.5.0
OPENAPI_RUST_GENERATOR=$(DOCKER) run -e JAVA_OPTS="-Dlog.level=error" --user $(UID_GID) --rm -v $(shell pwd):/mnt $(OPENAPI_RUST_GENERATOR_IMAGE)

BUF_CLI_VERSION=v1.54.0

ifndef PACKAGE_VERSION
	PACKAGE_VERSION=0.0.0
endif

PYTHON_IMAGE=python:3.10

export PATH:= $(PATH):$(GOBINPATH)

GOBUILD=$(GOCMD) build
GORUN=$(GOCMD) run
GOCLEAN=$(GOCMD) clean
GOTOOL=$(GOCMD) tool
GOGENERATE=$(GOCMD) generate
GOTEST=$(GOCMD) test
GOTESTRACE=$(GOTEST) -race
GOGET=$(GOCMD) get
GOFMT=$(GOCMD)fmt

GOTEST_FLAGS=-count=1 -race -failfast
LAKEFS_BINARY_NAME=lakefs
LAKECTL_BINARY_NAME=lakectl

UI_DIR=webui
UI_BUILD_DIR=$(UI_DIR)/dist

DOCKER_IMAGE=lakefs
DOCKER_TAG=dev
VERSION=dev
export VERSION

# This cannot detect whether untracked files have yet to be added.
# That is sort-of a git feature, but can be a limitation here.
DIRTY=$(shell git diff-index --quiet HEAD -- || echo '.with.local.changes')
GIT_REF=$(shell git rev-parse --short HEAD --)
REVISION=$(GIT_REF)$(DIRTY)
export REVISION

.PHONY: all clean esti lint test gen help
all: build

clean:
	@rm -rf \
		$(LAKECTL_BINARY_NAME) \
		$(LAKEFS_BINARY_NAME) \
		$(UI_BUILD_DIR) \
		$(UI_DIR)/node_modules
	@mkdir -p $(UI_BUILD_DIR) && touch $(UI_BUILD_DIR)/.gitkeep

check-licenses: check-licenses-go-mod check-licenses-npm

check-licenses-go-mod:
	$(GOCMD) install github.com/google/go-licenses@latest
	$(GOBINPATH)/go-licenses check ./cmd/$(LAKEFS_BINARY_NAME)
	$(GOBINPATH)/go-licenses check ./cmd/$(LAKECTL_BINARY_NAME)

check-licenses-npm:
	$(GOCMD) install github.com/senseyeio/diligent/cmd/diligent@latest
	# The -i arg is a workaround to ignore NPM scoped packages until https://github.com/senseyeio/diligent/issues/77 is fixed
	$(GOBINPATH)/diligent check -w permissive -i ^@[^/]+?/[^/]+ $(UI_DIR)

.PHONY: tools
tools: ## Install tools
	$(GOCMD) install github.com/bufbuild/buf/cmd/buf@$(BUF_CLI_VERSION)

client-python: api/swagger.yml  ## Generate SDK for Python client - openapi generator version 7.0.0
	@rm -rf clients/python
	@mkdir -p clients/python
	@cp clients/python-static/.openapi-generator-ignore clients/python
	@echo "Generating Python client SDK"
	$(PY_OPENAPI_GENERATOR) generate \
		-i /mnt/$< \
		-g python \
		-t /mnt/clients/python-static/templates \
		-c /mnt/clients/python-static/python-codegen-config.yaml \
		--enable-post-process-file \
		--package-name lakefs_sdk \
		--http-user-agent "lakefs-python-sdk/$(PACKAGE_VERSION)" \
		--git-user-id treeverse --git-repo-id lakeFS \
		--additional-properties=infoName=Treeverse,infoEmail=services@treeverse.io,packageVersion=$(PACKAGE_VERSION),projectName=lakefs-sdk,packageUrl=https://github.com/treeverse/lakeFS/tree/master/clients/python \
		-o /mnt/clients/python

sdk-rust: api/swagger.yml  ## Generate SDK for Rust client - openapi generator version 7.1.0
	@rm -rf clients/rust
	@mkdir -p clients/rust
	@echo "Generating Rust client SDK"
	$(OPENAPI_RUST_GENERATOR) generate \
		-i /mnt/api/swagger.yml \
		-g rust \
		--additional-properties=infoName=Treeverse,infoEmail=services@treeverse.io,packageName=lakefs_sdk,packageVersion=$(PACKAGE_VERSION),packageUrl=https://github.com/treeverse/lakeFS/tree/master/clients/rust \
		-o /mnt/clients/rust

client-java: api/swagger.yml api/java-gen-ignore  ## Generate SDK for Java (and Scala) client
	@rm -rf clients/java
	@mkdir -p clients/java
	@cp api/java-gen-ignore clients/java/.openapi-generator-ignore
	@echo "Generating Java client SDK"
	$(OPENAPI_GENERATOR) generate \
		-i /mnt/api/swagger.yml \
		-g java \
		--invoker-package io.lakefs.clients.sdk \
		--http-user-agent "lakefs-java-sdk/$(PACKAGE_VERSION)-v1" \
		--additional-properties disallowAdditionalPropertiesIfNotPresent=false,useSingleRequestParameter=true,hideGenerationTimestamp=true,artifactVersion=$(PACKAGE_VERSION),parentArtifactId=lakefs-parent,parentGroupId=io.lakefs,parentVersion=0,groupId=io.lakefs,artifactId='sdk',artifactDescription='lakeFS OpenAPI Java client',artifactUrl=https://lakefs.io,apiPackage=io.lakefs.clients.sdk,modelPackage=io.lakefs.clients.sdk.model,mainPackage=io.lakefs.clients.sdk,developerEmail=services@treeverse.io,developerName='Treeverse lakeFS dev',developerOrganization='lakefs.io',developerOrganizationUrl='https://lakefs.io',licenseName=apache2,licenseUrl=http://www.apache.org/licenses/,scmConnection=scm:git:git@github.com:treeverse/lakeFS.git,scmDeveloperConnection=scm:git:git@github.com:treeverse/lakeFS.git,scmUrl=https://github.com/treeverse/lakeFS \
		-o /mnt/clients/java

.PHONY: clients client-python client-java
clients: client-python client-java sdk-rust

package-python: package-python-sdk package-python-wrapper

package-python-sdk: client-python
	$(DOCKER) run --user $(UID_GID) --rm -v $(shell pwd):/mnt -e HOME=/tmp/ -w /mnt/clients/python $(PYTHON_IMAGE) /bin/bash -c \
		"python -m pip install build --user && python -m build --sdist --wheel --outdir dist/"

package-python-wrapper:
	$(DOCKER) run --user $(UID_GID) --rm -v $(shell pwd):/mnt -e HOME=/tmp/ -w /mnt/clients/python-wrapper $(PYTHON_IMAGE) /bin/bash -c \
		"python -m pip install build --user && python -m build --sdist --wheel --outdir dist/"

package: package-python

.PHONY: gen-api
gen-api: ## Run the swagger code generator
	$(GOGENERATE) ./pkg/api/apigen ./pkg/auth ./pkg/authentication

.PHONY: gen-code
gen-code: gen-api ## Run the generator for inline commands
	$(GOGENERATE) \
		./contrib/auth/acl \
		./pkg/actions \
		./pkg/distributed \
		./pkg/graveler \
		./pkg/graveler/committed \
		./pkg/graveler/sstable \
		./pkg/kv \
		./pkg/permissions \
		./pkg/pyramid \
		./tools/wrapgen/testcode

LD_FLAGS := "-X github.com/treeverse/lakefs/pkg/version.Version=$(VERSION)-$(REVISION)"
build: gen build-binaries ## Download dependencies and build the default binary

build-binaries:
	$(GOBUILD) -o $(LAKEFS_BINARY_NAME) -ldflags $(LD_FLAGS) -v ./cmd/$(LAKEFS_BINARY_NAME)
	$(GOBUILD) -o $(LAKECTL_BINARY_NAME) -ldflags $(LD_FLAGS) -v ./cmd/$(LAKECTL_BINARY_NAME)

lint: ## Lint code
	$(GOCMD) tool golangci-lint run ./... $(GOLANGCI_LINT_FLAGS)
	cd $(UI_DIR) && npm run lint

esti: ## run esti (system testing)
	$(GOTEST) -v ./esti --args --system-tests

test: test-go test-hadoopfs  ## Run tests for the project

test-go: gen-api			# Run parallelism > num_cores: most of our slow tests are *not* CPU-bound.
	go list -f '{{.Dir}}/...' -m | xargs $(GOTEST) -coverprofile=cover.out -cover $(GOTEST_FLAGS) ./...

test-hadoopfs:
	cd clients/hadoopfs && mvn test

run-test:  ## Run tests without generating anything (faster if already generated)
	$(GOTEST) -count=1 -coverprofile=cover.out -race -short -cover -failfast ./...

fast-test:  ## Run tests without race detector (faster)
	$(GOTEST) -count=1 -coverprofile=cover.out -short -cover -failfast ./...

test-html: test  ## Run tests with HTML for the project
	$(GOTOOL) cover -html=cover.out

system-tests: # Run system tests locally
	./esti/scripts/runner.sh -r all

build-docker: build ## Build Docker image file (Docker required)
	$(DOCKER) buildx build --target lakefs -t treeverse/$(DOCKER_IMAGE):$(DOCKER_TAG) .

gofmt:  ## gofmt code formating
	@echo Running go formating with the following command:
	$(GOFMT) -e -s -w .

.PHONY: validate-proto
validate-proto: gen-proto  ## build proto and check if diff found
	git diff --quiet -- pkg/actions/actions.pb.go || (echo "Modification verification failed! pkg/actions/actions.pb.go"; false)
	git diff --quiet -- pkg/auth/model/model.pb.go || (echo "Modification verification failed! pkg/auth/model/model.pb.go"; false)
	git diff --quiet -- pkg/catalog/catalog.pb.go || (echo "Modification verification failed! pkg/catalog/catalog.pb.go"; false)
	git diff --quiet -- pkg/gateway/multipart/multipart.pb.go || (echo "Modification verification failed! pkg/gateway/multipart/multipart.pb.go"; false)
	git diff --quiet -- pkg/graveler/graveler.pb.go || (echo "Modification verification failed! pkg/graveler/graveler.pb.go"; false)
	git diff --quiet -- pkg/graveler/committed/committed.pb.go || (echo "Modification verification failed! pkg/graveler/committed/committed.pb.go"; false)
	git diff --quiet -- pkg/graveler/settings/test_settings.pb.go || (echo "Modification verification failed! pkg/graveler/settings/test_settings.pb.go"; false)
	git diff --quiet -- pkg/kv/secondary_index.pb.go || (echo "Modification verification failed! pkg/kv/secondary_index.pb.go"; false)
	git diff --quiet -- pkg/kv/kvtest/test_model.pb.go || (echo "Modification verification failed! pkg/kv/kvtest/test_model.pb.go"; false)

.PHONY: validate-mockgen
validate-mockgen: gen-code
	git diff --quiet -- pkg/actions/mock/mock_actions.go || (echo "Modification verification failed! pkg/actions/mock/mock_actions.go"; false)
	git diff --quiet -- pkg/auth/mock/mock_auth_client.go || (echo "Modification verification failed! pkg/auth/mock/mock_auth_client.go"; false)
	git diff --quiet -- pkg/authentication/api/mock_authentication_client.go || (echo "Modification verification failed! pkg/authentication/api/mock_authentication_client.go"; false)
	git diff --quiet -- pkg/graveler/committed/mock/batch_write_closer.go || (echo "Modification verification failed! pkg/graveler/committed/mock/batch_write_closer.go"; false)
	git diff --quiet -- pkg/graveler/committed/mock/meta_range.go || (echo "Modification verification failed! pkg/graveler/committed/mock/meta_range.go"; false)
	git diff --quiet -- pkg/graveler/committed/mock/range_manager.go || (echo "Modification verification failed! pkg/graveler/committed/mock/range_manager.go"; false)
	git diff --quiet -- pkg/graveler/mock/graveler.go || (echo "Modification verification failed! pkg/graveler/mock/graveler.go"; false)
	git diff --quiet -- pkg/graveler/hooks_handler_isvalid.gen.go || (echo "Modification verification failed! pkg/graveler/hooks_handler_isvalid.gen.go"; false)
	git diff --quiet -- pkg/kv/mock/store.go || (echo "Modification verification failed! pkg/kv/mock/store.go"; false)

## `SECURITY.md`

# Security Policy

## Supported Versions

To receive latest security and regular updates, users should stay up to date on all
releases.  Prior to the release of a 1.0.0 version only the latest released version
will receive all security updates.

Please contact us at https://lakefs.io/contact-us/ if you need security updates for
an earlier version.

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |
| < latest| :x: |

## Staying Up to Date

We announce all releases on the [lakefs-releases][slack-lakefs-releases] channel of
our Slack workspace.  There is also a mailing list for security announcements which
you can join: [security-announce@treeverse.io][security-mailing-list].

## Reporting a Vulnerability

We take the security of lakeFS seriously.  You can help us by following responsible
disclosure guidelines.

If you believe you’ve discovered a serious vulnerability, please report it to us by
emailing security@treeverse.io.  Please **do _NOT_** open an issue as GitHub issues
are publicly discoverable.  We acknowledge reports within 24 hours.  We will report
progress to the email used for reporting.

We will evaluate your report and if necessary issue a fix and an advisory. We would
like to credit you if the issue was unknown to us prior to your report; please tell
us if you would prefer that we do not.

We will work to release a fix within 90 days.  In rare conditions we may request an
additional 14 days to release a fix.  This is in line with disclosure policies such
as those of [Google Project Zero][project-zero-policy].  Hopefully we shall release
a fix well before then.

[project-zero-policy]: https://googleprojectzero.blogspot.com/2021/04/policy-and-disclosure-2021-edition.html
[slack-lakefs-releases]: https://lakefs.slack.com/archives/C017S6YFFSP
[security-mailing-list]: https://groups.google.com/g/lakefs-security-announce
