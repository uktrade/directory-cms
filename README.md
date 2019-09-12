# directory-cms

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gitflow-image]][gitflow]
[![calver-image]][calver]

**Directory CMS - the Department for International Trade (DIT)**

---

## Development

### Installing
    $ git clone https://github.com/uktrade/directory-cms
    $ cd directory-cms
    $ virtualenv .venv -p python3.6
    $ source .venv/bin/activate
    $ pip install -r requirements_test.txt
    # Start postgres now before proceeding.
    $ make debug_db
    $ make debug_migrate
    $ make debug_createsuperuser


### Requirements
[Python 3.6](https://www.python.org/downloads/release/python-368/)

[Postgres 9.5](https://www.postgresql.org/)

[Redis](https://redis.io/)


#### Configuration

Secrets such as API keys and environment specific configurations are placed in `conf/env/secrets-do-not-commit` - a file that is not added to version control. To create a template secrets file with dummy values run `make init_secrets`.

### Commands

| Command                       | Description |
| ----------------------------- | ------------|
| make clean                    | Delete pyc files |
| make pytest                   | Run all tests |
| make pytest test_foo.py       | Run all tests in file called test_foo.py |
| make pytest -- --last-failed` | Run the last tests to fail |
| make pytest -- -k foo         | Run the test called foo |
| make pytest -- <foo>          | Run arbitrary pytest command |
| make flake8                   | Run linting |
| make manage <foo>             | Run arbitrary management command |
| make webserver                | Run the development web server |
| make requirements             | Compile the requirements file |
| make install_requirements     | Installed the compile requirements file |
| make css                      | Compile scss to css |
| make init_secrets             | Create your secret env var file |
| make worker                   | Run async cache celery worker |

### Image storage

Pages and images can be copied "upstream" from one environment to another. To facilitate this a single S3 bucket is used by all environments. A constraint of this approach is the bucket is immutable insofar as images can be uploaded but not deleted or changed.

The entries must be added on your `conf/.env` file:
```
AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```

Speak to a team mate or consult dev vault to retrieve the `AWS_STORAGE_BUCKET_NAME`.

#### /etc/hosts file entry

UI clients on local expect the CMS to be reachable at the address http://cms.trade.great.

     Add 127.0.0.1 cms.trade.great

You can test this works by attempting to visit http://cms.trade.great:8010/admin in your browser.


## Running the webserver
    $ source .venv/bin/activate
    $ make debug_webserver

## Running the tests

    $ make debug_test

### Create a new template_sql file

    To speed up tests a SQL template file is provided. If the file becomes obsolete run the following command on an up-to-date db instance to improve test speeds locally.

    *NOTE:* You should avoid committing updated database templates to the repository, as doing so has the potential to expose sensitive data from your copy of the database. Only templates created from a freshly created/migrated database should ever be committed to the repository.

    $ make update_db_template


## Session

Signed cookies are used as the session backend to avoid using a database. We therefore must avoid storing non-trivial data in the session, because the browser will be exposed to the data.


## Caching

When adding new pages the following steps should be followed to ensure they are added to the cache:

1. Add an entry to the sub-app's cache.py e.g.:
```
class MyPageSubscriber(AbstractDatabaseCacheSubscriber):
    model = models.MyPage
    subscriptions = [
        models.RelatedPageOne,
        models.RelatedpageTwo,
    ]
```

2. Add `MyPageSubscriber.subscribe()` to the sub-apps's `apps.py`

Note on `subscriptions`: the page is serialized when saved to the cache as a JSON document. The serializer may contain content provided by another page. How do we clear the page's cache when related content changes? By adding the related page to `subscriptions` . Any model defined in `subscriptions` will result in the cache entry being cleared when related content is changed.


## Staff SSO

On local machine, SSO is turned off by default.
If you need to enable, set the `FEATURE_ENFORCE_STAFF_SSO_ENABLED` to `true`.
You also need to set:
```
STAFF_SSO_AUTHBROKER_URL
AUTHBROKER_CLIENT_ID
AUTHBROKER_CLIENT_SECRET
```

Speak to webops or a team mate for the above values.


## Helpful links
* [Developers Onboarding Checklist](https://uktrade.atlassian.net/wiki/spaces/ED/pages/32243946/Developers+onboarding+checklist)
* [Gitflow branching](https://uktrade.atlassian.net/wiki/spaces/ED/pages/737182153/Gitflow+and+releases)
* [GDS service standards](https://www.gov.uk/service-manual/service-standard)
* [GDS design principles](https://www.gov.uk/design-principles)

## Related projects:
https://github.com/uktrade?q=directory

https://github.com/uktrade?q=great

[code-climate-image]: https://codeclimate.com/github/uktrade/directory-cms/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-cms

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-cms/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-cms/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-cms/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-cms

[gitflow-image]: https://img.shields.io/badge/Branching%20strategy-gitflow-5FBB1C.svg
[gitflow]: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

[calver-image]: https://img.shields.io/badge/Versioning%20strategy-CalVer-5FBB1C.svg
[calver]: https://calver.org
