.PHONY: runserver
runserver:
	poetry run python -m manage runserver
	
.PHONY: migrate
migrate:
	poetry run python -m manage migrate

.PHONY: migrations
migrations:
	poetry run python -m manage makemigrations

.PHONY: runworker
runworker:
	poetry run python -m celery -A TTSAPI worker --pool threads