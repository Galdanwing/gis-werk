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
