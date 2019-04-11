web: python manage.py distributed_migrate --noinput && python manage.py update_translation_fields && gunicorn conf.wsgi --bind 0.0.0.0:$PORT
celery_worker: celery -A conf worker -l info
