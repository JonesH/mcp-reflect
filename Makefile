.PHONY: lint fix format mypy test

lint:
	poetry run ruff check .

fix:
	poetry run ruff --fix --unsafe-fixes .

format:
	poetry run black .

mypy:
	poetry run mypy .

test:
	poetry run pytest tests/
