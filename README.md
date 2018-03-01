# directory-cms

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gemnasium-image]][gemnasium]

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

### SASS
We use SASS CSS pre-compiler. If you're doing front-end work your local machine will also need the following dependencies:

[node](https://nodejs.org/en/download/)

[SASS](https://rubygems.org/gems/sass/versions/3.4.22)

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

### CSS development

When doing front-end development work you will need to be able to compile SASS to CSS. First run:

    $ npm install

Then:

    $ gulp sass

...to compile sass. You can also watch for changes by running:

    $ gulp sass:watch

We add compiled CSS files to version control. This will sometimes result in conflicts if multiple developers are working on the same SASS files. However, by adding the compiled CSS to version control we avoid having to install node, npm, node-sass, etc to non-development machines.

You should not edit CSS files directly, instead edit their SCSS counterparts.

## Session

Signed cookies are used as the session backend to avoid using a database. We therefore must avoid storing non-trivial data in the session, because the browser will be exposed to the data.

## Image storage

Pages and images can be copied "upstream" from one environment to another. To facilitate this a single S3 bucket is used by all environments. A constraint of this approach is the bucket is immutable insofar as images can be uploaded but not deleted or changed.

## Page auto-translations

Google Translate is used to automatically translate pages. To facilitate the authentication with Google, ask a colleague to share the Google authentication key file with you, then transpose the values from the keyfile to env vars on your machine:

| env var | source                      |
| --------  | ------------------------ |
| DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_ID | private_key_id    |
| DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_B64* | private_key |
| DIRECTORY_CMS_GOOGLE_TRANSLATE_CLIENT_EMAIL | client_email      |
| DIRECTORY_CMS_GOOGLE_TRANSLATE_CLIENT_ID | client_email_id      |
| DIRECTORY_CMS_GOOGLE_TRANSLATE_CERT_URL | client_x509_cert_url  |

*`DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_B64` is derived from the value of `private_key` by base64 encoding `private_key`. This is done to avoid complications surrounding control characters and white space across different environments (Linux, Mac, Heroku).

```
export DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_ID=...
export DIRECTORY_CMS_GOOGLE_TRANSLATE_CLIENT_EMAIL=...
export DIRECTORY_CMS_GOOGLE_TRANSLATE_CLIENT_ID=...
export DIRECTORY_CMS_GOOGLE_TRANSLATE_CERT_URL=...
export DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY=$'-----BEGIN PRIVATE KEY-----...-----END PRIVATE KEY-----\n'
export DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_B64=`python -c "
import os
import base64
value = bytes(os.environ['DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY'], 'utf8')
print(base64.b64encode(value).decode())
"`
```

The steps for generating a new key file can be found [here](https://cloud.google.com/translate/docs/reference/libraries#setting_up_authentication)


[circle-ci-image]: https://circleci.com/gh/uktrade/directory-cms/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-cms/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-cms/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-cms

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-cms.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-cms
