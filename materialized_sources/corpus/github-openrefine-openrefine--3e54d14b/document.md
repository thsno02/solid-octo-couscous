# Repository semantic capsule: OpenRefine/OpenRefine

- Commit: `6d5d0579ee84c787eb31d04fa1676582f6e7b65e`
- Default branch: `master`
- Description: OpenRefine/OpenRefine
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# OpenRefine

[![DOI](https://zenodo.org/badge/6220644.svg)](https://zenodo.org/badge/latestdoi/6220644)
[![Join the chat at https://gitter.im/OpenRefine/OpenRefine](https://badges.gitter.im/OpenRefine/OpenRefine.svg)](https://gitter.im/OpenRefine/OpenRefine)
[![Snapshot release](https://github.com/OpenRefine/OpenRefine/actions/workflows/snapshot_release.yml/badge.svg)](https://github.com/OpenRefine/OpenRefine/actions/workflows/snapshot_release.yml) [![Coverage Status](https://coveralls.io/repos/github/OpenRefine/OpenRefine/badge.svg?branch=master)](https://coveralls.io/github/OpenRefine/OpenRefine?branch=master) [![Translation progress](https://hosted.weblate.org/widgets/openrefine/-/svg-badge.svg)](https://hosted.weblate.org/engage/openrefine/?utm_source=widget)
[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor-GitHub-blue)](https://github.com/sponsors/OpenRefine)
[![Donate](https://img.shields.io/badge/Donate-OpenRefine-blue)](https://openrefine.org/donate)
[![OpenRefine Store](https://img.shields.io/badge/🛍️Shop-OpenRefine_Store-blue)](https://store.openrefine.org)

OpenRefine is a Java-based power tool that allows you to load data, understand it,
clean it up, reconcile it, and augment it with data coming from
the web. All from a web browser and the comfort and privacy of your own computer.

Official website: **https://openrefine.org**

Community forum: **https://forum.openrefine.org**

[<img src="https://github.com/OpenRefine/OpenRefine/blob/master/graphics/icon/open-refine-320px.png" align="right">](https://openrefine.org)

## Download

* [OpenRefine Releases](https://github.com/OpenRefine/OpenRefine/releases)

## Snapshot releases

You can download snapshots of the development version of OpenRefine.
To do so, you need to be logged in to GitHub. Then, click on the first item with a green tick / check mark on [this page](https://github.com/OpenRefine/OpenRefine/actions/workflows/snapshot_release.yml) and scroll down to the Artifacts section to find the version that matches your operating system.

## Run from source

If you have cloned this repository to your computer, you can run OpenRefine with:

* `./refine` on Mac OS and Linux
* `refine.bat` on Windows

This requires [JDK 11](https://adoptium.net/) or newer, [Apache Maven](https://maven.apache.org/) and [Node.js 18](https://nodejs.org/) or newer.

## Documentation

* [User Manual](https://openrefine.org/docs)
* [FAQ](https://github.com/OpenRefine/OpenRefine/wiki/FAQ)

## Contributing to the project

* [Developers Guide & Architecture](https://github.com/OpenRefine/OpenRefine/wiki/Documentation-For-Developers)
* [Contributing Guide](https://github.com/OpenRefine/OpenRefine/blob/master/CONTRIBUTING.md)
* [Project Governance](https://github.com/OpenRefine/OpenRefine/blob/master/GOVERNANCE.md)

## Contact us

* [Community forum](https://forum.openrefine.org)
* [Twitter](https://www.twitter.com/openrefine)
* [Gitter](https://gitter.im/OpenRefine/OpenRefine)
* [Matrix (bridged from Gitter)](https://matrix.to/#/#OpenRefine_OpenRefine:gitter.im)

## Licensing and legal issues

OpenRefine is open source software and is licensed under the BSD license located in the [LICENSE.txt](LICENSE.txt). See the folders `licenses` under `/main/webapp/` as well as within each `/extensions` for information on open source libraries that OpenRefine depends on.

## Funding OpenRefine

OpenRefine is maintained by a small core team and relies on grants plus community support.
• **Donate** or become a monthly sponsor: https://openrefine.org/donate
• **See our backers**: https://openrefine.org/backers
• **Machine-readable manifest**: https://openrefine.org/funding.json

## Credits

This software was created by Metaweb Technologies, Inc. and originally written and conceived by [David Huynh](https://github.com/dfhuynh). Metaweb Technologies, Inc. was acquired by Google, Inc. in July 2010 and the product was renamed Google Refine. In October 2012, it was renamed OpenRefine as it transitioned to a community-driven project.

Since 2020, OpenRefine is fiscally sponsored by [Code for Science and Society](https://www.codeforsociety.org/) (CS&S).

See [CONTRIBUTING.md](./CONTRIBUTING.md) for instructions on how to contribute yourself.

## `AGENTS.md`

# AGENTS.md - OpenRefine Project Information

This file provides important information about the OpenRefine project and repository for AI agents and developers.

## Project Overview

**OpenRefine** is a Java-based power tool that allows you to load data, understand it, clean it up, reconcile it, and augment it with data coming from the web. All from a web browser and the comfort and privacy of your own computer.

- **License**: BSD-3-Clause
- **Official Website**: https://openrefine.org
- **Documentation**: https://openrefine.org/docs
- **Community Forum**: https://forum.openrefine.org
- **Version**: 3.10-SNAPSHOT (as of this writing)

## Technology Stack

### Backend
- **Language**: Java
- **Minimum Java Version**: JDK 21
- **Maximum Java Version**: JDK 26
- **Build Tool**: Apache Maven 
- **Project Structure**: Multi-module Maven project

### Frontend
- **JavaScript Libraries**: jQuery, jQuery UI, Select2, Underscore.js
- **Internationalization**: @wikimedia/jquery.i18n
- **Build/Package Management**: Node.js 24+ and npm 11.16.0+
- **E2E Testing**: Cypress with Node.js 24

### Project Modules
- `modules/core` - Core OpenRefine functionality
- `modules/grel` - GREL (General Refine Expression Language)
- `main` - Main application and webapp
- `server` - Server components
- `extensions` - Extension modules (database, jython, pc-axis, wikibase)
- `packaging` - Distribution packaging
- `benchmark` - Performance benchmarks

## Build System

### Building OpenRefine

```bash
./refine build
```

This command:
- Compiles all Java code using Maven
- Builds the webapp frontend
- Prepares all modules and extensions
- Creates necessary artifacts

### Running OpenRefine

```bash
# On Mac OS and Linux
./refine

# On Windows
refine.bat
```

**Configuration Options:**
- `-c <path>` - Path to refine.ini file (default: ./refine.ini)
- `-d <path>` - Path to the data directory
- `-H <host>` - Expected host header value
- `-i <interface>` - Network interface to bind (default: 127.0.0.1)
- `-m <memory>` - JVM min and max memory heap size (default: 1400M)
- `-p <port>` - Port to listen on (default: 3333)
- `-v <level>` - Verbosity level [error,warn,info,debug,trace]
- `-w <path>` - Path to the webapp (default: main/webapp)
- `--debug` - Enable JVM debugging on port 8000
- `--jmx` - Enable JMX monitoring

### Other Build Commands

```bash
./refine clean              # Clean compiled classes
./refine test              # Run all tests
./refine extensions_test   # Run extension tests
./refine server_test       # Run server tests
./refine e2e_tests         # Run end-to-end tests
./refine lint              # Reformat source code according to conventions
./refine mac_dist <ver>    # Make MacOS binary distribution
./refine windows_dist <ver> # Make Windows binary distribution
./refine linux_dist <ver>  # Make Linux binary distribution
./refine dist <ver>        # Make all distributions
```

## Testing Infrastructure

### Unit Tests
- **Framework**: TestNG (Java)
- **Location**: Throughout the codebase in `src/test` directories
- **Run**: `./refine test` or `./refine server_test` or `./refine extensions_test`

### End-to-End Tests
- **Framework**: Cypress
- **Location**: `main/tests/cypress/`
- **Setup**: 
  ```bash
  cd main/tests/cypress
  npm i -g yarn
  yarn install
  ```
- **Run**: `./refine e2e_tests`
- **Browser**: Chrome (default in CI)
- **Configuration**: Uses environment variables like `CYPRESS_BROWSER`, `CYPRESS_SPECS`, `CYPRESS_GROUP`

### Testing in CI
The project uses GitHub Actions for continuous integration:
- **E2E Tests**: `.github/workflows/pull_request_e2e.yml` - Runs Cypress tests on pull requests
- **Server Tests**: `.github/workflows/pull_request_server.yml` - Runs server-side tests
- **CodeQL Analysis**: Security scanning for Java and JavaScript

## Development Workflow

### Code Contributions
1. Fork the repository
2. Create a branch named with the issue number and brief description
3. Make changes (avoid unrelated modifications)
4. Create unit and/or E2E tests for your changes
5. Run `./refine lint` before submitting (CI will fail if lint fails)
6. Ensure all tests pass
7. Submit a pull request for review

### Code Style and Formatting
- **Linting**: Run `./refine lint` to reformat code according to OpenRefine conventions
- **EditorConfig**: The repository includes `.editorconfig` for consistent formatting:
  - Charset: UTF-8
  - Line endings: LF
  - Indent: 4 spaces (2 for YAML, JSON, LESS, shell scripts)
  - Max line length: 120 characters
  - Java imports organized with specific layout rules
  - Insert final newline

### Important Files
- `pom.xml` - Root Maven project configuration
- `refine` / `refine.bat` - Main launch scripts
- `refine.ini` - Runtime configuration (can be created)
- `.editorconfig` - Code formatting rules
- `CONTRIBUTING.md` - Contribution guidelines
- `GOVERNANCE.md` - Project governance model

## Extension System

OpenRefine supports a plugin architecture for extending functionality. Extensions are located in the `extensions/` directory:
- **database** - Database import/export functionality
- **jython** - Python scripting support via Jython
- **pc-axis** - PC-Axis file format support
- **wikibase** - Wikibase/Wikidata integration

Each extension is a Maven module with its own structure and can include:
- Java backend code
- JavaScript frontend code
- Internationalization files
- Specific tests

## Project Dependencies

### Backend Dependencies
- Jackson (2.21.0) - JSON processing
- Various Apache Commons libraries
- Jetty - Embedded web server
- SLF4J - Logging
- TestNG - Testing

### Frontend Dependencies
- jQuery (3.7.1)
- jQuery UI (1.14.2)
- jQuery Migrate (3.6.0)
- Select2 (4.1.0)
- js-cookie (3.0.8)
- tablesorter (2.32.0)
- underscore (1.13.8)
- wikimedia/jquery.i18n (1.0.9)

## Data and Configuration

- **Default Data Directory**: OS-dependent, can be specified with `-d` flag
- **Default Port**: 3333
- **Default Interface**: 127.0.0.1 (localhost only)
- **Default Memory**: 1400M (can be configured)

## Internationalization

OpenRefine supports multiple languages:
- Translation files located in `*/langs/` directories
- Uses Weblate for community translations - https://hosted.weblate.org/engage/openrefine/
- Managed through @wikimedia/jquery.i18n

## Community and Support

- **Forum**: https://forum.openrefine.org
- **Issue Tracker**: https://github.com/OpenRefine/OpenRefine/issues
- **Developer Forum**: https://forum.openrefine.org/c/dev/8
- **Gitter Chat**: https://gitter.im/OpenRefine/OpenRefine
- **Twitter**: @openrefine

## Fiscal Sponsorship

Since 2020, OpenRefine is fiscally sponsored by Code for Science and Society (CS&S).

## Important Notes for AI Agents

1. **Always run `./refine lint` before submitting code** - The CI will fail if code is not properly formatted
2. **Tests are required** - Both unit tests and E2E tests should be added for new features
3. **Multi-module project** - Changes may span multiple Maven modules (core, grel, main, server, extensions)
4. **Java version compatibility** - Code must work with Java 11-21
5. **Build before running** - Always run `./refine build` after code changes before testing
6. **Memory configuration** - For E2E tests, memory is configured via refine.ini (REFINE_MIN_MEMORY, REFINE_MEMORY)
7. **Extension isolation** - Extensions are separate modules with their own dependencies
8. **Frontend changes** - May require Node.js/npm operations in `main/webapp/`
9. **Path-specific workflows** - Some CI workflows ignore specific paths (e.g., translation files, IDE configs)
10. **No force push** - The repository does not allow force pushes or rebase operations that rewrite history

## Getting Started for Development

```bash
# Clone the repository

## `CONTRIBUTING.md`

The OpenRefine project welcomes contributions in a variety of forms.
This document contains information a few of the ways you can contribute to the OpenRefine project.
Please also review our [Governance model](https://github.com/OpenRefine/OpenRefine/blob/master/GOVERNANCE.md)

## Provide peer user support

We welcome users to the [OpenRefine forum](https://forum.openrefine.org/) to ask questions and request assistance.
If you can help answer questions in your area of expertise, it would be a benefit to the community.

If a forum discussion determines there is a bug in OpenRefine or a new feature is identified,
we welcome bug reports and feature requests. Please search the [issue tracker](https://github.com/OpenRefine/OpenRefine/issues) first to make sure
the bug / feature hasn't already been added. Note: the development team principally works from the issue
tracker, so anything not included there risks getting lost.

## Promote OpenRefine

Promoting OpenRefine is a great way to give back. Did you write a tutorial or article about OpenRefine on your blog or site?
Are you organizing a workshop or presentation for OpenRefine in your city? Let us, and the community, know via our [forum](https://forum.openrefine.org/) or social media.

## Contribute translations

We want OpenRefine to be available in as many languages as possible to serve
the biggest community of users. You can help us [translate OpenRefine](https://docs.openrefine.org/technical-reference/translating-ui) into languages you are fluent in [via Weblate](https://hosted.weblate.org/engage/openrefine/?utm_source=widget).
Although we have the beginnings of translations for many languages, only a few are complete and popular languages
like Spanish, Brazilian Portuguese, and French could use help.

## Contribute documentation

When browsing our [user manual](https://openrefine.org/docs/) or other documentation, feel free to use the edit button to suggest improvements.
For large changes, you might want to first discuss your proposed changes on the forum and then [prepare your changes locally](https://openrefine.org/docs/technical-reference/documentation-contributions).

##  Contribute code 

You can contribute code in various ways:
- Fix bugs or implement new features. Follow [our guide towards your first code contribution](https://openrefine.org/docs/technical-reference/code-contributions)
- Improve test coverage. Much of our code was originally written without tests, so help on this front is very much appreciated.
- Develop an OpenRefine extension
- Develop a reconciliation service

All developers including new distributions and plugin developers are invited to leverage the following OpenRefine project management areas.
- the [official documentation](https://openrefine.org/docs/) for shared documentation between both user docs and [technical reference](https://docs.openrefine.org/technical-reference/contributing)
- the [developer forum](https://forum.openrefine.org/c/dev/8) for technical questions, new feature development and anything code related. We invite you to share your idea there first. Someone may be able to point out to existing development saving you hours of research and development.
- the [issue tracker](https://github.com/OpenRefine/OpenRefine/issues) for requesting new features and bug reports.
- [Gitter Chat](https://gitter.im/OpenRefine/OpenRefine) (only occasionally monitored)

### How to submit PR's (pull requests), patches, and bug fixes

All code changes are made via GitHub Pull Requests which are reviewed before merging, even those by core committers.

If you are unfamiliar with git, GitHub, or open source development, please see [our guide towards your first code contribution](https://openrefine.org/docs/technical-reference/code-contributions).

- If you are looking for something to work on, please see our [issue list](https://github.com/OpenRefine/OpenRefine/issues). We have a separate tag for [Good First Issues](https://github.com/OpenRefine/OpenRefine/issues?q=is%3Aopen+is%3Aissue+label%3A%22Good+First+Issue%22).

- create a branch named with the issue number and a brief description
- avoid changes unrelated to fixing the issue
- create unit and/or end-to-end tests which cover the bug fix or new feature
- run `./refine lint` before submitting your PR (CI will fail if lint fails)
- make sure all tests are green before submitting your PR
- Add screenshots for UI changes (if applicable).
- we attempt to prioritize PR reviews, but please be patient

### New functionality via extensions

OpenRefine supports a plugin architecture to extend its functionality. You can find more information on how to write
an extension on our [website](https://openrefine.org/docs/technical-reference/writing-extensions).
Giuliano Tortoreto also wrote separate documentation detailing how to build an extension for OpenRefine.
[PDF](https://github.com/giTorto/OpenRefineExtensionDoc/blob/master/main.pdf) and [LaTeX](https://github.com/giTorto/OpenRefineExtensionDoc/) versions are available. It dates from 2014, but still contains good information.

If you want your extension included in the [list of extensions](https://openrefine.org/extensions) advertised on openrefine.org,
please submit a pull request on the download page, please edit [this file](https://github.com/OpenRefine/openrefine.org/blob/master/src/pages/extensions.md).

## `SECURITY.md`

# OpenRefine Security Policy

## Supported Versions

Security updates are provided for the latest stable release, and are published as patch releases. For instance, if the latest stable version is 3.8.2, reported vulnerabilities affecting it will be fixed by releasing further patch releases (such as 3.8.3). Accumulated patches are included in the next minor or major release (e.g. 3.9 or 4.0)

Previous releases do not get security updates, so we recommend always running the latest stable release.

## Reporting a Vulnerability

Our core team will try their best to fix any valid vulnerability that is reported to them.

You can privately report a vulnerability to the OpenRefine team by [creating a security advisory on GitHub](https://github.com/OpenRefine/OpenRefine/security/advisories/new). This report will be kept private while it is being assessed by the team.

Keep in mind that OpenRefine is designed to run locally on a user's PC, while also making network calls across the internet only upon a user's choice or command.
As such, certain vulnerabilities might not apply to OpenRefine's design. In doubt, please submit a report anyway.
