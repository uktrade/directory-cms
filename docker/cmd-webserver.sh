#!/bin/bash -xe

python /usr/src/app/manage.py distributed_migrate --noinput
python /usr/src/app/manage.py collectstatic --noinput
python /usr/src/app/manage.py generate_google_translate_cerdentials
gunicorn config.wsgi --bind [::1]:$PORT --bind 0.0.0.0:$PORT --log-file -
