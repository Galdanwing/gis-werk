install-precommit:
	# Installs pre-commit, will raise errors if pipx is not installed
	pipx install pre-commit


run-precommit: install-precommit
	# Runs all pre-commit hooks, automatically runs during commits.
	pre-commit run

start-project:
	docker compose up --build

compile-requirements:
	# update the requirements in geoProject/pyproject.toml and then run this command
	docker compose exec web pip-compile
	docker compose exec web pip-compile --extra dev -o requirements-dev.txt

run-tests:
	docker compose exec web pytest

migrate:
	docker compose exec web ./manage.py makemigrations
	docker compose exec web ./manage.py migrate

import-data:
	# Command assumes data is located in geoProject/geoProject/
	docker compose exec web ./manage.py ingest_data municipalities_nl.geojson

create-superuser:
	docker compose exec web ./manage.py createsuperuser --username admin --noinput --email admin@admin.admin
