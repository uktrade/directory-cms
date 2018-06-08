build: docker_test

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -r requirements_test.txt

FLAKE8 := flake8 . --exclude=migrations,.venv,node_modules
PYTEST := pytest . -v --ignore=node_modules --cov=. --cov-config=.coveragerc --capture=no $(pytest_args)
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
	if [ "$$FEATURE_AUTO_TRANSLATE_ENABLED" != "" ]; then \
		python manage.py generate_google_translate_cerdentials; \
	fi && \
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
	$(DEBUG_SET_ENV_VARS) && ./manage.py makemigrations core export_readiness find_a_supplier


DOCKER_COMPOSE_REMOVE_AND_PULL := docker-compose -f docker-compose.yml -f docker-compose-test.yml rm -f && docker-compose -f docker-compose.yml -f docker-compose-test.yml pull
DOCKER_COMPOSE_CREATE_ENVS := python ./docker/env_writer.py ./docker/env.json ./docker/env.test.json ./docker/env-postgres.test.json ./docker/env-postgres.json

docker_run:
	$(DOCKER_COMPOSE_CREATE_ENVS) && \
	$(DOCKER_COMPOSE_REMOVE_AND_PULL) && \
	docker-compose up --build

DOCKER_SET_DEBUG_ENV_VARS := \
	export DIRECTORY_CMS_SESSION_COOKIE_SECURE=false; \
	export DIRECTORY_CMS_PORT=8010; \
	export DIRECTORY_CMS_SECRET_KEY=debug; \
	export DIRECTORY_CMS_POSTGRES_USER=debug; \
	export DIRECTORY_CMS_POSTGRES_PASSWORD=debug; \
	export DIRECTORY_CMS_POSTGRES_DB=directory_cms_debug; \
	export DIRECTORY_CMS_DEBUG=true; \
	export DIRECTORY_CMS_UTM_COOKIE_DOMAIN=.great; \
	export DIRECTORY_CMS_SECURE_HSTS_SECONDS=0; \
	export DIRECTORY_CMS_PYTHONWARNINGS=all; \
	export DIRECTORY_CMS_PYTHONDEBUG=true; \
	export DIRECTORY_CMS_GREAT_EXPORT_HOME=/; \
	export DIRECTORY_CMS_CUSTOM_PAGE=/custom; \
	export DIRECTORY_CMS_EXPORTING_NEW=/new; \
	export DIRECTORY_CMS_EXPORTING_OCCASIONAL=/occasional; \
	export DIRECTORY_CMS_EXPORTING_REGULAR=/regular; \
	export DIRECTORY_CMS_GUIDANCE_MARKET_RESEARCH=/market-research; \
	export DIRECTORY_CMS_GUIDANCE_CUSTOMER_INSIGHT=/customer-insight; \
	export DIRECTORY_CMS_GUIDANCE_FINANCE=/finance; \
	export DIRECTORY_CMS_GUIDANCE_BUSINESS_PLANNING=/business-planning; \
	export DIRECTORY_CMS_GUIDANCE_GETTING_PAID=/getting-paid; \
	export DIRECTORY_CMS_GUIDANCE_OPERATIONS_AND_COMPLIANCE=/operations-and-compliance; \
	export DIRECTORY_CMS_SERVICES_EXOPPS_INTERSTITIAL=/export-opportunities; \
	export DIRECTORY_CMS_SERVICES_EXOPPS=http://opportunities.export.great.gov.uk; \
	export DIRECTORY_CMS_SERVICES_FAB=http://buyer.trade.great:8001; \
	export DIRECTORY_CMS_SERVICES_GET_FINANCE=/get-finance; \
	export DIRECTORY_CMS_SERVICES_SOO=http://soo.trade.great:8008; \
	export DIRECTORY_CMS_INFO_ABOUT=/about; \
	export DIRECTORY_CMS_INFO_PRIVACY_AND_COOKIES=/privacy-and-cookies; \
	export DIRECTORY_CMS_INFO_TERMS_AND_CONDITIONS=/terms-and-conditions; \
	export DIRECTORY_CMS_SECURE_SSL_REDIRECT=false; \
	export DIRECTORY_CMS_HEALTH_CHECK_TOKEN=debug; \
	export DIRECTORY_CMS_SIGNATURE_SECRET=debug; \
	export DIRECTORY_CMS_BASE_URL=cms.trade.great; \
	export DIRECTORY_CMS_DATABASE_URL=postgres://debug:debug@postgres:5432/directory_cms_debug; \
	export DIRECTORY_CMS_CSRF_COOKIE_SECURE=false; \
	export DIRECTORY_CMS_APP_URL_EXPORT_READINESS=http://exred.trade.great:8007; \
	export DIRECTORY_CMS_APP_URL_FIND_A_SUPPLIER=http://supplier.trade.great:8005; \
	export DIRECTORY_CMS_COPY_DESTINATION_URLS=https://dev.cms.directory.uktrade.io,https://stage.cms.directory.uktrade.io; \
	export DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_ID=debug; \
	export DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_B64="ZGVidWc="; \
	export DIRECTORY_CMS_GOOGLE_TRANSLATE_CLIENT_EMAIL=debug; \
	export DIRECTORY_CMS_GOOGLE_TRANSLATE_CLIENT_ID=debug; \
	export DIRECTORY_CMS_GOOGLE_TRANSLATE_CERT_URL=debug; \
	export DIRECTORY_CMS_GOOGLE_APPLICATION_CREDENTIALS=config/google-cloud-credentials.json; \
	export DIRECTORY_CMS_EMAIL_BACKEND_CLASS_NAME=console; \
	export DIRECTORY_CMS_EMAIL_HOST=debug; \
	export DIRECTORY_CMS_EMAIL_PORT=debug; \
	export DIRECTORY_CMS_EMAIL_HOST_USER=debug; \
	export DIRECTORY_CMS_EMAIL_HOST_PASSWORD=debug; \
	export DIRECTORY_CMS_DEFAULT_FROM_EMAIL=debug

