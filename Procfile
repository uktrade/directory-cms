web: python manage.py distributed_migrate --noinput && gunicorn conf.wsgi --worker-class gevent --worker-connections 1000 --bind 0.0.0.0:$PORT
celery_worker: FEATURE_ENFORCE_STAFF_SSO_ENABLED=False celery -A conf worker -l info
celery_beat: FEATURE_ENFORCE_STAFF_SSO_ENABLED=False celery -A conf beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler