# Changelog

## Pre-release

**Implemented enhancements:**

- CMS-1561 - Removed CTA fields from accordions on country guide page. Added new CTAs to be displayed at the top of the page. Regenerated db template to speed up tests
- CMS-1419 - Added Wagtail registration view for SSO users, group info management UI, and updated user edit view to mark users as approved
- CMS-1421 - Integrate with GOV.UK Notify to send SSO user approval notifications
- CI-104 - Added capital invest landing, region, sector and opportunity pages.
- NOTICKET - Removed blanket debug logging to remove noise when using interactive shell tools
- CI-144 - Updated capital invest landing page to match more recent invision designs
- CI-148 - Updated capital invest pages to match more recent page designs
- CI-150 - Updated featured cards on Invest home page to be more flexible and all from cms
- CI-128 - Changed required fields to be nullable and removed unused fields on Invest home page
- CI-152 - Changed `next steps` sections to be `contact` section on capital invest pages
- CI-153 - Removed the cards pdf buttons on Capital Invest Landing page, region cards are now only displayed with markdown text
- CMS-1638 - Prevent leaking user information on sql table dump
- CMS-1603 - Introduced separate base page classes for each app so that unique slug enforcement can be relaxed in great_international


### Fixed bugs:

- CMS-1556 - Fixed copy upstream not working for pages that have the same slug but exist under different apps
- CMS-1578 - Fixed issue with `SSORedirectUsersToRequestAccessViews` middleware that caused an `AttributeError` to be raised when a users was not authenticated
- CMS-1423 - Updated SSO notifications to use the user's first name in the greeting, instead of the full name
- CMS-1419 - Fixed 'too_many_redirects' when logging in via SSO
- NOTICKET - Upgrade django-restframework to 3.9.4 to fix XSS vulnerability
- CMS-1589 - Upgrade django-staff-sso-client to version 0.3.0 to fix blank username field bug
- NOTICKET - Update guidance for `update_db_template` in README
- CI-154 - Added section three to guide landing page for ISD/contact section
- CMS-1633 - Removed `Page.delete()` override from `BasePage` so that child pages of differing types are deleted as intended


## [2019.05.09](https://github.com/uktrade/directory-cms/releases/tag/2019.05.09)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.04.24_1...2019.05.09)

**Implemented enhancements:**

- CMS-1468 - Copied international EU Exit contact form models into great_international
- CMS-1417 - Integrate staff SSO
- CMS-1462 - Remove char limit from fields in `InternationalArticlePage`
- CMS-1449 - Upgrade to wagtailmedia 0.3.0, for future Wagtail 2.4+ compat
- CMS-1396 - Improve `BasePage.get_tree_based_routing()` efficiency by fetching site and routing settings in the same query
- CI-99 - Removed unused fields for the capital invest banner on the Invest landing page
- CI-101 - Added Investor Support Directory section to `InvestHomePage`
- CMS-1397 - Updated custom url methods on `BasePage` to support tree-based routing when enabled
- CMS-1399 - Replaced unused `lookup_by_full_path` API endpoint with new `lookup_by_path` API endpoint to support tree-based routing
- CMS-1396 - Made 'uses_tree_based_routing' field editable in the CMS for all international page types
- CI-116 - Moved sections around in content panels, removed cta_text fields and added capital investment image on Invest Landing Page
- CMS-1248 - Removed JPEG compression overrides to improve image quality
- CMS-1446 - Prevent changing of a user's personal details when SSO is enforced for users
- NOTICKET - Optimised `BasePage.full_path` by uisng `specific_class` to access class attribute values instead of `specific`
- NOTICKET - Optimised serializers by using page-type specific queries instead of `PageQuerySet.specific()` where possible


### Fixed bugs:

- Upgraded urllib3 to fix [vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2019-11324)


## [2019.04.24_1](https://github.com/uktrade/directory-cms/releases/tag/2019.04.24_1)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.04.24...2019.04.24_1)

**Implemented enhancements:**

- Added `FEATURE_MAINTENANCE_MODE_ENABLED` to enable maintenance mode


## [2019.04.24](https://github.com/uktrade/directory-cms/releases/tag/2019.04.24)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.04.10...2019.04.24)

**Implemented enhancements:**

- Added `feature highlight` and `feature link` fields to `InternationalHomePage` [CMS-1385]
