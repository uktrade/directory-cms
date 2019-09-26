# Changelog

## Pre-release

### Implemented enhancements
- XOT-1107 - Add article pages to serializer for topic pages, only serialize necessary data
- XOT-1444 - add article video transcript component
- XOT-1108 - Filter markets by sector
- XOT-1074 - Add `ArticePage` to the children of `TopicLandingPage`
- CI-508 - Allowing DIT services pages to be children of invest, capital invest and trade home pages
- CI-510 - Updated help panel to mirror front-end changes
- XOT-1124 - Add icon and pages count to industry tags
- CI-518 - Added new how dit help fields to International Home page

### Fixed bugs
- No ticket - Add missing field to serializer

## [2019.09.19](https://github.com/uktrade/directory-cms/releases/tag/2019.09.19)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.09.18...2019.09.19)

### Implemented enhancements
- CI-498 - Changed ebook pdf to a cta link
- XOT-1039 - Add campaign block to Great Domestic Homepage
- No ticket - Add database fixtures and update readme with usage instructions
- CI-503 - Added fields to WhyChooseUkPage for ready to trade

## [2019.09.18](https://github.com/uktrade/directory-cms/releases/tag/2019.09.18)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.08.27_1...2019.09.18)

### Implemented enhancements
- No ticket - Reinstate db template and add makefile commands to make setting up fresh database faster
- CMS-1732 - Add new fields to HPO detail page for image alt and video transcript
- XOT-1035 - Add hero image renditions for new responsive frontend component
- XOT-1020 - Added extra fields to article page type (domestic and international)
- CI-460 - Added updated fields to Capital invest contact form and success pages
- CI-475 - Added featured description to About DIT services page to be used on featured cards
- CI-476 - Allow invest regions pages to be added as related regions to About UK pages
- CI-477 - Why choose the UK page can add international article page as child
- XOT-1033 - Great domestic homepage
- CI-478 - Added breadcrumbs label to capital invest landing page
- CI-474 - Allowed pages to be moved to reflect new IA, changed Invest and About UK landing pages children pages
- CI-451 - Added new fields to International home page
- CI-479 - Added video to Why choose UK Page
- CI-480 - Added SEOOptimisationPanel to more pages
- No ticket - Improve speed of test execution
- XOT-1073 Add industry tags to Country Pages
- CI-486 - Added brexit banner field to `InternationalHomePage`
- CI-496 - Updated field on `InternationalHomePage` to be markdown
- CI-492 - Added `mapped_regions` to region page
- No ticket - Add migrations check to CircleCI


### Fixed bugs
- XOT-1033 - Fix hero CTA link serializer
- No ticket - Fixed base sector page serializer being in serializer_mapping
- No ticket - Undone CI-496 changes, markdown field back to charfield


## [2019.08.27_1](https://github.com/uktrade/directory-cms/releases/tag/2019.08.27_1)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.08.27...2019.08.27_1)

### Hotfix
- no ticket - Management command that lists pages containing slug-base hyperlinking

## [2019.08.27](https://github.com/uktrade/directory-cms/releases/tag/2019.08.27)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.08.15...2019.08.27)

### Implemented enhancements
- CMS-1832 - Update django
- CMS-1753 - Remove slug links from markdown fields
- CI-431 - Added `AboutUkRegionListingPage` and `AboutUkRegionPage` which will replace `CapitalInvestRegionPage`
- CI-400 - Added related regions and text on About Uk pages for map
- XOT-1020 - Added extra fields to article page type (domestic and international)
- CMS-1716 - Remove obsolete code

### Fixed Bugs
- CMS-1830 - Move title field into translated admin panels to fix bug with untranslated tree_based_breadcrumbs


## [2019.08.15](https://github.com/uktrade/directory-cms/releases/tag/2019.08.15)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.08.08...2019.08.15)

### Implemented enhancements
- No ticket - Make teaser field optional in international articles
- No ticket - Add featured industries to Invest home page
- CI-321 - About UK landing page
- CI-276 - Added `CapitalInvestContactFormPage` and `CapitalInvestContactFormSuccessPage`
- CI-429 - Tree based breadcrumbs can now use `breadcrumbs_label` if available

### Fixed Bugs
- CI-426 - Added pdf document upload to why choose uk page for ebook section


## [2019.08.08](https://github.com/uktrade/directory-cms/releases/tag/2019.08.08)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.07.24...2019.08.08)

- CMS-1774 - Use correct slug for Invest region landing page for tree based routing
- CMS-1596 - Use correct slugs for new FAS pages under great international for tree based routing. Hide "uses tree-based routing" checkbox from admin panels
- CMS-1664 (Follow-up) - Update admin panels on international invest homepage
- CMS-1664 (Follow-up) - Update fields on international invest homepage to match those in invest/models
- No ticket - Split up code in great domestic to make files smaller
- No ticket - Update db template after new migrations added
- CMS-1692 - More small tweaks to Invest HPO pages
- CI-323 - Added "About the UK" section pages - landing page and "why choose the UK" page
- CI-365 - Changed the "Contact Us" section on the services page in "About DIT" to have its body be markdown
- TT-1689 - Move tests in the tests folder
- CI-368 - Add ebooks promotional section on "why choose the UK" page
- CI-367 - Update `CapitalInvestRegionPage`
- CI-366 - Add CTA to UK benefits section of invest home page
- CI-383 - Populated About DIT landing page
- CI-325 - Removed prioritised checkbox from capital invest opportunity page as it is now being randomised
- CI-328 - Removed unused fields for capital invest opportunity page
- No-ticket - Fix models hierarchy
- CI-404 - Clean up new Invest International home page fields that are no longer used