DOCKER_SET_TEST_ENV_VARS := \
	export DIRECTORY_CMS_DEFAULT_FILE_STORAGE=core.storage_backends.FileSystemStorage

docker_test_env_files:
	$(DOCKER_SET_DEBUG_ENV_VARS) && \
	$(DOCKER_SET_TEST_ENV_VARS) && \
	$(DOCKER_COMPOSE_CREATE_ENVS)

DOCKER_REMOVE_ALL := \
	docker ps -a | \
	grep directoryui_ | \
	awk '{print $$1 }' | \
	xargs -I {} docker rm -f {}

docker_remove_all:
	$(DOCKER_REMOVE_ALL)

docker_debug: docker_remove_all
	$(DOCKER_SET_DEBUG_ENV_VARS) && \
	$(DOCKER_COMPOSE_CREATE_ENVS) && \
	docker-compose pull && \
	docker-compose build && \
	docker-compose run --service-ports webserver make django_webserver

docker_webserver_bash:
	docker exec -it directoryui_webserver_1 sh

docker_test: docker_remove_all
	$(DOCKER_SET_DEBUG_ENV_VARS) && \
	$(DOCKER_SET_TEST_ENV_VARS) && \
	$(DOCKER_COMPOSE_CREATE_ENVS) && \
	$(DOCKER_COMPOSE_REMOVE_AND_PULL) && \
	docker-compose -f docker-compose-test.yml build && \
	docker-compose -f docker-compose-test.yml run sut

docker_build:
	docker build -t ukti/directory-ui-export-readiness:latest .

