# directory-cms

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![snyk-image]][snyk]

**Directory CMS - the Department for International Trade (DIT)**

---

For more information on installation please check the [Developers Onboarding Checklist](https://uktrade.atlassian.net/wiki/spaces/ED/pages/32243946/Developers+onboarding+checklist)


## Development


We aim to follow [GDS service standards](https://www.gov.uk/service-manual/service-standard) and [GDS design principles](https://www.gov.uk/design-principles).


## Requirements
[Python 3.6](https://www.python.org/downloads/release/python-368/)

## Running locally

### Installing
    $ git clone https://github.com/uktrade/directory-cms
    $ cd directory-cms
    $ virtualenv .venv -p python3.6
    $ source .venv/bin/activate
    $ pip install -r requirements_test.txt

### Running the webserver
    $ source .venv/bin/activate
    $ make debug_webserver

### New /etc/hosts file entry

     Add 127.0.0.1 cms.trade.great

If you encounter an error along the lines of... "HTTPConnectionPool(host='cms.trade.great', port=8010): Max retries exceeded with url: /api/pages/lookup-by-slug/home/?fields=%2A&service_name=EXPORT_READINESS (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x10f103908>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known',))""

You need to update your hosts file (located at etc/hosts) with an additional line `127.0.0.1 cms.trade.great`. You can test this works by attempting to visit cms.trade.great:8010/admin in your browser

## Running the tests

    $ make debug_test

### Create a new template_sql file

    To speed up tests a SQL template file is provided. If the file becomes old run the following command on an up-to-date db instance
    $ pg_dump -O -f db_template.sql directory_cms_debug

## Session

Signed cookies are used as the session backend to avoid using a database. We therefore must avoid storing non-trivial data in the session, because the browser will be exposed to the data.

## Image storage

Pages and images can be copied "upstream" from one environment to another. To facilitate this a single S3 bucket is used by all environments. A constraint of this approach is the bucket is immutable insofar as images can be uploaded but not deleted or changed.

The following environment variables must be set on your host machine:

| env var |
| --------  |
| DIRECTORY_CMS_AWS_STORAGE_BUCKET_NAME |
| DIRECTORY_CMS_AWS_ACCESS_KEY_ID |
| DIRECTORY_CMS_AWS_SECRET_ACCESS_KEY |

Speak to a team mate or consult heroku settings to retrieve the `DIRECTORY_CMS_AWS_STORAGE_BUCKET_NAME`.


[circle-ci-image]: https://circleci.com/gh/uktrade/directory-cms/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-cms/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-cms/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-cms

[snyk-image]: https://snyk.io/test/github/uktrade/directory-cms/badge.svg
[snyk]: https://snyk.io/test/github/uktrade/directory-cms
