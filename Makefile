install-precommit:
	# Installs pre-commit, will raise errors if pipx is not installed
	pipx install pre-commit


run-precommit: install-precommit
	# Runs all pre-commit hooks, automatically runs during commits.
	pre-commit run
