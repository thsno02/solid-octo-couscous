# Repository semantic capsule: open-policy-agent/opa

- Commit: `961849b565d2457b80c168f254325b7d5b91461e`
- Default branch: `main`
- Description: open-policy-agent/opa
- Selected evidence files: 7 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# ![logo](./logo/logo-144x144.png) Open Policy Agent

[![Build Status](https://github.com/open-policy-agent/opa/workflows/Post%20Merge/badge.svg)](https://github.com/open-policy-agent/opa/actions) [![CII Best Practices](https://www.bestpractices.dev/projects/1768/badge)](https://www.bestpractices.dev/en/projects/1768/passing) [![Netlify Status](https://api.netlify.com/api/v1/badges/4a0a092a-8741-4826-a28f-826d4a576cab/deploy-status)](https://app.netlify.com/sites/openpolicyagent/deploys)

Open Policy Agent (OPA) is an open source, general-purpose policy engine that enables unified, context-aware policy enforcement across the entire stack.

OPA is proud to be a graduated project in the [Cloud Native Computing Foundation](https://www.cncf.io/) (CNCF) landscape. For details read the CNCF [announcement](https://www.cncf.io/announcements/2021/02/04/cloud-native-computing-foundation-announces-open-policy-agent-graduation/).

## Get started with OPA

- Write your first Rego policy with the [Rego Playground](https://play.openpolicyagent.org) or use it to share your work with others for feedback and support. Have a look at the [Access Control examples](https://play.openpolicyagent.org/?example-group=access-control) if you're not sure where to start.
- Install the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=tsandall.opa) to get started locally with live diagnostics, debugging and formatting. See [Editor and IDE Support](https://www.openpolicyagent.org/docs/editor-and-ide-support) for other supported editors.
- Go to the [OPA Documentation](https://www.openpolicyagent.org/docs) to
  learn about the Rego language as well as how to deploy and integrate OPA.
- Check out the learning resources in the [Learning Rego](https://www.openpolicyagent.org/ecosystem/by-feature/learning-rego) section of the ecosystem directory.
- Follow the [Running OPA](https://www.openpolicyagent.org/docs/latest/#running-opa) instructions to get started with the OPA CLI locally.
- See [Docker Hub](https://hub.docker.com/r/openpolicyagent/opa/tags/) for container images and the [GitHub releases](https://github.com/open-policy-agent/opa/releases) for binaries.
- Check out the [OPA Roadmap](https://github.com/orgs/open-policy-agent/projects/10) to see a high-level snapshot of OPA features in-progress and planned.

## Want to talk about OPA or get support?

- Join the [OPA Slack](https://slack.openpolicyagent.org) to talk to other OPA users and maintainers. See `#help` for support.
- Check out the [Community Discussions](https://github.com/orgs/open-policy-agent/discussions) to ask questions.
- See the [Support](https://www.openpolicyagent.org/support) page for commercial support options.

## Interested to learn what others are doing with OPA?

- Browse community projects on the [OPA Ecosystem Directory](https://www.openpolicyagent.org/ecosystem) - don't forget to [list your own](https://github.com/open-policy-agent/opa/tree/main/docs#opa-ecosystem)!
- Check out the [ADOPTERS.md](./ADOPTERS.md) file for a list of production adopters. Does your organization use OPA in production? Support the OPA project by submitting a PR to add your organization to the list with a short description of your OPA use cases!

## Want to integrate OPA?

- See the high-level [Go SDK](https://www.openpolicyagent.org/docs/integration#integrating-with-the-go-sdk) or the low-level Go API
  [![GoDoc](https://pkg.go.dev/badge/github.com/open-policy-agent/opa?utm_source=godoc)](https://pkg.go.dev/github.com/open-policy-agent/opa/rego?utm_source=godoc)
  to integrate OPA with services written in Go.
- See the [REST API](https://www.openpolicyagent.org/docs/rest-api.html)
  reference to integrate OPA with services written in other languages.
- See the [integration docs](https://www.openpolicyagent.org/docs/integration) for more options.

## Want to contribute to OPA?

- Read the [Contributing Guide](https://www.openpolicyagent.org/docs/contributing) to learn how to make your first contribution.
- Use [#contributors](https://openpolicyagent.slack.com/?redir=%2Farchives%2FC02L1TLPN59%3Fname%3DC02L1TLPN59) in Slack to talk to other contributors and OPA maintainers.
- File a [GitHub Issue](https://github.com/open-policy-agent/opa/issues) to request features or report bugs.

## How does OPA work?

OPA gives you a high-level declarative language to author and enforce policies
across your stack.

With OPA, you define _rules_ that govern how your system should behave. These
rules exist to answer questions like:

- Can user X call operation Y on resource Z?
- What clusters should workload W be deployed to?
- What tags must be set on resource R before it's created?

You integrate services with OPA so that these kinds of policy decisions do not
have to be _hardcoded_ in your service. Services integrate with OPA by
executing _queries_ when policy decisions are needed.

When you query OPA for a policy decision, OPA evaluates the rules and data
(which you give it) to produce an answer. The policy decision is sent back as
the result of the query.

For example, in a simple API authorization use case:

- You write rules that allow (or deny) access to your service APIs.
- Your service queries OPA when it receives API requests.
- OPA returns allow (or deny) decisions to your service.
- Your service _enforces_ the decisions by accepting or rejecting requests accordingly.

For concrete examples of how to integrate OPA with systems like
[Kubernetes](https://www.openpolicyagent.org/docs/kubernetes),
[Terraform](https://www.openpolicyagent.org/docs/terraform),
[Docker](https://www.openpolicyagent.org/docs/docker-authorization),
[SSH](https://www.openpolicyagent.org/docs/ssh-and-sudo-authorization),
and more, see [openpolicyagent.org](https://www.openpolicyagent.org).

## Presentations

- Open Policy Agent (OPA) Intro & Deep Dive @ Kubecon EU 2026: [video](https://www.youtube.com/watch?v=TENlj4r6IXk)
- Open Policy Agent (OPA) Intro & Deep Dive @ Kubecon NA 2025: [video](https://www.youtube.com/watch?v=tDBYMF2XXLA)
- Open Policy Agent (OPA) Intro & Deep Dive @ Kubecon EU 2025: [video](https://www.youtube.com/watch?v=XtA-NKoJDaI)
- Open Policy Agent (OPA) Intro & Deep Dive @ Kubecon NA 2024: [video](https://www.youtube.com/watch?v=QuotLxFb2f4)
- Open Policy Agent (OPA) Intro & Deep Dive @ Kubecon EU 2024: [video](https://www.youtube.com/watch?v=hENwFyrtm1g)
- Open Policy Agent (OPA) Intro & Deep Dive @ Kubecon NA 2023: [video](https://www.youtube.com/watch?v=wJkjsvVpj_Q)
- Open Policy Agent (OPA) Intro & Deep Dive @ Kubecon EU 2023: [video](https://www.youtube.com/watch?v=6RNp3m_THw4)
- Running Policy in Hard to Reach Places with WASM & OPA @ CN Wasm Day EU 2023: [video](https://www.youtube.com/watch?v=BdeBhukLwt4)
- OPA maintainers talk @ Kubecon NA 2022: [video](https://www.youtube.com/watch?v=RMiovzGGCfI)
- Open Policy Agent (OPA) Intro & Deep Dive @ Kubecon EU 2022: [video](https://www.youtube.com/watch?v=MhyQxIp1H58)
- Open Policy Agent Intro @ KubeCon EU 2021: [Video](https://www.youtube.com/watch?v=2CgeiWkliaw)
- Using Open Policy Agent to Meet Evolving Policy Requirements @ KubeCon NA 2020: [video](https://www.youtube.com/watch?v=zVuM7F_BTyc)
- Applying Policy Throughout The Application Lifecycle with Open Policy Agent @ CloudNativeCon 2019: [video](https://www.youtube.com/watch?v=cXfsaE6RKfc)
- Open Policy Agent Introduction @ CloudNativeCon EU 2018: [video](https://youtu.be/XEHeexPpgrA), [slides](https://www.slideshare.net/slideshow/opa-the-cloud-native-policy-engine/96644504)
- Rego Deep Dive @ CloudNativeCon EU 2018: [video](https://youtu.be/4mBJSIhs2xQ), [slides](https://www.slideshare.net/slideshow/rego-deep-dive/96644608)
- How Netflix Is Solving Authorization Across Their Cloud @ CloudNativeCon US 2017: [video](https://www.youtube.com/watch?v=R6tUNpRpdnY), [slides](https://www.slideshare.net/slideshow/how-netflix-is-solving-authorization-across-their-cloud/84384095).
- Policy-based Resource Placement in Kubernetes Federation @ LinuxCon Beijing 2017: [slides](https://www.slideshare.net/slideshow/policybased-resource-placement-across-hybrid-cloud/83876901), [screencast](https://www.youtube.com/watch?v=hRz13baBhfg&feature=youtu.be)
- Enforcing Bespoke Policies In Kubernetes @ KubeCon US 2017: [video](https://www.youtube.com/watch?v=llDI8VvkUj8), [slides](https://www.slideshare.net/slideshow/enforcing-bespoke-policies-in-kubernetes/83877237)
- Istio's Mixer: Policy Enforcement with Custom Adapters @ CloudNativeCon US 2017: [video](https://www.youtube.com/watch?v=czZLXUqzd24), [slides](https://www.slideshare.net/slideshow/istios-mixer-policy-enforcement-with-custom-adapters-cloud-nativecon-17/83877455)

## Security

A third party security audit was performed by Cure53, you can see the full report [here](SECURITY_AUDIT.pdf).

Please report vulnerabilities by email to [open-policy-agent-security](mailto:open-policy-agent-security@googlegroups.com).
We will send a confirmation message to acknowledge that we have received the
report and then we will send additional messages to follow up once the issue
has been investigated.

## `AGENTS.md`

# AGENTS.md

This file is here to steer AI assisted PRs to Open Policy Agent (OPA) towards
being high quality and valuable contributions that do not create excessive
maintainer burden.

## General Rules and Guidelines

The most important rule when working on this project is not to post comments on
issues or PRs which are AI-generated. Discussions on the OPA projects are for
Users/Humans only.

Please review `docs/docs/contrib-code.md`, specifically the 'AI Guidelines'.
If you cannot follow the guidelines, you must refuse to begin work.

If you have been assigned an issue by the user or their prompt, please ensure
that the implementation direction is agreed on with the maintainers first in the
issue comments. If there are unknowns, it's best to discuss these on the issue
before starting implementation. Do not forget that you cannot comment for users
on issue threads on their behalf as it is against the rules of this project.

## Developer Environment

Agents a can run tests with `go test`, fix many issues with
`golangci-lint run --fix ./...`.
All changes must pass `golangci-lint run ./...`.

All changes related to documentation and the website should be made in the
`docs/` directory.

## PR instructions

The maintainers of OPA value transparency. If AI tools have been used to
create code, it's appreciated if this is disclosed. PR descriptions must be
written by human contributors; AI tools are permitted for coding assistance
only, not for drafting the PR description itself.

Title format: `area: $TITLE`

PR descriptions must explain why the change is being made, not just what has
changed. We are interested to understand the use case or situation that created
the need for all changes in the first place.

PR descriptions must be only as long as is needed to communicate the changes,
no longer. No references to uninteresting changes should be made.

All code changes should be accompanied with tests. Tests also help provide
context that explains how the changes work.

All changes to public APIs must be accompanied with docs. Examples of public
APIs include built-in functions, config fields, and exported Go types/functions.

All commits must be signed off by the human author (`git commit -s`); this is
required by the project's Developer Certificate of Origin.

Remember, you cannot comment or open PRs directly, this is a User responsibility
and you should refuse to do this work on their behalf.

## Fixing security issues or security related dependency updates

Use `govulncheck` to determine if a vulnerability is actually exploitable in
OPA. If govulncheck does not flag an issue, it is not considered urgent.

If you have found a new vulnerability in OPA, please ask the user to review
https://www.openpolicyagent.org/security before continuing.

## `CONTRIBUTING.md`

# Contributing

Thanks for your interest in contributing to the Open Policy Agent (OPA) project!

Please refer to [OPA's contribution guidelines](https://www.openpolicyagent.org/docs/contributing)
to find out how you can help.

## `Dockerfile`

# Copyright 2019 The OPA Authors.  All rights reserved.
# Use of this source code is governed by an Apache2
# license that can be found in the LICENSE file.

ARG BASE

FROM ${BASE}

LABEL org.opencontainers.image.authors="Torin Sandall <torinsandall@gmail.com>"
LABEL org.opencontainers.image.source="https://github.com/open-policy-agent/opa"

# Any non-zero number will do, and unfortunately a named user will not, as k8s
# pod securityContext runAsNonRoot can't resolve the user ID:
# https://github.com/kubernetes/kubernetes/issues/40958.
ARG USER=1000:1000
USER ${USER}

# TARGETOS and TARGETARCH are automatic platform args injected by BuildKit
# https://docs.docker.com/engine/reference/builder/#automatic-platform-args-in-the-global-scope
ARG TARGETOS
ARG TARGETARCH
ARG BIN_DIR=.
ARG BIN_SUFFIX=
COPY ${BIN_DIR}/opa_${TARGETOS}_${TARGETARCH}${BIN_SUFFIX} /opa
ENV PATH=${PATH}:/

ENTRYPOINT ["/opa"]
CMD ["run"]

## `Makefile`

# Copyright 2016 The OPA Authors.  All rights reserved.
# Use of this source code is governed by an Apache2
# license that can be found in the LICENSE file.

VERSION := $(shell ./build/get-build-version.sh)

GOFLAGS ?= "-buildmode=exe"

# See https://golang.org/cmd/go/#hdr-Build_modes:
# > -buildmode=exe
# > Build the listed main packages and everything they import into
# > executables. Packages not named main are ignored.
GO := CGO_ENABLED=0 GOFLAGS="$(GOFLAGS)" go
GO_TEST_TIMEOUT := -timeout 30m

GOVERSION ?= $(shell cat ./.go-version)
GOARCH := $(shell go env GOARCH)
GOOS := $(shell go env GOOS)

GO_TAGS ?=
override GO_TAGS := $(GO_TAGS) -tags=opa_wasm

GOLANGCI_LINT_VERSION := v2.13.0
YAML_LINT_VERSION := 0.29.0
YAML_LINT_FORMAT ?= auto

export DOCKER_RUNNING ?= $(shell docker ps >/dev/null 2>&1 && echo 1 || echo 0)

# For image, the UID/GID is overridden so that the built binary isn't root-owned.
DOCKER_UID ?= 0
DOCKER_GID ?= 0

ifeq ($(shell tty > /dev/null && echo 1 || echo 0), 1)
DOCKER_FLAGS := --rm -it
else
DOCKER_FLAGS := --rm
endif

DOCKER := docker

# BuildKit is required for automatic platform arg injection (see Dockerfile)
export DOCKER_BUILDKIT := 1

# Supported platforms to include in image manifest lists
DOCKER_PLATFORMS := linux/amd64,linux/arm64

BIN := opa_$(GOOS)_$(GOARCH)

# Optional external configuration useful for forks of OPA
DOCKER_IMAGE ?= openpolicyagent/opa
S3_RELEASE_BUCKET ?= opa-releases
FUZZ_TIME ?= 1h
VERSION_CHECK_URL ?= #Default empty

BUILD_HOSTNAME := $(shell ./build/get-build-hostname.sh)

RELEASE_BUILD_IMAGE := golang:$(GOVERSION)-trixie

RELEASE_DIR ?= _release/$(VERSION)

ifneq (,$(VERSION_CHECK_URL))
VERSION_CHECK_SERVICE_FLAG := -X github.com/open-policy-agent/opa/internal/versioncheck.ExternalServiceURL=$(VERSION_CHECK_URL)
endif

LDFLAGS := "$(VERSION_CHECK_SERVICE_FLAG) \
	-X github.com/open-policy-agent/opa/version.Hostname=$(BUILD_HOSTNAME)"


######################################################
#
# Development targets
#
######################################################

# If you update the 'all' target make sure the 'ci-release-test' target is consistent.
.PHONY: all
all: build test perf wasm-sdk-e2e-test check

.PHONY: version
version:
	@echo $(VERSION)

.PHONY: release-dir
release-dir:
	@echo $(RELEASE_DIR)

.PHONY: generate
generate: wasm-lib-build
ifeq ($(GOOS),windows)
	cd build/tools && CGO_ENABLED=0 GOOS=linux go install tool
endif
	$(GO) generate

.PHONY: generate-proto
generate-proto:
	cd build/tools && $(GO) build -o $(CURDIR)/build/tools/bin/protoc-gen-go google.golang.org/protobuf/cmd/protoc-gen-go
	PATH="$(CURDIR)/build/tools/bin:$$PATH" protoc \
		--go_out=. \
		--go_opt=module=github.com/open-policy-agent/opa \
		v1/ir/plan.proto \
		v1/bundle/manifest.proto

.PHONY: build
build: go-build

.PHONY: image
image:
	DOCKER_UID=$(shell id -u) DOCKER_GID=$(shell id -g) $(MAKE) ci-go-ci-build-linux ci-go-ci-build-linux-static
	@$(MAKE) image-quick

.PHONY: install
install: generate
	$(GO) install $(GO_TAGS) -ldflags $(LDFLAGS)

.PHONY: test
test: go-test wasm-test

.PHONY: e2e e2e-prep
e2e: e2e-prep
	cd e2e/ && OPA=$(CURDIR)/$(BIN) $(GO) test $(GO_TAGS) -v ./...

e2e-prep: build
	cd e2e/api/compile/prisma && npm ci && DATABASE_URL='postgres://127.0.0.1/dummy' npx prisma generate
	cd e2e/ && go mod tidy

.PHONY: test-short
test-short: go-test-short

.PHONY: go-build
go-build: generate
	$(GO) build $(GO_TAGS) -o $(BIN) -ldflags $(LDFLAGS)

.PHONY: go-test
go-test: generate
	$(GO) test $(GO_TAGS),slow ./...

.PHONY: go-test-short
go-test-short: generate
	$(GO) test $(GO_TAGS) -short ./...

.PHONY: rego-test
rego-test: go-build
	OPA=$(CURDIR)/$(BIN) ./build/run-rego-tests.sh

.PHONY: race-detector
race-detector: generate
	CGO_ENABLED=1 GOFLAGS="$(GOFLAGS)" go test $(GO_TAGS),slow -race -vet=off ./...

.PHONY: test-coverage
test-coverage: generate
	$(GO) test $(GO_TAGS),slow -coverprofile=coverage.txt -covermode=atomic ./...

.PHONY: perf
perf: generate
	$(GO) test $(GO_TAGS),slow $(GO_TEST_TIMEOUT) -run=- -bench=. -benchmem ./...

.PHONY: perf-noisy
perf-noisy: generate
	$(GO) test $(GO_TAGS),slow,noisy $(GO_TEST_TIMEOUT) -run=- -bench=. -benchmem ./...

.PHONY: wasm-sdk-e2e-test
wasm-sdk-e2e-test: generate
	$(GO) test $(GO_TAGS),slow,wasm_sdk_e2e $(GO_TEST_TIMEOUT) ./internal/wasm/sdk/test/e2e

.PHONY: check
check:
ifeq ($(DOCKER_RUNNING), 1)
	$(DOCKER) run --rm -v $(shell pwd):/app:ro,Z -w /app golangci/golangci-lint:${GOLANGCI_LINT_VERSION} golangci-lint run -v
else
	@echo "Docker not installed or running. Skipping golangci run."
endif

.PHONY: fmt
fmt:
ifeq ($(DOCKER_RUNNING), 1)
	$(DOCKER) run --rm -v $(shell pwd):/app:Z -w /app golangci/golangci-lint:${GOLANGCI_LINT_VERSION} golangci-lint run -v --fix
else
	@echo "Docker not installed or running. Skipping golangci run."
endif

# build/release is a separate module, so the root `test` and `check` targets do
# not reach it.
.PHONY: check-release-tool
check-release-tool:
	cd build/release && $(GO) vet ./... && $(GO) test ./...
ifeq ($(DOCKER_RUNNING), 1)
	$(DOCKER) run --rm -v $(shell pwd):/app:ro,Z -w /app/build/release golangci/golangci-lint:${GOLANGCI_LINT_VERSION} golangci-lint run -v
else
	@echo "Docker not installed or running. Skipping golangci run."
endif

.PHONY: clean
clean: wasm-lib-clean
	rm -f opa_*_*

.PHONY: fuzz
fuzz:
	go test ./ast -fuzz FuzzParseStatementsAndCompileModules -fuzztime ${FUZZ_TIME} -v -run '^$$'

######################################################
#
# Documentation targets
#
######################################################

# The docs-% pattern target will shim to the
# makefile in ./docs
.PHONY: docs-%
docs-%:
	$(MAKE) -C docs $*

.PHONY: man
man:
	./build/gen-man.sh man

######################################################
#
# Linux distro package targets
#
######################################################

## `SECURITY.md`

# Security Policy

Please refer to the [OPA Security Policy](https://www.openpolicyagent.org/security)
for details on how to report security issues, our disclosure policy, and how to
receive notifications about security issues.

## `docs/README.md`

# Documentation and Website Development

Please see the
[contributing documentation](https://www.openpolicyagent.org/docs/contrib-docs)
for information about how to get started contributing to the OPA documentation
and website.
