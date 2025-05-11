.PHONY: lint fix format mypy test

lint:
	poetry run ruff check .

fix:
	poetry run ruff format .

format:
	poetry run black .

mypy:
	poetry run mypy .

test:
	poetry run pytest tests/

all:
	@echo "Running auto fixes..."
	$(MAKE) fix
	@echo "Formatting code..."
	$(MAKE) format
	@echo "Linting code..."
	$(MAKE) lint
	@echo "Running mypy type checks..."
	$(MAKE) mypy
	@echo "Running tests..."
	$(MAKE) test
