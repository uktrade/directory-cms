clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -r requirements_test.txt

FLAKE8 := flake8 . --exclude=migrations,.venv
PYTEST := pytest . -v --ignore=venv --ignore=conf/celery.py --cov=. --cov-config=.coveragerc --capture=no $(pytest_args)
PYTEST_FIXTURES := pytest --fixtures
COLLECT_STATIC := python manage.py collectstatic --noinput
DJANGO_MIGRATE := python manage.py distributed_migrate --noinput
SYNC_TRANSLATION_FIELDS := python manage.py sync_page_translation_fields --noinput

CODECOV := \
	if [ "$$CODECOV_REPO_TOKEN" != "" ]; then \
	   codecov --token=$$CODECOV_REPO_TOKEN ;\
	fi

test:
	$(COLLECT_STATIC) && $(DJANGO_MIGRATE) && $(SYNC_TRANSLATION_FIELDS) && $(FLAKE8) && $(PYTEST) && $(CODECOV)

DJANGO_WEBSERVER := \
	python manage.py collectstatic --noinput && \
	python manage.py runserver 0.0.0.0:$$PORT

django_webserver:
	$(DJANGO_WEBSERVER)


DEBUG_CREATE_DB := \
	psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = '$$DB_NAME'" | \
	grep -q 1 || psql -U postgres -c "CREATE DATABASE $$DB_NAME"; \
	psql -U postgres -tc "SELECT 1 FROM pg_roles WHERE rolname = '$$DB_USER'" | \
	grep -q 1 || echo "CREATE USER $$DB_USER WITH PASSWORD '$$DB_PASSWORD'; GRANT ALL PRIVILEGES ON DATABASE \"$$DB_NAME\" to $$DB_USER; ALTER USER $$DB_USER CREATEDB" | psql -U postgres

debug_db:
	$(DEBUG_SET_ENV_VARS) && $(DEBUG_CREATE_DB)

migrations:
	$(DEBUG_SET_ENV_VARS) && ./manage.py makemigrations core export_readiness find_a_supplier invest components great_international


DEBUG_SET_ENV_VARS := \
	export PORT=8010; \
	export SECRET_KEY=debug; \
	export DEBUG=true;\
	export SESSION_COOKIE_SECURE=false; \
	export UTM_COOKIE_DOMAIN=.great; \
	export SECURE_HSTS_SECONDS=0; \
	export PYTHONDEBUG=true; \
	export GREAT_EXPORT_HOME=/; \
	export CUSTOM_PAGE=/custom; \
	export SECURE_SSL_REDIRECT=false; \
	export HEALTH_CHECK_TOKEN=debug; \
	export SIGNATURE_SECRET=debug; \
	export BASE_URL=cms.trade.great; \
	export DB_NAME=directory_cms_debug; \
	export DB_USER=debug; \
	export DB_PASSWORD=debug; \
	export DATABASE_URL=postgres://debug:debug@localhost:5432/directory_cms_debug; \
	export CSRF_COOKIE_SECURE=false; \
	export APP_URL_EXPORT_READINESS=http://exred.trade.great:8007; \
	export APP_URL_FIND_A_SUPPLIER=http://supplier.trade.great:8005; \
	export APP_URL_INVEST=http://invest.trade.great:8011; \
	export APP_URL_GREAT_INTERNATIONAL=http://international.trade.great:8012/international/; \
	export COPY_DESTINATION_URLS=https://directory-cms-dev.herokuapp.com,https://dev.cms.directory.uktrade.io,https://stage.cms.directory.uktrade.io,http://cms.trade.great:8010; \
	export AWS_STORAGE_BUCKET_NAME=$$DIRECTORY_CMS_AWS_STORAGE_BUCKET_NAME; \
	export AWS_ACCESS_KEY_ID=$$DIRECTORY_CMS_AWS_ACCESS_KEY_ID; \
	export AWS_SECRET_ACCESS_KEY=$$DIRECTORY_CMS_AWS_SECRET_ACCESS_KEY; \
	export EMAIL_BACKEND_CLASS_NAME=console; \
	export EMAIL_HOST=$$DIRECTORY_CMS_EMAIL_HOST; \
	export EMAIL_PORT=$$DIRECTORY_CMS_EMAIL_PORT; \
	export EMAIL_HOST_USER=$$DIRECTORY_CMS_EMAIL_HOST_USER; \
	export EMAIL_HOST_PASSWORD=$$DIRECTORY_CMS_EMAIL_HOST_PASSWORD; \
	export DEFAULT_FROM_EMAIL=$$DIRECTORY_CMS_DEFAULT_FROM_EMAIL; \
	export FEATURE_DEBUG_TOOLBAR_ENABLED=true; \
	export REDIS_CACHE_URL=redis://localhost:6379; \
	export REDIS_CELERY_URL=redis://localhost:6379/1; \
	export API_CACHE_DISABLED=true; \
	export ENVIRONMENT_CSS_THEME_FILE=core/css/environment_dev_theme.css; \
	export CELERY_ALWAYS_EAGER=true; \
	export ACTIVITY_STREAM_ACCESS_KEY_ID=123-id-key; \
	export ACTIVITY_STREAM_SECRET_ACCESS_KEY=123-secret-key



TEST_SET_ENV_VARS := \
	export DEFAULT_FILE_STORAGE=core.storage_backends.FileSystemStorage; \
	export API_CACHE_DISABLED=false; \
	export STATICFILES_STORAGE=django.contrib.staticfiles.storage.StaticFilesStorage; \
	export DEBUG=false

debug_webserver:
	$(DEBUG_SET_ENV_VARS) && $(DJANGO_WEBSERVER)

debug_pytest_no_migrations:
	$(DEBUG_SET_ENV_VARS) && $(TEST_SET_ENV_VARS) && pytest -vv --nomigrations --reuse-db --ignore=node_modules --capture=no $(pytest_args)

debug_pytest:
	$(DEBUG_SET_ENV_VARS) && $(TEST_SET_ENV_VARS) && $(PYTEST)

debug_pytest_fixtures:
	$(DEBUG_SET_ENV_VARS) && $(TEST_SET_ENV_VARS) && $(PYTEST_FIXTURES)

debug_test:
	$(DEBUG_SET_ENV_VARS) && $(TEST_SET_ENV_VARS) && $(PYTEST) --cov-report=html

debug_test_last_failed:
	make debug_test pytest_args='-v --last-failed'

debug_manage:
	$(DEBUG_SET_ENV_VARS) && ./manage.py $(cmd)

debug_shell:
	$(DEBUG_SET_ENV_VARS) && ./manage.py shell

debug: debug_db test_requirements debug_test

debug_celery_worker:
	$(DEBUG_SET_ENV_VARS); celery -A conf worker -l info

compile_requirements:
	pip-compile requirements.in
	pip-compile requirements_test.in

upgrade_requirements:
	pip-compile --upgrade requirements.in
	pip-compile --upgrade requirements_test.in

.PHONY: clean test_requirements debug_webserver debug_test debug
