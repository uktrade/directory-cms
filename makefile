ARGUMENTS = $(filter-out $@,$(MAKECMDGOALS)) $(filter-out --,$(MAKEFLAGS))
TESTFILES?=tests

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

ENV_VAR?='test,dev'
pytest:
	ENV_FILES=$(ENV_FILES) \
	pytest $(TESTFILES) $(ARGUMENTS) \
	--ignore=node_modules \
	--ignore=conf/celery.py \
	--capture=no \
	--nomigrations \
	--reuse-db \
	-W ignore::DeprecationWarning \
	-vv

flake8:
	flake8 . \
	--exclude=.venv,venv,node_modules,migrations \
	--max-line-length=120

ENV_VAR?='secrets-do-not-commit,dev'
manage:
	ENV_FILES=$(ENV_FILES) ./manage.py $(ARGUMENTS)

ENV_VAR?='secrets-do-not-commit,dev'
webserver:
	ENV_FILES=$(ENV_FILES) python manage.py runserver 0.0.0.0:8010 $(ARGUMENTS)

requirements:
	pip-compile requirements.in
	pip-compile requirements_test.in

install_requirements:
	pip install -r requirements_test.txt

css:
	./node_modules/.bin/gulp sass

secrets:
	cp conf/env/secrets-template conf/env/secrets-do-not-commit; \
	sed -i -e 's/#DO NOT ADD SECRETS TO THIS FILE//g' conf/env/secrets-do-not-commit

worker:
	ENV_FILES='secrets-do-not-commit,dev' celery -A conf worker -l info

.PHONY: clean pytest flake8 manage webserver requirements install_requirements css worker
