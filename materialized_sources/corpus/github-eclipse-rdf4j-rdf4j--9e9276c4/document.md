# Repository semantic capsule: eclipse-rdf4j/rdf4j

- Commit: `a6352dc2c21a7b1fb521543948f4c752ed9b9385`
- Default branch: `main`
- Description: eclipse-rdf4j/rdf4j
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# Welcome to the Eclipse RDF4J repository

![RDF4J](https://github.com/eclipse/rdf4j/blob/main/site/static/images/rdf4j-logo-orange-114.png)

This is the main code repository for the Eclipse RDF4J project. 

[![main status](https://github.com/eclipse/rdf4j/workflows/main%20status/badge.svg)](https://github.com/eclipse/rdf4j/actions?query=workflow%3A%22main+status%22)
[![develop status](https://github.com/eclipse/rdf4j/workflows/develop%20status/badge.svg)](https://github.com/eclipse/rdf4j/actions?query=workflow%3A%22develop+status%22) [![Join the chat at https://gitter.im/eclipse/rdf4j](https://badges.gitter.im/eclipse/rdf4j.svg)](https://gitter.im/eclipse/rdf4j?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Visit the [project website](https://rdf4j.org/) for news, documentation, and downloadable releases. For support questions, comments, and any ideas for improvements you'd like to discuss, please use our [discussion forum](https://github.com/eclipse/rdf4j/discussions). If you have found a bug or have a very specific feature/improvement request, you can also use our [issue tracker](https://github.com/eclipse/rdf4j/issues) to report it.

## Installation and usage

For installation and usage instructions of the RDF4J Workbench and Server applications, see [RDF4J Server and Workbench](https://rdf4j.org/documentation/tools/server-workbench). 

For installation and usage instructions of the RDF4J Java libaries, see [Programming with RDF4J](https://rdf4j.org/documentation/programming). 

### Building from source

RDF4J is a multi-module [maven](https://maven.apache.org/index.html) project. It can be compiled, tested, and installed with the [usual maven lifecycle phases](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html) from the command line, for example:

- `mvn verify` - compiles and runs all tests
- `mvn package` - compiles, tests, and packages all modules
- `mvn install` - compiles, tests, packages, and installs all artifacts in the local maven repository
- `mvn -Pquick install` - compiles, packages and installs everything (skipping test execution)

These commands can be run from the project root to execute on the entire project or (if you're only interested in working with a particular module) from any module's subdirectory. 

To build the full RDF4J project, including onejar and SDK files and full aggregated javadoc, from source, run:

     mvn -Passembly package

The SDK and onejar will be available in `assembly/target`. Individual module jars and wars will be in `target/` in their respective modules. 

Modern IDEs like Eclipse, IntelliJ IDEA, or Netbeans can of course also be used to build, test, and run (parts of) the project. 

## Keen to contribute?

We welcome contributions! Whether you have a new feature you want to add, or a bug you want to fix, or a bit of documentation you want to improve, it's all very welcome. Have a look in our [issue tracker](https://github.com/eclipse/rdf4j/issues) for any open problems, in particular the ones marked as [good first issue](https://github.com/eclipse/rdf4j/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) or as [help wanted](https://github.com/eclipse/rdf4j/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22). Or feel free to add your own new issue if what you have in mind is not there yet.

To get started on your contribution, please first read our [Contributor
guidelines](https://github.com/eclipse/rdf4j/blob/main/CONTRIBUTING.md).

The short version:

1. Digitally sign the [Eclipse Contributor Agreement (ECA)](https://www.eclipse.org/legal/ECA.php), as follows: 
     * [Register an Eclipse account](https://accounts.eclipse.org/user/register). **Important**: Use the same email address that you will use on Git commits as the author address. 
     * Open the [ECA form](https://accounts.eclipse.org/user/eca) and complete it. See the [ECA FAQ](https://www.eclipse.org/legal/ecafaq.php) for more info. 
2. Create an issue in the [issue tracker](https://github.com/eclipse/rdf4j/issues) that describes your improvement, new feature, or bug fix - or if you're picking up an existing issue, comment on that issue that you intend to provide a solution for it.
3. Fork the GitHub repository.
4. Create a new branch (starting from main) for your changes. Name your branch like this: `GH-1234-short-description-here` where 1234 is the Github issue number.
5. Make your changes on this branch. Apply the [RDF4J code formatting guidelines](https://github.com/eclipse/rdf4j/blob/main/CONTRIBUTING.md#code-formatting). Don't forget to include unit tests.
7. Run `mvn verify` from the project root to make sure all tests succeed (both your own new ones, and existing).
8. Commit your changes into the branch. Make sure the commit author name and e-mail correspond to what you used to sign the ECA. Use meaningful commit messages. Reference the issue number in each commit message (for example "GH-276: added null check").
9. Once your fix is complete, put it up for review by opening a Pull Request against the main branch in the central Github repository. If you have a lot of commits on your PR, make sure to [squash your commits](https://rdf4j.org/documentation/developer/squashing).

These steps are explained in more detail in the [Contributor
guidelines](https://github.com/eclipse/rdf4j/blob/main/CONTRIBUTING.md).

You can find more detailed information about our development and release processes in the [Developer Workflow and Project Management](https://rdf4j.org/documentation/developer/) documentation.

## `AGENTS.md`

# You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:

   1.1) Policy-based rules, mandatory prerequisites, and constraints.

   1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.

     1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.

   1.3) Other prerequisites (information and/or actions needed).

   1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?

   2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk.  
   **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.

   3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.

   3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.

   3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?

   4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:

   5.1) Using available tools and their capabilities  
   5.2) All policies, rules, checklists, and constraints  
   5.3) Previous observations and conversation history  
   5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.

   6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them.

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.

   7.1) Resolve conflicts using the order of importance in #1.

   7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.

     7.2.1) To check for whether an option is relevant, reason about all information sources from #5.  

     7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.

   7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.

   8.1) Don't be dissuaded by time taken or user frustration.

   8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.

---

## Read‑Me‑Now: Proportional Test‑First Rule

**Default:** Use **test‑first (TDD)** for any change that alters externally observable behavior.

**Proportional exceptions:** You may **skip writing a new failing test** *only* when **all** Routine B gates (below) pass, or when using Routine C (Spike/Investigate) with **no production code changes**.

**You may not touch production code for behavior‑changing work until a smallest‑scope failing automated test exists inside this repo and you have captured its report snippet.** A user‑provided stack trace or “obvious” contract violation is **not** a substitute for an in‑repo failing test.

**Auto‑stop:** If you realize you patched production before creating/observing the failing test for behavior‑changing work, **stop**, revert the patch, and resume from “Reproduce first”.

**Traceability trio (must appear in your handoff):**
1. **Descritpion** (what you’re about to do)
2. **Evidence** (Surefire/Failsafe snippet from this repo)
3. **Plan** (one and only one `in_progress` step)

It is illegal to `-am` when running tests!
It is illegal to `-q` when running tests!
Always keep untracked artifacts!

> **Clarification:** For **strictly behavior‑neutral refactors** that are already **fully exercised by existing tests**, or for **bugfixes with an existing failing test**, you may use **Routine B — Change without new tests**. In that case you must capture **pre‑change passing evidence** at the smallest scope that hits the code you’re about to edit, prove **Hit Proof**, then show **post‑change passing evidence** from the **same selection**.
> **No exceptions for any behavior‑changing change** — for those, you must follow **Routine A — Full TDD** or **Routine D — ExecPlans**.

---

## Four Routines: Choose Your Path

**Routine A — Full TDD**
**Routine B — Change without new tests (Proportional, gated)**
**Routine C — Spike/Investigate (No production changes)**
**Routine D — ExecPlans: Complex features or significant refactors**

### Decision quickstart

1. **Is ExecPlans required (complex feature, significant refactor, etc. or explicitly requested by the user)?**
   → **Yes:** **Routine D (ExecPlans)**. Use an ExecPlan (as described in .agent/PLANS.md) from design to implementation.
   → **No:** continue.

3. **Does a failing test already exist in this repo that pinpoints the issue?**
→ **Yes:** **Routine B (Bugfix using existing failing test).**
→ **No:** continue.

4. **Is the edit strictly behavior‑neutral, local in scope, and clearly hit by existing tests?**
→ **Yes:** **Routine B (Refactor/micro‑perf/documentation/build).**
→ **No or unsure:** continue.

5. **Is new externally observable behavior required?**
   → **Yes:** **Routine A (Full TDD)**. Add the smallest failing test first.
   → **No:** continue.

6. **Is this purely an investigation/design spike with no production code changes?**
   → **Yes:** **Routine C (Spike/Investigate).**
   → **No or unsure:** **Routine A.**

---

## ExecPlans

When writing complex features or significant refactors, use an ExecPlan (as described in PLANS.md) from design to implementation.

## ExecPlans

When writing complex features or significant refactors, use an ExecPlan (as described in PLANS.md) from design to implementation.

---

### Benchmarking workflow (repository-wide)

The `scripts/run-single-benchmark.sh` helper is the supported path for spot-checking performance optimisations. It builds the chosen module with the `benchmarks` profile, constrains the benchmark selection to a single `@Benchmark` method, and when `--enable-jfr` is supplied it enforces repeatable profiling defaults (no warmup, ten 10-second measurements, one fork) while clearly reporting the destination of the generated JFR recording. Lean on this script whenever you need a reproducible measurement harness.

## Proportionality Model (Think before you test)

Score the change on these lenses. If any are **High**, prefer **Routine A or D**.

- **Behavioral surface:** affects outputs, serialization, parsing, APIs, error text, timing/order?
- **Blast radius:** number of modules/classes touched; public vs internal.
- **Reversibility:** quick revert vs migration/data change.
- **Observability:** can existing tests or assertions expose regressions?
- **Coverage depth:** do existing tests directly hit the edited code?
- **Concurrency / IO / Time:** any risk here is **High** by default.

---

## Purpose & Contract

* **Bold goal:** deliver correct, minimal, well‑tested changes with clear handoff. Fix root causes; avoid hacks.
* **Bias to action:** when inputs are ambiguous, choose a reasonable path, state assumptions, and proceed.
* **Ask only when blocked or irreversible:** permissions, missing deps, conflicting requirements, destructive repo‑wide changes.
* **Definition of Done**
    * Code formatted and imports sorted.
    * Compiles with a quick profile / targeted modules.
    * Relevant module tests pass; failures triaged or crisply explained.
    * Only necessary files changed; headers correct for new files.
    * Clear final summary: what changed, why, where, how verified, next steps.
    * **Evidence present:** failing test output (pre‑fix) and passing output (post‑fix) are shown for Routine A; for Routine B show **pre/post green** from the **same selection** plus **Hit Proof**; for Routine D NO EVIDENCE.

### No Monkey‑Patching or Band‑Aid Fixes (Non‑Negotiable)

Durable, root‑cause fixes only. No muting tests, no broad catch‑and‑ignore, no widening APIs “to make green”.

**Strictly avoid**
* Sleeping/timeouts to hide flakiness.
* Swallowing exceptions or weakening assertions.
* Reflection/internal state manipulation to bypass interfaces.
* Feature flags that disable validation instead of fixing logic.
* Changing public APIs/configs without necessity tied to root cause.

**Preferred approach**
* Reproduce the issue and isolate the smallest failing test (class → method).
* Trace to the true source; fix in the right module.
* Add focused tests for behavior/edge cases (Routine A) or prove coverage/neutrality (Routine B).
* Run tight, targeted verifies; broaden only if needed.

---

## Enforcement & Auto‑Fail Triggers

Your run is **invalid** and must be restarted from “Reproduce first” if any occur:

* You modify production code before adding and running the smallest failing test in this repo **for behavior‑changing work**.
* You proceed without pasting a Surefire/Failsafe report snippet from `target/*-reports/`.
* Your plan does not have **exactly one** `in_progress` step.
* You run tests using `-am` or `-q`.
* You treat a narrative failure description or external stack trace as equivalent to an in‑repo failing test.
* **Routine B specific:** you cannot demonstrate that existing tests exercise the edited code (**Hit Proof**), or you fail to capture both pre‑ and post‑change **matching** passing snippets from the same selection.
* **Routine C breach:** you change production code while in a spike.

**Recovery procedure:**
Update the plan (`in_progress: create failing test`), post a description of your next step, create the failing test, run it, capture the report snippet, then resume.
For Routine B refactors: if any gate fails, **switch to Full TDD** and add the smallest failing test.

---

## Evidence Protocol (Mandatory)

After each grouped action, post an **Evidence block**, then continue working:

**Evidence template**
```
Evidence:
Command: python3 .codex/skills/mvnf/scripts/mvnf.py Class#method (preferred) OR mvn -o -Dmaven.repo.local=.m2_repo -pl <module> -Dtest=Class#method verify
Report: <module>/target/surefire-reports/<file>.txt
Snippet:
\<copy 1–30 lines capturing the failure or success summary>
```

**Routine B additions**
* **Pre‑green:** capture a pre‑change **passing** snippet from the **most specific** test selection that hits your code (ideally a class or method).
* **Hit Proof (choose one):**
    * An existing test class/method that directly calls the edited class/method, plus a short `rg -n` snippet showing the call site; **or**
    * A Surefire/Failsafe output line containing the edited class/method names; **or**
    * A temporary assertion or deliberate, isolated failing check in a **scratch test** proving the path is executed (then remove).
* **Post‑green:** after the patch, re‑run the **same selection** and capture a passing snippet.

---

## `CONTRIBUTING.md`

# How to contribute

So you want to help out making Eclipse RDF4J better. That's great, we welcome your contributions! 
Before you dive in, here are some things you need to know.

## Terms of Use

This repository is subject to the Terms of Use of the Eclipse Foundation

* http://www.eclipse.org/legal/termsofuse.php

## Eclipse Development Process

This Eclipse Foundation open project is governed by the Eclipse Foundation
Development Process and operates under the terms of the Eclipse IP Policy.

* https://eclipse.org/projects/dev_process
* https://www.eclipse.org/org/documents/Eclipse_IP_Policy.pdf

## Eclipse Contributor Agreement

In order to be able to contribute to Eclipse Foundation projects you must
electronically sign the Eclipse Contributor Agreement (ECA).

* http://www.eclipse.org/legal/ECA.php

The ECA provides the Eclipse Foundation with a permanent record that you agree
that each of your contributions will comply with the commitments documented in
the Developer Certificate of Origin (DCO). Having an ECA on file associated with
the email address matching the "Author" field of your contribution's Git commits
fulfills the DCO's requirement that you sign-off on your contributions.

For more information, please see the Eclipse Committer Handbook:
https://www.eclipse.org/projects/handbook/#resources-commit

### Signing the Eclipse Contributor Agreement
You must digitally sign the [Eclipse Contributor Agreement (ECA)](https://www.eclipse.org/legal/ECA.php). You can do this as follows:

* If you haven't done so already, [register an Eclipse account](https://accounts.eclipse.org/user/register). **Important**: Use the same email address that you will use on Git commits as the author address.
* Open the [ECA form](https://accounts.eclipse.org/user/eca) and complete it. See the [ECA FAQ](https://www.eclipse.org/legal/ecafaq.php) for more info.


## Creating your contribution

Once the legalities are out of the way you can dig in. Here's how:

1. Create an issue in the [issue tracker](https://github.com/eclipse/rdf4j/issues) that describes your improvement, new feature, or bug fix. Alternatively, comment on an existing issue to indicate you're keen to help solve it.
2. Fork the repository on GitHub.
3. Create a new branch for your changes starting from the `main` branch. Name your branch like this: `GH-1234-short-description-here` where 1234 is the Github issue number. See [Workflow](#workflow) for details.
4. Make your changes. Apply the [RDF4J code formatting guidelines](#code-formatting) by running `mvn process-resources`.
5. Make sure you include tests. We use JUnit 5 with AssertJ and Mockito. Have a look around for existing tests to get some idea, and of course feel free to ask advice.
6. Make sure the test suite passes after your changes: you can run `mvn verify` to run tests locally.
7. Commit your changes into the branch. Make sure the commit author name and e-mail correspond to what you used to sign the ECA. Use meaningful commit messages. Reference the issue number in the commit message (for example "GH-276: added null check").
8. Push your changes to your branch in your forked repository.
9. Optionally [squash your commits](https://rdf4j.org/documentation/developer/squashing) to clean up the commit history.
10. Use GitHub to submit a pull request (PR) for your contribution back to the central RDF4J repository. Once you have submitted your PR, do not use your branch for any other development (unless asked to do so by the reviewers of your PR). 

Once you've put up a PR, we will review your contribution, possibly make some suggestions for improvements, and once everything is complete it will be merged into the `main` branch (if it's a bug fix to be included in the next maintenance release) or into the `develop` branch (if it's a feature or improvement to be included in the next minor or major release).

We are happy to receive "work in progress" pull requests as well: if you're not quite finished, but would like some early feedback on your approach, feel free to publish a PR early and ask us to review. 

## Code formatting

Eclipse RDF4J follows the [Eclipse Coding Conventions for Java](https://wiki.eclipse.org/Coding_Conventions), with a couple of minor modifications:

- We use a line width of 120 characters.
- We use Unix line endings (LF).
- We require curly braces for every control statement body (e.g. if-else), even if it is a single line.
- We use a single tab as the indentation in all XML files (including the `pom.xml` files). 
- We use the following header comment on every Java file:

```
/*******************************************************************************
 * Copyright (c) ${year} Eclipse RDF4J contributors.
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Distribution License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/org/documents/edl-v10.php.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 *******************************************************************************/
 ```

...of course, replace `${year}` with the actual current year (if you use
Eclipse IDE, this will happen automatically). All RDF4J copyright headers
record only the year a file was _first_ contributed, so there is no need
to update the year of existing files if you modify those files.

**NB** for older existing source code, RDF4J sometimes uses a slightly different
copyright header, mentioning 'Aduna' as additional copyright holder . Please
make sure you do not use that different header for any new contributions. 

For import statements, the following conventions hold:

- we do not use wildcard imports or wildcard static imports
- we allow static imports where possible, but do not require their use
- we apply a fixed ordering for import statements, following Eclipse conventions. Import statements are ordered in groups separated by a single empty line, in the following order: static imports, java.\*, javax.\*, org.\*, com.\*, everything else.

There are various ways to apply these conventions to your code, depending on which editor/IDE you use.

### Eclipse IDE users

1. In Eclipse, open 'Preferences' -> 'Java' -> 'Code Style' -> 'Formatter' 
2. Click 'Import...' and find the file `eclipse-settings/eclipse-rdf4j-conventions.xml`, located in the git repository root.
3. The active profile should now say 'Eclipse rdf4j '. Click ok.
4. When making changes to Java code, hit Ctrl+Shift+F before saving to reformat the code. Alternatively, you can configure Eclipse to automatically apply formatting on save. This can be activated by going to 'Preferences' -> 'Java' -> 'Editor' -> 'Save Actions' and making sure the 'Format source code' option checkbox is ticked.

Similarly, to apply templates:

1. In Eclipse, open 'Preferences' -> 'Java' -> 'Code Style' -> 'Code Templates' 
2. Click 'Import...' and find the file `eclipse-settings/codetemplates.xml`, located in the git repository root.
3. Click OK. The templates will be automatically applied when necessary. 

For import organization, the Eclipse defaults should be fine, but you can make sure as follows:

1. go to 'Preferences' -> 'Java' -> 'Code Style' -> 'Organize Imports'. 
2. Make sure the list of ordered groups corresponds to 'java', 'javax', 'org', 'com'.
3. Make sure the numbers of (static) imports needed for wildcard imports are set suitable high (99 or more).

You can apply import organization by hitting Ctrl+Shift+O, or you can configure Eclipse to automtaically organize imports on save. This can be activated by going to 'Preferences' -> 'Java' -> 'Editor' -> 'Save Actions' and making sure the 'Organize imports' option checkbox is ticked.

Finally, for XML formatting, the Eclipse defaults should be fine, but you can make sure as follows:

1. go to 'Preferences' -> 'XML' -> 'XML Files' -> 'Editor'. 
2. Make sure line width is set to 120, 'Indent using tabs' is active, and indentation size is set to 1. 

### Other IDEs / using the Maven formatter and import sorting plugins

If you do not use Eclipse IDE, we still welcome your contributions of course. There are several ways in which you can configure your IDE to format according to our conventions. Some tools will have the Eclipse code conventions built in, or will have options to import Eclipse formatter and import sorting settings. 

In addition, the RDF4J project is configured to use the [formatter maven plugin](https://code.revelc.net/formatter-maven-plugin/), the [import sorting maven plugin](https://code.revelc.net/impsort-maven-plugin/index.html) and [XML Format plugin](https://acegi.github.io/xml-format-maven-plugin/) for validation of all code changes against the coding conventions, and compiling the project using Apache Maven will automatically activate these plugins and fix most formatting/import issues.

The formatters are automatically run by maven during the `process-resources` phase, which means they will activate whenever you compile, verify, package or install the project using maven (see the [maven default lifecycle](https://maven.apache.org/ref/3.6.3/maven-core/lifecycles.html#default_Lifecycle) for more details).

To validate your changes manually, run the following command:

```
mvn formatter:validate impsort:check xml-format:xml-check
```

To reformat your code manually before committing, run:

```
mvn formatter:format impsort:sort xml-format:xml-format
```

or alternatively:

```
mvn process-resources
```

Please note: these maven plugins are meant as a tool to help you and 
us to quickly check the most common formatting problems. They are _not_,
however, intended to completely relieve you of responsibility for correct
formatting, and won't necessarily cover all code conventions we follow. For
example, the guideline that we don't allow wildcard import statements is not
checked by these plugins. 

Having said all that, we appreciate your best effort, but if occassionally something slips through, that's no big deal: code conventions are there to help us as developers, not to make your life miserable :) 
     
## Workflow 

The short version for contributors: start from the `main` branch, and create a new, separate branch for every bugfix, improvement, or new feature. We recommend you use `GH-<issuenumber>-short-description` as the branch name, where `<issuenumber>` is the number of the Github issue you're fixing (without the leading `#`), and `short-description` is a few keywords that describe the issue.

For more detailed information on how RDF4J manages git branches, versioning, releases, and planning, see [Info for RDF4J developers](https://rdf4j.org/documentation/developer/).

## `SECURITY.md`

# Security Policy

Eclipse RDF4J follows the [Eclipse Vulnerability Reporting Policy](https://www.eclipse.org/security/policy.php). Vulnerabilities are tracked by the Eclipse security team, in cooperation with the RDF4J project lead. Fixing vulnerabilities is taken care of by the RDF4J project committers, with assistance and guidance of the security team. 

## Supported Versions

Eclipse RDF4J supports security updates for the following releases:


| Version | Supported          |
| ------- | ------------------ |
| current release   | ✅ |
| latest minor release before the current   | ✅(on request only) |
| latest major release before the current   | ✅(on request only) |
| anything older   | :x:                |

For example if the current release is 4.1, we support security patches for 4.1.x (the current release) and 4.0.x (latest minor before current), as well as for 3.7.x (latest major before current), but not for 3.6.x or older. Security patches for the current release are provided proactively by the team, while patches for older supported releases are provided on request only.

## Reporting a Vulnerability

We recommend that in case of suspected vulnerabilities you do not use the RDF4J public issue tracker, but instead contact the Eclipse Security Team directly via security@eclipse.org.
