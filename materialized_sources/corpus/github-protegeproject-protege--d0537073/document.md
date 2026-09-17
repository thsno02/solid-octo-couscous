# Repository semantic capsule: protegeproject/protege

- Commit: `d9c9d392f9d88b5c4dc49a109009e9c460b6fb2b`
- Default branch: `master`
- Description: protegeproject/protege
- Selected evidence files: 2 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# Protege Desktop

[Protege](https://protege.stanford.edu) is a free, open-source ontology editor that supports the latest [OWL 2.0 standard](http://www.w3.org/TR/owl2-overview/). Protege has a pluggable architecture, and many [plugins](https://protegewiki.stanford.edu/wiki/Protege_Plugin_Library) for different functionalities are available.

To read more about **Protege's features**, please visit the Protege [home page](https://protege.stanford.edu).

The latest version of Protege can be [downloaded](https://protege.stanford.edu/software.php#desktop-protege) from the Protege website, or from [github](https://github.com/protegeproject/protege-distribution/releases).

If you would like to contribute to the Protege Project please see our [contributing guide](https://github.com/protegeproject/protege/blob/master/CONTRIBUTING.md)

The [Developer Documentation](https://github.com/protegeproject/protege/wiki/Developer-Documentation) may be found on the wiki.

**Looking for support?** Please ask questions on the [protege-user](https://protege.stanford.edu/support.php) or [protege-dev](https://protege.stanford.edu/support.php) mailing lists. If you found a bug or would like to request a feature, you may also use [this issue tracker](https://github.com/protegeproject/protege/issues).

Protege is released under the [BSD 2-clause license](https://raw.githubusercontent.com/protegeproject/protege/master/license.txt).

Instructions for [building from source](https://github.com/protegeproject/protege/wiki/Building-from-Source) are available on the the wiki.

## `CONTRIBUTING.md`


# Contributing

Thanks for considering a contribution to the Protégé project!  You can contribute in a number of ways from filing bug reports through to code contributions.

We have a [code of conduct](CODE_OF_CONDUCT.md) that contributors must abide to.  Please take some time to have a look at it.

## Reporting Bugs

We use GitHub Issues to manage bug reports.  Before creating a bug report please have a quick look at [our issue tracker](https://github.com/protegeproject/protege/issues) to see if someone else has already filed an issue.

### How do I submit a Bug Report?

When you submit a bug report you should explain the problem and include additional details to help maintainers reproduce the problem:

* Use a clear and descriptive title for the issue to identify the problem.
* If you can describe exactly what time the issue occurred, we can more confidently review our (rather large) logs to look for reports related to your issue.
* Describe the exact steps which reproduce the problem in as many details as possible. For example, what you were trying to do and what you expected.
* Provide specific examples to demonstrate the steps.
* Describe the behavior you observed after following the steps and point out what exactly is the problem with that behavior.
* Explain which behavior you expected to see instead and why.

Please include details about your configuration and environment:

* The version of Protégé that you're using
* The name and version of the operating system that you're using

We will assign the correct labels to your issue after reviewing your issue.

## Code Contributions

Protégé is written using Java.  You can contribute by forking the GitHub repository and submitting a pull request.  

Once you have submitted a pull request we will review your code and test it.  We may require you to make some changes to your code or the documentaiton of your code.  You should include automated tests with your code.

### What can I work on?

Our [issue tracker](https://github.com/protegeproject/protege/issues) has a list of feature requests and bugs that need fixing.  You can use this as an inspiration for something to work on.  

A number of the issues are tagged as ["Easy first issue"](https://github.com/protegeproject/protege/issues?q=is%3Aissue+is%3Aopen+label%3A%22Note%3A+Easy+First+Issue%22).  These are some of the easier issues to tackle that you might want to start with.  

If you start working on an issue, please leave a comment in the issue discussion thread so that other people know you are working on the issue.  If you stop working on an issue please leave a comment in the thread so that we know.

Here are some other ideas for other ways you can contribute:

* __Add more unit tests__ We are always looking to increase test coverage.  Writing tests is a good way to "get your toes wet" with the code base.  We use Mockito and Hamcrest for writing tests.  Before writing tests please take a look at other tests in the code base so that you get a feeling for the style that we use.  Test code is as important as the main code base.  Please write your test code with the same care that you would write you main code.  New tests should be submitted as pull requests.


