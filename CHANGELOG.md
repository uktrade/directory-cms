# Changelog

## Pre-release

## [2019.05.09](https://github.com/uktrade/directory-cms/releases/tag/2019.05.09)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.05.03...2019.05.09)

**Implemented enhancements:**

- [CMS-1468](https://uktrade.atlassian.net/browse/CMS-1468) Copied international EU Exit contact form models into great_international
- [CMS-1417](https://uktrade.atlassian.net/browse/CMS-1417) Integrate staff SSO
- [CMS-1462](https://uktrade.atlassian.net/browse/CMS-1462) Remove char limit from fields in `InternationalArticlePage`
- [CMS-1449](https://uktrade.atlassian.net/browse/CMS-1449) Upgrade to wagtailmedia 0.3.0, for future Wagtail 2.4+ compat


## [2019.05.03](https://github.com/uktrade/directory-cms/releases/tag/2019.05.03)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.04.24_1...2019.05.03)

**Implemented enhancements:**

- [CI-99](https://uktrade.atlassian.net/browse/CI-99) Removed unused fields for the capital invest banner on the Invest landing page
- [CI-101](https://uktrade.atlassian.net/browse/CI-101) Added Investor Support Directory section to `InvestHomePage`
- [CMS-1397](https://uktrade.atlassian.net/browse/CMS-1397) Updated custom url methods on `BasePage` to support tree-based routing when enabled
- [CMS-13998](https://uktrade.atlassian.net/browse/CMS-13998) Replaced unused `lookup_by_full_path` API endpoint with new `lookup_by_path` API endpoint to support tree-based routing
- [CMS-1396](https://uktrade.atlassian.net/browse/CMS-1396) Made 'uses_tree_based_routing' field editable in the CMS for all international page types
- [CI-116](https://uktrade.atlassian.net/browse/CI-116) Moved sections around in content panels, removed cta_text fields and added capital investment image on Invest Landing Page
- [CMS-1248](https://uktrade.atlassian.net/browse/CMS-1248) Removed JPEG compression overrides to improve image quality

### Fixed bugs:

- Upgraded urllib3 to fix [vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2019-11324)


## [2019.04.24_1](https://github.com/uktrade/directory-cms/releases/tag/2019.04.24_1)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.04.24...2019.04.24_1)

**Implemented enhancements:**

- Added `FEATURE_MAINTENANCE_MODE_ENABLED` to enable maintenance mode


## [2019.04.24](https://github.com/uktrade/directory-cms/releases/tag/2019.04.24)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.04.10...2019.04.24)

**Implemented enhancements:**

- Added `feature highlight` and `feature link` fields to `InternationalHomePage` [CMS-1385](https://uktrade.atlassian.net/browse/CMS-1385)
