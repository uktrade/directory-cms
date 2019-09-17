ARGUMENTS = $(filter-out $@,$(MAKECMDGOALS)) $(filter-out --,$(MAKEFLAGS))

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

pytest:
	ENV_FILES='test,dev' \
	pytest tests $(ARGUMENTS) \
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

manage:
	ENV_FILES='secrets-do-not-commit,dev' ./manage.py $(ARGUMENTS)

check_migrations:
	yes n | ENV_FILES='test,dev' ./manage.py migrate --plan

webserver:
	ENV_FILES='secrets-do-not-commit,dev' python manage.py runserver 0.0.0.0:8010 $(ARGUMENTS)

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

setup_db:
	PGPASSWORD=debug dropdb  directory_cms_debug
	PGPASSWORD=debug createdb -h localhost -U debug directory_cms_debug
	PGPASSWORD=debug psql -h localhost -U debug -d directory_cms_debug -f db_template.sql >/dev/null 2>&1

update_db_template:
	createdb -U postgres -h localhost cms_temporary_template
	psql -U postgres -h localhost -d cms_temporary_template -f db_template.sql
	ENV_FILES='secrets-do-not-commit,dev' \
	export DATABASE_URL=postgres://postgres:postgres@localhost:5432/cms_temporary_template; \
	python ./manage.py migrate
	pg_dump -U postgres \
		--no-owner \
		--file=db_template.sql \
		--dbname=cms_temporary_template
	dropdb -U postgres cms_temporary_template

dummy_data:
	ENV_FILES='secrets-do-not-commit,dev' ./manage.py loaddata fixtures/data.json

.PHONY: clean pytest flake8 manage webserver requirements install_requirements css worker check_migrations
