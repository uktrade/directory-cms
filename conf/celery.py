from __future__ import absolute_import, unicode_literals
import os
from ssl import CERT_NONE

from django.conf import settings

from celery import Celery

# note AUTHBROKER_URL is misidentified as a secret by celery when pidbox is used, resulting in
# celery trying to parse AUTHBROKER_URL as a transport, resulting in error. so turn the feature off in Procfile

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('cms')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

if settings.FEATURE_REDIS_USE_SSL:
    ssl_conf = {
        'ssl_cert_reqs': CERT_NONE,
        'ssl_ca_certs': None,
        'ssl_certfile': None,
        'ssl_keyfile': None
    }
    app.conf.broker_use_ssl = ssl_conf
    app.conf.redis_backend_use_ssl = ssl_conf

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
