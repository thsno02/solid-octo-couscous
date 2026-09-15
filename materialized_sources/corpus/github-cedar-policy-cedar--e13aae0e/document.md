# Repository semantic capsule: cedar-policy/cedar

- Commit: `2f4019fd645cc8d4a4c0c1f8bd0280c77d754e28`
- Default branch: `main`
- Description: cedar-policy/cedar
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# Cedar

![Cedar Logo](./logo.svg)

[![Crates.io](https://img.shields.io/crates/v/cedar-policy.svg)](https://crates.io/crates/cedar-policy)
[![docs.rs](https://img.shields.io/docsrs/cedar-policy)](https://docs.rs/cedar-policy/latest/cedar_policy/)
![nightly](https://github.com/cedar-policy/cedar/actions/workflows/nightly_build.yml/badge.svg)
![nightly-deps](https://github.com/cedar-policy/cedar/actions/workflows/nightly_build_downstream.yml/badge.svg)
![audit](https://github.com/cedar-policy/cedar/actions/workflows/cargo_audit.yml/badge.svg)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/11398/badge)](https://www.bestpractices.dev/projects/11398)

This repository contains source code of the Rust crates that implement the [Cedar](https://www.cedarpolicy.com/) policy language.

Cedar is a language for writing and enforcing authorization policies in your applications. Using Cedar, you can write policies that specify your applications' fine-grained permissions. Your applications then authorize access requests by calling Cedar's authorization engine. Because Cedar policies are separate from application code, they can be independently authored, updated, analyzed, and audited. You can use Cedar's validator to check that Cedar policies are consistent with a declared schema which defines your application's authorization model.

Cedar is:

### Expressive

Cedar is a simple yet expressive language that is purpose-built to support authorization use cases for common authorization models such as RBAC and ABAC.

### Performant

Cedar is fast and scalable. The policy structure is designed to be indexed for quick retrieval and to support fast and scalable real-time evaluation, with bounded latency.

### Analyzable

Cedar is designed for analysis using Automated Reasoning. This enables analyzer tools capable of optimizing your policies and proving that your security model is what you believe it is.

## Using Cedar

Cedar can be used in your application by depending on the [`cedar-policy` crate](https://crates.io/crates/cedar-policy).

Just add `cedar-policy` as a dependency by running

```sh
cargo add cedar-policy
```

## Crates in This Workspace

* [cedar-policy](./cedar-policy) : Main crate for using Cedar to authorize access requests in your applications, and validate Cedar policies against a schema
* [cedar-policy-symcc](./cedar-policy-symcc) : Crate containing the Cedar symbolic compiler, enabling verification of properties about your Cedar policies with concrete counterexamples
* [cedar-policy-cli](./cedar-policy-cli) : Crate containing a simple command-line interface (CLI) for interacting with Cedar
* [cedar-language-server](./cedar-language-server) : Contains the implementation for the Cedar Langauge Server
* [cedar-wasm](./cedar-wasm) : Crate defining the wasm interface for Cedar, enabling use with JavaScript and TypeScript
* [cedar-policy-core](./cedar-policy-core) : Internal crate containing the Cedar parser, evaluator, typechecker, and other core components
* [cedar-policy-formatter](./cedar-policy-formatter) : Internal crate containing an auto-formatter for Cedar policies
* [cedar-testing](./cedar-testing) : Internal crate containing integration testing code

## Quick Start

Let's put the policy in `policy.cedar` and the entities in `entities.json`.

`policy.cedar`:

```cedar
permit (
  principal == User::"alice",
  action == Action::"view",
  resource in Album::"jane_vacation"
);
```

This policy specifies that `alice` is allowed to view the photos in the `"jane_vacation"` album.

`entities.json`:

```json
[
    {
        "uid": { "type": "User", "id": "alice"} ,
        "attrs": {"age": 18},
        "parents": []
    },
    {
        "uid": { "type": "Photo", "id": "VacationPhoto94.jpg"},
        "attrs": {},
        "parents": [{ "type": "Album", "id": "jane_vacation" }]
    },
    {
        "uid": { "type": "Photo", "id": "SecretPhoto94.jpg"},
        "attrs": {},
        "parents": [{ "type": "Album", "id": "jane_secrets" }]
    }
]

```

Cedar represents principals, resources, and actions as entities. An entity has a type (e.g., `User`) and an id (e.g., `alice`). They can also have attributes (e.g., `User::"alice"`'s `age` attribute is the integer `18`).

Now, let's test our policy with the CLI:

```sh
 cargo run --bin cedar authorize \
    --policies policy.cedar \
    --entities entities.json \
    --principal 'User::"alice"' \
    --action 'Action::"view"' \
    --resource 'Photo::"VacationPhoto94.jpg"'
```

CLI output:

```
ALLOW
```

This request is allowed because `VacationPhoto94.jpg` belongs to `Album::"jane_vacation"`, and `alice` can view photos in `Album::"jane_vacation"`.

Let's test out policy again with a photo that `alice` shouldn't have access:

```sh
 cargo run --bin cedar authorize \
    --policies policy.cedar \
    --entities entities.json \
    --principal 'User::"alice"' \
    --action 'Action::"view"' \
    --resource 'Photo::"SecretPhoto94.jpg"'
```

CLI output:

```
DENY
```

This request is denied because `SecretPhoto94.jpg` belongs to `Album::"jane_secrets"`, and `alice` doesn't have explicit permission to view photos from this Album. 

If you'd like to see more details on what can be expressed as Cedar policies, see the [documentation](https://docs.cedarpolicy.com).

Examples of how to use Cedar in an application are contained in the repository [cedar-examples](https://github.com/cedar-policy/cedar-examples). [TinyTodo](https://github.com/cedar-policy/cedar-examples/tree/main/tinytodo) is a simple task list management app whose users' requests, sent as HTTP messages, are authorized by Cedar. It shows how you can integrate Cedar into your own Rust program.

## Documentation

General documentation for Cedar is available at [docs.cedarpolicy.com](https://docs.cedarpolicy.com), with source code in the [cedar-policy/cedar-docs](https://github.com/cedar-policy/cedar-docs/) repository.

Generated documentation for the latest version of the Rust crates can be accessed
[on docs.rs](https://docs.rs/cedar-policy).

If you're looking to integrate Cedar into a production system, please be sure to read the [security best practices](https://docs.cedarpolicy.com/other/security.html)

## Building

To build, simply run `cargo build` (or `cargo build --release`).

## What's New

We maintain changelogs for our public-facing crates:
[cedar-policy](https://github.com/cedar-policy/cedar/blob/main/cedar-policy/CHANGELOG.md) and
[cedar-policy-cli](https://github.com/cedar-policy/cedar/blob/main/cedar-policy-cli/CHANGELOG.md).
Changelogs for all release branches and the `main` branch are all maintained on
the `main` branch of this repository; you can see the most up-to-date changelogs
by following the links above.

For a list of the current and past releases, see [crates.io](https://crates.io/crates/cedar-policy) or [Releases](https://github.com/cedar-policy/cedar/releases).

## Backward Compatibility Considerations

Cedar is written in Rust and you will typically depend on Cedar via Cargo. Cargo makes sane choices for the majority of projects, but your needs may differ. If you don't want automatic updates to Cedar, then you can pin to a specific version in your `Cargo.toml`. For example:

```toml
[dependencies]
cedar-policy = "=2.4.2"
```

Note that this is different from:

```toml
[dependencies]
cedar-policy = "2.4.2"
```

Which expresses that 2.4.2 is the minimum version of Cedar you accept, and you implicitly accept anything newer that is semver-compatible. See <https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html>.

## Security

See [SECURITY](SECURITY.md) for more information.

## Contributing

We welcome contributions from the community. Please either file an issue, or see [CONTRIBUTING](CONTRIBUTING.md)

## License

This project is licensed under the Apache-2.0 License.

## `CONTRIBUTING.md`

# Contributing to Cedar

Cedar is a community project that is built and maintained by people just like **you**. We're glad you're interested in helping out. There are several different ways you can do it, but before we talk about that, let's talk about how to get started.

## First Things First

1. **When in doubt, open an issue** - For almost any type of contribution, the first step is opening an issue. Even if you think you already know what the solution is, writing down a description of the problem you're trying to solve will help everyone get context when they review your pull request. If it's truly a trivial change (e.g. spelling error), you can skip this step — but as the subject says, when in doubt, [open an issue](https://github.com/cedar-policy/cedar/issues). DO NOT open an issue for security-related issues. See [SECURITY](SECURITY.md).
2. **Only submit your own work**  (or work you have sufficient rights to submit) - Please make sure that any code or documentation you submit is your work or you have the rights to submit. We respect the intellectual property rights of others.

## Ways to Contribute

### Bug Reports

A bug is when software behaves in a way that you didn't expect and the developer didn't intend. To help us understand what's going on, we first want to make sure you're working from the latest version. Please make sure you're testing against the latest version.

Once you've confirmed that the bug still exists in the latest version, you'll want to check to make sure it's not something we already know about on the [open issues GitHub page](https://github.com/cedar-policy/cedar/issues).

If you've upgraded to the latest version and you can't find it in our open issues list, then you'll need to tell us how to reproduce it. To make the behavior as clear as possible, please provide your policies, entities, request, and CLI commands.

The easier it is for us to recreate your problem, the faster it is likely to be fixed. Please try to include as much information as you can. Details like these are incredibly useful:

* A reproducible test case or series of steps
* The version of our code being used
* Any modifications you've made relevant to the bug
* Anything unusual about your environment or deployment

### Feature Requests

If you've thought of a way that Cedar could be better, we want to hear about it. We track feature requests using GitHub, so please feel free to open an issue which describes the feature you would like to see, why you need it, and how it should work.

### Documentation Changes

If you would like to contribute to the documentation hosted on docs.cedarpolicy.com, please do so in the [documentation](https://github.com/cedar-policy/cedar-docs) repo.

### Contributing Code

As with other types of contributions, the first step is to [**open an issue on GitHub**](https://github.com/cedar-policy/cedar/issues). Opening an issue before you make changes makes sure that someone else isn't already working on that particular problem. It also lets us all work together to find the right approach before you spend a bunch of time on a PR. So again, when in doubt, open an issue.

If you would like to propose a change to the Cedar language, or suggest a substantial new feature, please [follow the RFC process](https://github.com/cedar-policy/rfcs).

## Changelog

Cedar maintains changelogs for the public-facing crates [cedar-policy](https://github.com/cedar-policy/cedar/blob/main/cedar-policy/CHANGELOG.md) and [cedar-policy-cli](https://github.com/cedar-policy/cedar/blob/main/cedar-policy-cli/CHANGELOG.md), which adhere to the [Keep A Changelog](https://keepachangelog.com/en/1.0.0/) format. The purpose of the changelog is for the contributors and maintainers to incrementally build release notes throughout the development process to avoid the painful and error-prone process of attempting to compile the release notes at release time. On each release the "unreleased" entries of the changelog are moved under the appropriate header. Also, incrementally building the changelog provides a concise, human-readable list of significant features that have been added to the unreleased version under development. Changelogs for all release branches and the `main` branch are all maintained on the `main` branch of this repository only; you can see the most up-to-date changelogs by following the links above.

### Which changes require a changelog entry?

Changelogs are intended for developers integrating with libraries and APIs, and end-users interacting with Cedar policies (collectively referred to as "user"). In short, any change that a user of Cedar might want to be aware of should be included in the changelog. The changelog is *not* intended to replace the git commit log that developers of Cedar itself rely upon. The following are some examples of changes that should be in the changelog:

* A newly added feature
* A fix for a user-facing bug
* Dependency updates
* Fixes for security issues

The following are some examples where a changelog entry is not necessary:

* Adding, modifying, or fixing tests
* An incremental PR for a larger feature (such features should include *one* changelog entry for the feature)
* Documentation changes or code refactoring
* Build-related changes

### Where should I put my changelog entry?

Add your entry under the "Unreleased" section, as part of the same PR that introduces the change.
In the (rarer) case that your PR is to a `release/X.Y.Z` branch rather than `main`, make a separate PR to `main` which adds the changelog entry under the appropriate version header of the `main` changelog.

## Review Process

We deeply appreciate everyone who takes the time to make a contribution. We will review all contributions as quickly as possible. As a reminder, [opening an issue](https://github.com/cedar-policy/cedar/issues) discussing your change before you make it is the best way to smooth the PR process. This will prevent a rejection because someone else is already working on the problem, or because the solution is incompatible with the architectural direction.
Also take a minute to review our [style guide](style_guide.md). Most of this is handled by automated tooling, but there are a few conventions around documentation and error messages you should review before making a larger contribution.

During the PR process, expect that there will be some back-and-forth. Please try to respond to comments in a timely fashion, and if you don't wish to continue with the PR, let us know. If a PR takes too many iterations for its complexity or size, we may reject it. Additionally, if you stop responding we may close the PR as abandoned. In either case, if you feel this was done in error, please add a comment on the PR.

If we accept the PR, a maintainer will merge your change and usually take care of backporting it to appropriate branches ourselves.

If we reject the PR, we will close the pull request with a comment explaining why. This decision isn't always final: if you feel we have misunderstood your intended change or otherwise think that we should reconsider then please continue the conversation with a comment on the PR and we'll do our best to address any further points you raise.

 Before sending us a pull request, please ensure that:

1. You are working against the latest source on the *main* branch.
2. You check existing open, and recently merged, pull requests to make sure someone else hasn't addressed the problem already.
3. You open an issue to discuss any significant work - we would hate for your time to be wasted.

To send us a pull request, please:

1. Fork the repository.
2. Modify the source; please focus on the specific change you are contributing. If you also reformat all the code, it will be hard for us to focus on your change.
3. Ensure local tests pass.
4. Commit to your fork using clear commit messages.
5. Send us a pull request, answering any default questions in the pull request interface.
6. Pay attention to any automated CI failures reported in the pull request, and stay involved in the conversation.

GitHub provides additional document on [forking a repository](https://help.github.com/articles/fork-a-repo/) and [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Finding Ways to Contribute

Looking at the existing issues is a great way to find something to contribute on. Looking at any issues labeled as 'help-wanted' or 'good-first-issue' is a great place to start.

## Code of Conduct

This project follows the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/main/code-of-conduct.md). For more information see the [Code of Conduct FAQ](https://www.cncf.io/conduct/faq/) or contact [conduct@cncf.io](mailto:conduct@cncf.io) with any additional questions or comments.

## Security Issues

If you think you have discovered a security issue related to Cedar, **please write to us** at [cedar-policy-security@lists.cncf.io ](mailto:cedar-policy-security@lists.cncf.io ); do **NOT** open a public issue. See [SECURITY](SECURITY.md).

## Licensing

See the [LICENSE](LICENSE) file for our project's licensing. We will ask you to confirm the licensing of your contribution.

## `Cargo.toml`

[workspace]
members = [
	"cedar-policy",
	"cedar-policy-core",
	"cedar-policy-formatter",
	"cedar-policy-cli",
	"cedar-policy-symcc",
	"cedar-testing",
	"cedar-wasm",
	"cedar-language-server",
]

resolver = "2"

# cargo-dist config. Workspace default `dist = false`; `cedar-policy-cli`
# opts in via its own `[package.metadata.dist]`.
[workspace.metadata.dist]
cargo-dist-version = "0.32.0"
ci = "github"
dist = false
installers = ["shell", "powershell"]
tag-namespace = "cedar-policy-cli"
targets = [
    "x86_64-unknown-linux-gnu",
    "aarch64-unknown-linux-gnu",
    "x86_64-apple-darwin",
    "aarch64-apple-darwin",
    "x86_64-pc-windows-msvc",
]
include = ["NOTICE", "THIRD_PARTY_LICENSES.txt"]
pr-run-mode = "plan"
install-updater = false
post-announce-jobs = ["./build_experimental", "./set_release_title"]

# SHA-pin the actions cargo-dist injects into the generated workflow.
[workspace.metadata.dist.github-action-commits]
"actions/checkout" = "df4cb1c069e1874edd31b4311f1884172cec0e10"            # v6.0.3
"actions/upload-artifact" = "043fb46d1a93c77aae656e7c1c64a875d1fc6a0a"     # v7.0.1
"actions/download-artifact" = "3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c"   # v8

# Enable global integer overflow detection for the release profile
[profile.release]
overflow-checks = true

# The profile that 'dist' will build with
[profile.dist]
inherits = "release"
lto = "thin"

[profile.bench]
overflow-checks = true
debug = "line-tables-only"  # this adds more debug symbols/info to the binary than the default for `release` (which is `none`)

# https://insta.rs/docs/quickstart/ recommends compiling `insta` and `similar` in release mode, even for dev dependency
[profile.dev.package]
insta.opt-level = 3
similar.opt-level = 3

# Keys that packages can inherit
[workspace.package]
# Check the minimum supported Rust version with `cargo install cargo-msrv && cargo msrv --min 1.X.0` where `X` is something lower than the version noted here (to confirm that versions lower than the one noted here _don't_ work)
rust-version = "1.89"
version = "4.13.0"
homepage = "https://cedarpolicy.com"
keywords = ["cedar", "authorization", "policy", "security"]
categories = ["compilers", "config"]
license = "Apache-2.0"
edition = "2021"
repository = "https://github.com/cedar-policy/cedar"

# We actually deny all rustc warnings in CI, but it's clearer if we explicitly
# "deny" here even if setting to "warn" has the same effect.
[workspace.lints.rust]
unsafe_code = "forbid"
unexpected_cfgs = { level = 'deny', check-cfg = ['cfg(kani)', 'cfg(fuzzing)'] }
missing_debug_implementations = "deny"
rust-2018-idioms = "deny"
unused_assignments = "allow" # In Rust 1.92 this one erroneously identifies some fields in error structs as unused, when they are actually used in the `#[error]` attribute

# For clippy lints CI will only block on errors, so setting one to "warn" just
# means we'll see it in local runs.
[workspace.lints.clippy]
nursery = { level = "warn", priority = -1 }
# Enabling some pedantic lints incrementally
cast_lossless = "warn"
cast_possible_truncation = "warn"
cloned_instead_of_copied = "warn"
format_collect = "warn"
format_push_string = "warn"
implicit_clone = "warn"
inconsistent_struct_constructor = "warn"
inefficient_to_string = "warn"
large_types_passed_by_value = "warn"
needless_pass_by_value = "warn"
option_as_ref_cloned = "warn"
option_option = "warn"
redundant_clone = "deny"
ref_option = "warn"
ref_option_ref = "warn"
trivially_copy_pass_by_ref = "warn"

# When overriding lints, require `expect` instead of `allow`, and require a reason
allow_attributes = "deny"
allow_attributes_without_reason = "deny"
should_panic_without_expect = "deny"

# These lints may be worth enforcing, but cause a lot of noise at the moment.
use_self = "allow"
option_if_let_else = "allow"
redundant_pub_crate = "allow"
too_long_first_doc_paragraph = "allow"
# We don't want to enforce these lints.
missing_const_for_fn = "allow"
needless_doctest_main = "allow"
# see #878
result_large_err = "allow"
large_enum_variant = "allow"

# Error on potential panics
unwrap_used = "deny"
expect_used = "deny"
fallible_impl_from = "deny"
unreachable = "deny"
indexing_slicing = "deny"
string_slice = "deny"
panic = "deny"
todo = "deny"
unimplemented = "deny"

## `SECURITY.md`

# SECURITY.md

## Reporting a Vulnerability

If you think you have discovered a security issue related to Cedar, **please write to us** at [cedar-policy-security@lists.cncf.io ](mailto:cedar-policy-security@lists.cncf.io ); do **NOT** open a public issue. Along with your notification email, please provide any supporting material (proof-of-concept code, tool output, etc.) that would be useful in helping us understand the nature and severity of the security concern.

We will send a non-automated acknowledgement email reply within 1 business day followed by an initial assessment of the issue within 5 business days. Subsequently, we will work in partnership with you to assess any impact of the issue and prepare a security advisory (including any patches with appropriate fix) as needed.

If we confirm that your report represents a security issue in Cedar, we will work with you to agree on an embargo period (typically at least 2 weeks AFTER any necessary development time) which will provide enough time to test our proposed fix and develop patches prior to any broader or more public disclosure. At the end of the embargo period, Cedar maintainers will publicly release information about the security issue together with the patches that mitigate it.
