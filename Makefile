.PHONY: lint format mypy test

lint:
	poetry run ruff check .

format:
	poetry run black .

mypy:
	poetry run mypy .

test:
	poetry run pytest tests/