### Fixed Bugs
- No ticket - Fix not being able to create invest region landing page under homepage
- CI-373 - Fix panels on why choose UK page


## [2019.07.24](https://github.com/uktrade/directory-cms/releases/tag/2019.07.24)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.07.18...2019.07.24)

- XOT-932 - Add Country Guide pages to search
- CI-342 - CapitalInvestOpportunityPage gets all projects that have the same related sector as self so they can be randomised
- CI-344 - Similar projects title and related_page_one/teo/three CapitalInvestOpportunityPage` are no longer used, only removed from panels for now
- CMS-1648 - Added tree-based routing helpers


## [2019.07.18](https://github.com/uktrade/directory-cms/releases/tag/2019.07.18)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.06.27...2019.07.18)

### Implemented enhancements
- XOT-922 - Added Marketing Article Page template
- CMS-1692 - Update HPO pages to work with tree based routing. Added hero thumbnail image rendition to use with card frontend component. Changed slug for contact pages.
- CMS-1664 - Update invest homepage model to use correct new url for tree based routing
- No ticket - Split up model and admin panel code in great international app to make files much shorter and easier to work with
- CI-304 - Gave opportunity page a related region page and a scale numerical value to use for filtering
- CI-267 - Added cta text and link for sector page for related opportunities section
- CMS-1727 - Move region pages from Invest to International
- CI-324 - Made `BaseInternationalSectorPage` and sector and new sub-sector page inherit from this and opportunity listing page filters by sub sector
- CI-322 - Added "About DIT" placeholder landing page
- CI-322 - Added "About DIT" services pages

### Fixed Bugs
- NOTICKET - Capital invest landing page image serializers use aspect ratio for card images
- CMS-1737 - Fix 500 on user approval
- NOTICKET - Upgrade Django to 2.2.3 to fix vulnerability alert


## [2019.06.27](https://github.com/uktrade/directory-cms/releases/tag/2019.06.27)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.05.20...2019.06.27)

### Implemented enhancements

- CMS-1666 - Updated `slug_identity`, `slug` and `url_path` page values in accordance with directory-constants 18.0.0
- Upgraded `directory-components` to 20.0.0

### Fixed Bugs

- CMS-1678 - Fix SSO login bug by using a later version of django-staff-sso-client
- no ticket - Turn off Debug Toolbar locally by default, as it prevents some pages from being created (fix in Wagtail 2.6)
- no-ticket - Update `django-debug-toolbar` to fix django 2 incompatibility
- CMS-1676 - Fix copy upstream


## [2019.06.20](https://github.com/uktrade/directory-cms/releases/tag/2019.06.20)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.05.12...2019.06.20)

**Implemented enhancements:**

- XOT-763 - Serialize parent pages for use in breadcrumbs and GA360 page category/section
- CMS-1591 - Copy invest homepage and HPO pages in International app
- CMS-1604 - Added `WagtailAdminExclusivePageMixin` (a less restrictive version of `ExclusivePageMixin`) and used for page types in great_international
- CI-165 - Redesign of capital invest pages, added help panels to show which fields are required to get section to show on capital invest pages
- CMS-1627 - Replace GreatInternationalApp with InternationalHomePage
- CMS-1627 - Replace ExportReadinessApp with HomePage
- CI-125 - Changed field types and max_length for some fields in the capital invest opportunity pages
- CI-216 - Add icon headings to cms with default text that was old hardcoded text on Opportunity pages
- CI-211 - Created basic opportunity listing page
- CMS-1624 - Copy FAS homepage and industry contact pages in International app
- CMS-1507 - Upgraded to Django 2.2 and Wagtail 2.5

### Fixed Bugs

- CI-217 - Fix Django security vulnerability by updating to new patch version.
- CMS-1670 - Fix issue with international root page ending up with incorrect ContentType after applying migrations from CMS-1627
- NOTICKET - Removed duplicate `case_study_image` on sector page


## [2019.06.12](https://github.com/uktrade/directory-cms/releases/tag/2019.06.12)
[Full Changelog](https://github.com/uktrade/directory-cms/compare/2019.05.09...2019.06.12)

**Implemented enhancements:**

- CMS-1561 - (follow up) Don't output intro CTA dictionary when link and/or title are empty
- CMS-1561 - Removed CTA fields from accordions on country guide page. Added new CTAs to be displayed at the top of the page. Regenerated db template to speed up tests
- CMS-1419 - Added Wagtail registration view for SSO users, group info management UI, and updated user edit view to mark users as approved
- CMS-1421 - Integrate with GOV.UK Notify to send SSO user approval notifications
- CI-104 - Added capital invest landing, region, sector and opportunity pages.
- NOTICKET - Removed blanket debug logging to remove noise when using interactive shell tools
- CI-144 - Updated capital invest landing page to match more recent invision designs
- CI-148 - Updated capital invest pages to match more recent page designs
- CI-150 - Updated featured cards on Invest home page to be more flexible and all from cms
- CI-128 - Changed required fields to be nullable and added new fields for featured cards on Invest home page
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
