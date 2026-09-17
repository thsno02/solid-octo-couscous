# Repository semantic capsule: apache/jena

- Commit: `17a7834ff4366f80e232208639678df63d00d0ed`
- Default branch: `main`
- Description: apache/jena
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

Jena README
===========

Welcome to Apache Jena, a Java framework for writing Semantic Web applications.

See https://jena.apache.org/ for the project website, including documentation.

The codebase for the active modules is in git:

https://github.com/apache/jena

## `AGENTS.md`

<!--
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Agent Guide for jena

This file is read by automated agents (security scanners, code
analyzers, AI assistants) operating on this repository.

## Security

Security model: [SECURITY.md](./SECURITY.md)

Agents that scan this repository should consult `SECURITY.md` and the
threat model it links before reporting issues.

## `CONTRIBUTING.md`

Apache Jena : Contributing
==========================

The project welcomes contributions, large and small, from anyone.

The mailing list for project-wide discussions is dev@jena.apache.org and all
development work happens in public, using GitHub isues and that mailing list.

The processes described here are guidelines, rather than fixed requirements.


## Contributions

Contributions can be made by:

* Github pull requests (preferred)
* Emailing a patch file to the developers list

Contributions should include:

* Tests
* Documentation as needed

Documentation is kept and published via a git repository:

   https://github.com/apache/jena-site/

## Workflow

### Github issues

The project uses github issues to track work.  Please create 
a github issue so that we can track a contribution.

Github issue:

    https://github.com/apache/jena/issues

### Github

It is useful to create a Gihhub issue use the issue number (e.g. GH-9999)
in the pull request title. This activates the automated mirroring of
discussions onto the project developers mailing list.

To make a contribution:

* On github, fork https://github.com/apache/jena into you github account.
* Create a branch in your fork for the contribution.
* Make your changes. Include the Apache source header at the top of each file.
* Generate a pull request via github. Further changes to your branch will automatically
  show up in the pull request

### Discussion and Merging

A project committer will review the contribution and coordinate any project-wide discussion
needed. Review and discussion of the pull request itself takes place on
github.

The committer review guide:

    https://jena.apache.org/getting_involved/reviewing_contributions.html

### Patches

An alternative is to upload a patch/diff to JIRA.

### Code

Code style is about making the code clear for the next person
who looks at the code.

The project prefers code to be formatted in the common java style with
sensible deviation for short forms.

The project does not enforce a particular style but asks for:

* Kernighan and Ritchie style "Egyptian brackets" braces.
* Spaces for indentation
* No `@author` tags.
* One statement per line
* Indent level 4 for Java
* Indent level 2 for XML

See, for illustration:
https://google.github.io/styleguide/javaguide.html#s4-formatting

The codebase has a long history - not all of it follows this style.

The code should have no warnings, in particular, use `@Override` and types
for generics, and don't declared checked exceptions that are not used.
Use `@SuppressWarnings("unused")` as necessary.

Please don't mix reformatting and functional changes; it makes it harder
to review.

### Legal

When you contribute, you affirm that the contribution is your original work and
that you license the work to the Apache Software Foundation. You agree to license the
material under the terms and conditions of the 
[Contributor's Agreement](https://www.apache.org/licenses/contributor-agreements.html).

You, as an individual, must be entitled to make the contribution to the
project. If the contribution is part of your employment, please arrange
this before making the contribution.

For a large contribution, the project may ask for a specific Software
Grant from the contributor.

If in doubt, or if you have any questions, ask on the dev@jena.apache.org
mailing list. Legal issues are easier to deal with if done before
contributing, rather than after.

The project cannot accept contributions with unclear ownership nor
contributions containing work by other people without a clear agreement
from those people.

## `SECURITY.md`

<!--
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Security Policy

## Reporting a Vulnerability

`apache/jena` follows the [Apache Software Foundation security process](https://www.apache.org/security/). Please report suspected
vulnerabilities privately to `security@apache.org`; do not open public
GitHub issues or pull requests for security reports.

## Threat Model

What the project treats as in scope and out of scope, the security
properties it provides and disclaims, the adversary model, and how
findings are triaged are documented in [THREAT_MODEL.md](./THREAT_MODEL.md).
