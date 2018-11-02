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
[Python 3.5](https://www.python.org/downloads/release/python-352/)

### Docker
To use Docker in your local development environment you will also need the following dependencies:

[Docker >= 1.10](https://docs.docker.com/engine/installation/)

[Docker Compose >= 1.8](https://docs.docker.com/compose/install/)

## Running locally with Docker
This requires all host environment variables to be set.

    $ make docker_run

### Run debug webserver in Docker

    $ make docker_debug

### Run tests in Docker

    $ make docker_test

### Host environment variables for docker-compose
``.env`` files will be automatically created (with ``env_writer.py`` based on ``env.json``) by ``make docker_test``, based on host environment variables with ``DIRECTORY_CMS_`` prefix.

#### Web server

## Running locally without Docker

### Installing
    $ git clone https://github.com/uktrade/directory-cms
    $ cd directory-cms
    $ virtualenv .venv -p python3.5
    $ source .venv/bin/activate
    $ pip install -r requirements_test.txt

### Running the webserver
    $ source .venv/bin/activate
    $ make debug_webserver

### Running the tests

    $ make debug_test

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
