# Repository semantic capsule: wikimedia/mediawiki

- Commit: `eb2c0acaeeb2135c7a6e2952b536f0deb3343ba2`
- Default branch: `master`
- Description: wikimedia/mediawiki
- Selected evidence files: 2 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# MediaWiki

MediaWiki is a free and open-source wiki software package written in PHP. It
serves as the platform for Wikipedia and the other Wikimedia projects, used
by hundreds of millions of people each month. MediaWiki is localised in over
350 languages and its reliability and robust feature set have earned it a large
and vibrant community of third-party users and developers.

MediaWiki is:

* feature-rich and extensible, both on-wiki and with hundreds of extensions;
* scalable and suitable for both small and large sites;
* simple to install, working on most hardware/software combinations; and
* available in your language.

For system requirements, installation, and upgrade details, see the files
RELEASE-NOTES, INSTALL, and UPGRADE.

* Ready to get started?
  * https://www.mediawiki.org/wiki/Special:MyLanguage/Download
* Setting up your local development environment?
  * https://www.mediawiki.org/wiki/Special:MyLanguage/Local_development_quickstart
* Looking for the technical manual?
  * https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Contents
* Seeking help from a person?
  * https://www.mediawiki.org/wiki/Special:MyLanguage/Communication
* Looking to file a bug report or a feature request?
  * https://bugs.mediawiki.org/
* Interested in helping out?
  * https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute

MediaWiki is the result of global collaboration and cooperation. The CREDITS
file lists technical contributors to the project. The COPYING file explains
MediaWiki's copyright and license (GNU General Public License, version 2 or
later). Many thanks to the Wikimedia community for testing and suggestions.

## `package.json`

{
	"name": "core",
	"private": true,
	"scripts": {
		"api-testing": "mocha --timeout 0 --recursive --parallel tests/api-testing",
		"doc": "jsdoc -c jsdoc.json",
		"lint": "grunt lint",
		"minify:svg": "svgo --config=.svgo.config.js --quiet --recursive --folder resources/src --folder resources/assets",
		"mocha": "mocha --timeout 0 --recursive",
		"qunit": "grunt qunit",
		"selenium-test": "if [ \"$CI\" = true ]; then node tests/selenium/docs/Stack/webdriverio.js; fi && wdio ./tests/selenium/wdio.conf.js",
		"test": "grunt lint && npm run doc && npm run jest",
		"jest": "jest --config tests/jest/jest.config.js"
	},
	"devDependencies": {
		"@apidevtools/swagger-parser": "^10.1.0",
		"@babel/preset-env": "7.25.4",
		"@pinia/testing": "1.0.3",
		"@stoplight/spectral-cli": "6.11.0",
		"@vue/test-utils": "2.4.6",
		"@vue/vue3-jest": "29.2.6",
		"@wdio/cli": "9.30.1",
		"@wdio/junit-reporter": "9.30.1",
		"@wdio/local-runner": "9.30.1",
		"@wdio/mocha-framework": "9.30.1",
		"@wdio/spec-reporter": "9.30.1",
		"@wikimedia/codex": "2.7.0",
		"@wikimedia/codex-icons": "2.7.0",
		"@wikimedia/karma-firefox-launcher": "2.1.3",
		"api-testing": "1.8.0",
		"chai-openapi-response-validator": "^0.14.2",
		"domino": "2.1.0",
		"dotenv": "8.2.0",
		"eslint-config-wikimedia": "0.32.5",
		"grunt": "1.6.3",
		"grunt-banana-checker": "0.13.0",
		"grunt-contrib-watch": "1.1.0",
		"grunt-eslint": "24.3.0",
		"grunt-karma": "4.0.2",
		"grunt-stylelint": "0.21.0",
		"jest": "29.7.0",
		"jest-environment-jsdom": "29.7.0",
		"jest-fetch-mock": "3.0.3",
		"jsdoc": "4.0.5",
		"jsdoc-wmf-theme": "1.3.0",
		"karma": "6.4.1",
		"karma-chrome-launcher": "3.1.0",
		"karma-mocha-reporter": "2.2.5",
		"karma-qunit": "4.2.0",
		"pinia": "3.0.4",
		"qunit": "2.26.0",
		"stylelint-config-wikimedia": "0.19.3",
		"svgo": "3.3.3",
		"vue": "3.5.13",
		"wdio-mediawiki": "file:tests/selenium/wdio-mediawiki",
		"xml2js": "^0.6.2"
	}
}
