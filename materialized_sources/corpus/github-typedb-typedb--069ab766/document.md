# Repository semantic capsule: typedb/typedb

- Commit: `66180f948b30a3163b380cde50b14945348501f1`
- Default branch: `master`
- Description: typedb/typedb
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

[![TypeDB](https://github.com/typedb/.github/raw/master/profile/banner.png)](https://typedb.com/)

[![Factory](https://factory.vaticle.com/api/status/typedb/typedb/badge.svg)](https://factory.vaticle.com/typedb/typedb)
[![CircleCI](https://circleci.com/gh/typedb/typedb/tree/master.svg?style=shield)](https://circleci.com/gh/typedb/typedb/tree/master)
[![GitHub release](https://img.shields.io/github/release/typedb/typedb.svg)](https://github.com/typedb/typedb/releases/latest)
[![Discord](https://img.shields.io/discord/665254494820368395?color=7389D8&label=discord&logo=discord&logoColor=ffffff)](https://typedb.com/discord)
[![Hosted By: Cloudsmith](https://img.shields.io/badge/OSS%20hosting%20by-cloudsmith-blue?logo=cloudsmith&style=flat)](https://cloudsmith.com)

# Introducing TypeDB

**TypeDB** is a next-gen database with a modern programming paradigm that lets you build data applications faster, safer, and more elegantly. Its intuitive and powerful data model unifies the strengths of relational, document and graph databases without their shortcomings. **TypeQL**, its groundbreaking query language, is declarative, functional, and strongly-typed, drastically simplifying data handling and logic. So now, even the most nested and interconnected datasets can be managed with ease. With TypeDB, we’ve reinvented the database for the modern programming era.

## Getting started

- [Deploy TypeDB](https://cloud.typedb.com) in the Cloud. Or, [download and install](https://typedb.com/docs/home/install/ce) TypeDB Community Edition.
- Explore the basics of TypeDB in our [Get Started Guide](https://typedb.com/docs/home/get-started/overview)
- Master TypeDB concepts with the [TypeDB Concepts docs](https://typedb.com/docs/core-concepts/typedb/overview) and [TypeQL Concepts docs](https://typedb.com/docs/core-concepts/typeql/)
- Discover more of TypeDB’s unique [Features](https://typedb.com/features).
- Follow the latest TypeDB news in the [TypeDB Blog](https://typedb.com/blog).
- Join our vibrant developer community over on our [Discord](https://typedb.com/discord) chat server.

##  Why TypeDB?

* TypeDB was crafted to natively express and combine diverse data features, allowing users to build advanced data models from a set of simple and intuitive building blocks.
* TypeDB's type system provides safety and flexibility at the same time, which makes both prototyping and building performant, production-ready data applications fast, elegant, and _enjoyable_.
* With TypeDB, and its query language TypeQL, we envision databases catching up with modern typed programming languages, allowing users to write clear, intuitive, and easy to maintain code.
* TypeDB comes with a mature ecosystem including language drivers and a graphical user interface: **[TypeDB Studio!](studio.typedb.com)**

## Database Fundamentals

### The schema

TypeDB schemas are based on a modern type system that natively supports inheritance and interfaces, and follows a [conceptual data modeling](https://typedb.com/docs/core-concepts/typeql/entities-relations-attributes) approach, in which user-defined types subtype (based on their function) three root types: entities, relations, and attributes.

- *Entities* are independent objects,
- *Relations* depend on their *role* interfaces played by either entities or relations,
- *Attributes* are properties with a value that can be *owned* by entities or relations.

Interface and inheritance for these types can be combined in many ways, resulting in highly expressive ways of modeling data.

```typeql
define

attribute full-name, value string;
attribute id, value string;
attribute email, sub id;
attribute employee-id, sub id;

entity user,
    owns full-name,
    owns email @unique,
    plays mentorship:trainee;
entity employee,
    owns employee-id @key,
    plays mentorship:mentor;

relation mentorship,
    relates mentor,
    relates trainee;
```

### The query language

The query language of TypeDB is [TypeQL](https://typedb.com/docs/core-concepts/typeql/). The syntax of TypeQL is fully variablizable and provides native support for polymorphic queries. The language is based on [fully declarative and composable](https://typedb.com/features#modern-language) patterns, mirroring the structure of natural language.

```typeql
match $user isa user,
    has full-name $name,
    has email $email;
# This returns all users of any type

match $user isa employee,
    has full-name $name,
    has email $email,
    has employee-id $id;
# This returns only users who are employees

match $user-type sub user;
$user isa $user-type,
    has full-name $name,
    has email $email;
# This returns all users and their type
```

### Functions

Functions, a new concept in TypeDB 3.0 and a cornerstone of TypeQL's query model, are like modularizable subqueries you can re-use and invoke whenever you want. You can learn more about them from the [TypeQL Functions Documentation](https://typedb.com/docs/core-concepts/typeql/queries-as-functions).

## Effective database engineering

TypeDB breaks down the patchwork of existing database paradigms into three fundamental ingredients: [types](https://typedb.com/features#strong-type-system), [inheritance](https://typedb.com/features#conceptual-modeling), and [interfaces](https://typedb.com/features#polymorphic-queries). This provides a unified way of working with data across all database applications, that directly impacts development:

- Make use of full [object model parity](https://typedb.com/#solve-object-relational-mismatch-entirely-within-the-database) when working with OOP
- Ensure [continuous extensibility](https://typedb.com/features#conceptual-modeling) of your data model
- Work with high-level [logical abstractions](https://typedb.com/features#conceptual-modeling) eliminating the need for physical data modeling
- Write high-clarity code with TypeQL's [near-natural](https://typedb.com/features#modern-language) queries even for the most complex databases
- Unleash the power of [fully declarative and composable](https://typedb.com/features#modern-language) patterns onto your data

## Installation and editions

### TypeDB editions

* [TypeDB Cloud](https://cloud.typedb.com) — multi-cloud DBaaS
* [TypeDB Enterprise](mailto://enterprise@typedb.com) — allows you to deploy TypeDB Cloud in your own environment
* **TypeDB Community Edition (CE)** — Open-source edition of TypeDB ← _This repository_

For a comparison of all three editions, see the [Deploy](https://typedb.com/deploy) page on our website.

### Download and run TypeDB CE

You can download TypeDB from the [GitHub Releases](https://github.com/typedb/typedb/releases). 

Or check our [Installation documentation](https://typedb.com/docs/home/install/ce).

### Compiling TypeDB CE from source using Bazel

> Note: You DO NOT NEED to compile TypeDB from the source if you just want to use TypeDB. See the _"Download and Run 
> TypeDB CE"_ section above.

1. Make sure you have the following dependencies installed on your machine:
   - [Bazel via Bazelisk](https://bazel.build/install).

2. You can build TypeDB server with TypeDB Console included with this command:

   ```sh
   $ bazel build //:assemble-typedb-all
   ```

   or either one of the following commands, depending on the targeted architecture and operating system:
   
      ```sh
      $ bazel build //:assemble-all-mac-x86_64-zip
      $ bazel build //:assemble-all-mac-arm64-zip
      $ bazel build //:assemble-all-linux-x86_64-targz
      $ bazel build //:assemble-all-linux-arm64-targz
      $ bazel build //:assemble-all-windows-x86_64-zip
      ```
   
   To build only TypeDB server, use for your corresponding platform:
   
      ```sh
      $ bazel build //:assemble-server-mac-x86_64-zip
      $ bazel build //:assemble-server-mac-arm64-zip
      $ bazel build //:assemble-server-linux-x86_64-targz
      $ bazel build //:assemble-server-linux-arm64-targz
      $ bazel build //:assemble-server-windows-x86_64-zip
      ```
   
   The commands above output to: `bazel-bin/`.

3. If you're on a Mac and would like to run any `bazel test` commands, you will need to install:
   - snappy: `brew install snappy`
   - jemalloc: `brew install jemalloc`

### Compiling TypeDB CE from source using Cargo

**For macs:**

Install prerequisites:
1. Rustup
2. `brew install protoc`

## Resources

### Developer resources

- Documentation: https://typedb.com/docs
- Discord Chat Server: https://typedb.com/discord
- Community Projects: https://github.com/typedb-osi

### Useful links

If you want to begin your journey with TypeDB, you can explore the following resources:

* More on TypeDB's [features](https://typedb.com/features)
* In-depth dive into TypeDB's [philosophy](https://typedb.com/docs/home/what-is-typedb)
* [TypeDB Get Started Guide](https://typedb.com/docs/home/get-started/overview) 
* [TypeDB Academy](https://typedb.com/docs/academy)
* **[TypeQL](https://github.com/typedb/typeql)**
* **[TypeDB Studio](https://github.com/typedb/typedb-studio)**

## Contributions

TypeDB and TypeQL are built using various open-source frameworks and technologies throughout its evolution. 
Today TypeDB and TypeQL use
[RocksDB](https://rocksdb.org),
[Rust](https://www.rust-lang.org/),
[pest](https://pest.rs/),
[Bazel](https://bazel.build),
[gRPC](https://grpc.io),
and [ZeroMQ](https://zeromq.org).

Thank you!

In the past, TypeDB was enabled by various open-source products and communities that we are hugely thankful to:
[Speedb](https://www.speedb.io/),
[ANTLR](https://www.antlr.org),
[Apache Cassandra](http://cassandra.apache.org), 
[Apache Hadoop](https://hadoop.apache.org), 
[Apache Spark](http://spark.apache.org), 
[Apache TinkerPop](http://tinkerpop.apache.org),
[Caffeine](https://github.com/ben-manes/caffeine),
[JanusGraph](http://janusgraph.org),
and [SCIP](https://www.scipopt.org).

### Package hosting
Package repository hosting is graciously provided by [Cloudsmith](https://cloudsmith.com).
Cloudsmith is the only fully hosted, cloud-native, universal package management solution, that
enables your organization to create, store and share packages in any format, to any place, with total
confidence.

## Licensing

It's released under the Mozilla Public License 2.0 (MPL 2.0).
For license information, please see [LICENSE](https://github.com/typedb/typedb/blob/master/LICENSE). 

## `CONTRIBUTING.md`

## Want to contribute?
Your contributions are warmly welcomed! To make the process as smooth as possible, please note:

### Large Contributions
Before starting work on a major feature, architectural change, or large refactor, please get in touch to discuss your idea. This ensures your work aligns with the project roadmap and has the best chance of being merged.

You can do this via:

- [GitHub Issues](../../issues)
- [Discord](https://typedb.com/discord)

Note: Large PRs submitted without prior discussion may be closed without review.

### Bug Fixes & Small Changes
Small improvements, documentation fixes, and bug reports are welcome via direct Pull Request or Issue.

### Code Quality
All submissions, including those from core maintainers, undergo a mandatory code review process.

## `Cargo.toml`


# Generated by TypeDB Cargo sync tool.
# Do not modify this file.

features = {}

[package]
	name = "typedb_server_bin"
	edition = "2024"
	version = "0.0.0"

[dev-dependencies]

	[dev-dependencies.test_utils]
		workspace = true

	[dev-dependencies.xoshiro]
		workspace = true

	[dev-dependencies.query]
		workspace = true

	[dev-dependencies.storage]
		workspace = true

	[dev-dependencies.steps]
		workspace = true

	[dev-dependencies.rand]
		workspace = true

	[dev-dependencies.http_steps]
		workspace = true

	[dev-dependencies.diagnostics]
		workspace = true

	[dev-dependencies.answer]
		workspace = true

	[dev-dependencies.executor]
		workspace = true

	[dev-dependencies.function]
		workspace = true

	[dev-dependencies.options]
		workspace = true

	[dev-dependencies.typeql]
		workspace = true

	[dev-dependencies.rand_core]
		workspace = true

	[dev-dependencies.lending_iterator]
		workspace = true

[dependencies]

	[dependencies.tokio]
		workspace = true

	[dependencies.server]
		workspace = true

	[dependencies.database]
		workspace = true

	[dependencies.tracing]
		workspace = true

	[dependencies.resource]
		workspace = true

	[dependencies.clap]
		workspace = true

	[dependencies.logger]
		workspace = true

	[dependencies.fail_point]
		workspace = true

	[dependencies.sentry]
		workspace = true

[[test]]
	path = "tests/assembly/assembly.rs"
	name = "test_assembly"

[[test]]
	path = "tests/assembly/fail_points.rs"
	name = "test_fail_points"

[[test]]
	path = "tests/benchmarks/concurrent_ops/bench_concurrency.rs"
	name = "bench_concurrency"

[[test]]
	path = "tests/benchmarks/iam/bench_iam.rs"
	name = "bench_iam"

[[test]]
	path = "tests/behaviour/connection/main.rs"
	name = "test_connection"

[[test]]
	path = "tests/behaviour/concept/main.rs"
	name = "test_concept"

[[test]]
	path = "tests/behaviour/service/http/connection/database.rs"
	name = "test_http_database"

[[test]]
	path = "tests/behaviour/service/http/connection/transaction.rs"
	name = "test_http_transaction"

[[test]]
	path = "tests/behaviour/service/http/driver/concept.rs"
	name = "test_http_driver_concept"

[[test]]
	path = "tests/behaviour/service/http/driver/http.rs"
	name = "test_http_driver_http"

[[test]]
	path = "tests/behaviour/service/http/driver/query.rs"
	name = "test_http_driver_query"

[[test]]
	path = "tests/behaviour/service/http/driver/user.rs"
	name = "test_http_driver_user"

[[test]]
	path = "tests/behaviour/service/http/driver/connection.rs"
	name = "test_http_driver_connection"

[[test]]
	path = "tests/behaviour/service/http/debug/debug.rs"
	name = "test_http_debug"

[[test]]
	path = "tests/behaviour/query/main.rs"
	name = "test_query"

[[test]]
	path = "tests/behaviour/debug/debug.rs"
	name = "test_debug"

[[bin]]
	path = "main.rs"
	name = "typedb_server_bin"


[workspace]
	resolver = "2"
	members = ["database/tools", "database", "answer", "util/test", "util/project", "durability/tests/crash/streamer", "durability/tests/crash/recoverer", "durability/tests/common", "durability", "ir", "tests/behaviour/steps", "tests/behaviour/steps/params", "tests/behaviour/service/http/http_steps", "admin", "admin/client", "encoding/tests", "encoding", "server", "server/service/admin/proto", "user", "function", "storage/tests", "storage", "system", "common/options", "common/structural_equality", "common/logger", "common/cache", "common/bytes", "common/lending_iterator", "common/primitive", "common/fail_point", "common/concurrency", "common/iterator", "common/error", "concept/tests", "concept", "diagnostics", "executor", "resource", "query", "compiler"]

	[workspace.dependencies]

		[workspace.dependencies.hyper-util]
			features = ["client", "client-legacy", "default", "http1", "http2", "server", "server-auto", "service", "tokio"]
			version = "0.1.20"
			default-features = false

		[workspace.dependencies.logger]
			path = "common/logger"
			features = []
			default-features = false

		[workspace.dependencies.fail_point]
			path = "common/fail_point"
			features = []
			default-features = false

		[workspace.dependencies.rpassword]
			features = []
			version = "7.5.3"
			default-features = false

		[workspace.dependencies.rand]
			features = ["alloc", "default", "getrandom", "libc", "rand_chacha", "small_rng", "std", "std_rng"]
			version = "0.8.6"
			default-features = false

		[workspace.dependencies.tokio-test]
			features = []
			version = "0.4.5"
			default-features = false

		[workspace.dependencies.iterator]
			path = "common/iterator"
			features = []
			default-features = false

		[workspace.dependencies.rustyline]
			features = ["custom-bindings", "fd-lock", "radix_trie", "with-file-history"]
			version = "15.0.0"
			default-features = false

		[workspace.dependencies.tokio-rustls]
			features = ["logging", "ring", "tls12"]
			version = "0.26.4"
			default-features = false

		[workspace.dependencies.executor]
			path = "executor"
			features = []
			default-features = false

		[workspace.dependencies.xxhash-rust]
			features = ["xxh3"]
			version = "0.8.15"
			default-features = false

		[workspace.dependencies.options]
			path = "common/options"
			features = []

## `docs/README.md`

# README

Blueprints are both meant to:

* **record existing architecture** of TypeDB
* **foresee and outline future architectural** changes

## Disclaimer 

Be wary of typos and logic mistakes (and if you find some, please **report or fix** them!)

## Blueprints

Descriptions of TypeDB's type system, query processing, and evaluation algorithms. The current scope is:

1. **Type system** grammar and rules
2. **TypeQL schema** definition semantics and operation
3. **TypeQL read** query semantics and operation
4. **TypeQL write** query semantics and operation
5. **TypeQL function** syntax
6. **TypeDB query planner** architecture
7. **TypeDB query execution** architecture

## Archived

An old version of the "TypeDB specification".
