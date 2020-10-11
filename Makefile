define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

test: ## run tests quickly with pytest
	pytest

install: clean ## install the package to the active Python's site-packages
	pip install .

repro: install ## Reproduce the analysis, excluding the reconciliation step
	cd analysis/; \
	echo "\033[1;32mChecking the matches...\033[0m"; \
	python similarity_check.py && python remove_false_matches.py; \
	echo "\033[1;32mSummarizing matches and assessing quality...\033[0m"; \
	python analyse_matches.py && python item_quality.py
	@echo "\033[1;32mDone!\033[0m"

develop: ## Initiate the environment to collaborate with the project (requires conda)
	conda env create -f environment.yml && conda activate wdt_panglaodb; \
	pip install -e .

update-proj: ## Update the project and environment to the latest remote version
	git pull origin master; \
	conda activate wdt_panglaodb && conda env update --file environment.yml

update-manu: ## Update manuscript submodules
	git submodule foreach git pull origin master