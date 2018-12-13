web: python manage.py distributed_migrate --noinput && gunicorn conf.wsgi --bind 0.0.0.0:$PORT
celery_worker: celery -A conf worker -l info