DEBUG_SET_ENV_VARS := \
	export PORT=8010; \
	export SECRET_KEY=debug; \
	export DEBUG=true ;\
	export SESSION_COOKIE_SECURE=false; \
	export UTM_COOKIE_DOMAIN=.great; \
	export SECURE_HSTS_SECONDS=0; \
	export PYTHONWARNINGS=all; \
	export PYTHONDEBUG=true; \
	export GREAT_EXPORT_HOME=/; \
	export CUSTOM_PAGE=/custom; \
	export EXPORTING_NEW=/new; \
	export EXPORTING_OCCASIONAL=/occasional; \
	export EXPORTING_REGULAR=/regular; \
	export GUIDANCE_MARKET_RESEARCH=/market-research; \
	export GUIDANCE_CUSTOMER_INSIGHT=/customer-insight; \
	export GUIDANCE_FINANCE=/finance; \
	export GUIDANCE_BUSINESS_PLANNING=/business-planning; \
	export GUIDANCE_GETTING_PAID=/getting-paid; \
	export GUIDANCE_OPERATIONS_AND_COMPLIANCE=/operations-and-compliance; \
	export SERVICES_EXOPPS=/export-opportunities; \
	export SERVICES_EXOPPS_ACTUAL=http://opportunities.export.great.gov.uk; \
	export SERVICES_FAB=http://buyer.trade.great:8001; \
	export SERVICES_GET_FINANCE=/get-finance; \
	export SERVICES_SOO=http://soo.trade.great:8008; \
	export INFO_ABOUT=/about; \
	export INFO_PRIVACY_AND_COOKIES=/privacy-and-cookies; \
	export INFO_TERMS_AND_CONDITIONS=/terms-and-conditions; \
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
	export COPY_DESTINATION_URLS=https://directory-cms-dev.herokuapp.com,https://dev.cms.directory.uktrade.io,https://stage.cms.directory.uktrade.io,http://cms.trade.great:8010; \
	export GOOGLE_APPLICATION_CREDENTIALS=config/google-cloud-credentials.json; \
	export GOOGLE_TRANSLATE_PRIVATE_KEY_ID=$$DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_ID; \
	export GOOGLE_TRANSLATE_PRIVATE_KEY_B64=$$DIRECTORY_CMS_GOOGLE_TRANSLATE_PRIVATE_KEY_B64; \
	export GOOGLE_TRANSLATE_CLIENT_EMAIL=$$DIRECTORY_CMS_GOOGLE_TRANSLATE_CLIENT_EMAIL; \
	export GOOGLE_TRANSLATE_CLIENT_ID=$$DIRECTORY_CMS_GOOGLE_TRANSLATE_CLIENT_ID; \
	export GOOGLE_TRANSLATE_CERT_URL=$$DIRECTORY_CMS_GOOGLE_TRANSLATE_CERT_URL; \
	export AWS_STORAGE_BUCKET_NAME=$$DIRECTORY_CMS_AWS_STORAGE_BUCKET_NAME; \
	export AWS_ACCESS_KEY_ID=$$DIRECTORY_CMS_AWS_ACCESS_KEY_ID; \
	export AWS_SECRET_ACCESS_KEY=$$DIRECTORY_CMS_AWS_SECRET_ACCESS_KEY; \
	export EMAIL_BACKEND_CLASS_NAME=console; \
	export EMAIL_HOST=$$DIRECTORY_CMS_EMAIL_HOST; \
	export EMAIL_PORT=$$DIRECTORY_CMS_EMAIL_PORT; \
	export EMAIL_HOST_USER=$$DIRECTORY_CMS_EMAIL_HOST_USER; \
	export EMAIL_HOST_PASSWORD=$$DIRECTORY_CMS_EMAIL_HOST_PASSWORD; \
	export DEFAULT_FROM_EMAIL=$$DIRECTORY_CMS_DEFAULT_FROM_EMAIL; \
	export FEATURE_AUTO_TRANSLATE_ENABLED=true

TEST_SET_ENV_VARS := \
	export DEFAULT_FILE_STORAGE=core.storage_backends.FileSystemStorage

debug_webserver:
	$(DEBUG_SET_ENV_VARS) && $(DJANGO_WEBSERVER)

debug_pytest:
	$(DEBUG_SET_ENV_VARS) && $(TEST_SET_ENV_VARS) && $(COLLECT_STATIC) && $(DJANGO_MIGRATE) && $(SYNC_TRANSLATION_FIELDS) && $(PYTEST)

debug_test:
	$(DEBUG_SET_ENV_VARS) && $(TEST_SET_ENV_VARS) && $(COLLECT_STATIC) && $(DJANGO_MIGRATE) && $(SYNC_TRANSLATION_FIELDS) && $(FLAKE8) && $(PYTEST) --cov-report=html

debug_test_last_failed:
	make debug_test pytest_args='-v --last-failed'

debug_manage:
	$(DEBUG_SET_ENV_VARS) && ./manage.py $(cmd)

debug_shell:
	$(DEBUG_SET_ENV_VARS) && ./manage.py shell

debug: debug_db test_requirements debug_test

heroku_deploy_dev:
	./docker/install_heroku_cli.sh
	docker login --username=$$HEROKU_EMAIL --password=$$HEROKU_TOKEN registry.heroku.com
	~/bin/heroku-cli/bin/heroku container:push web --app directory-cms-dev
	~/bin/heroku-cli/bin/heroku container:release web --app directory-cms-dev

compile_requirements:
	pip-compile requirements.in

upgrade_requirements:
	pip-compile --upgrade requirements.in

compile_test_requirements:
	pip-compile requirements_test.in

upgrade_test_requirements:
	pip-compile --upgrade requirements_test.in

compile_all_requirements: compile_requirements compile_test_requirements

upgrade_all_requirements: upgrade_requirements upgrade_test_requirements

.PHONY: build clean test_requirements docker_run docker_debug docker_webserver_bash docker_test debug_webserver debug_test debug heroku_deploy_dev heroku_deploy_demo
