# Extract arguments
RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(RUN_ARGS):;@:)

runserver:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

createsuperuser:
	poetry run python manage.py createsuperuser

startapp:
	poetry run python manage.py startapp $(RUN_ARGS)

collectstatic:
	poetry run python manage.py collectstatic

shell:
	poetry run python manage.py shell

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

check:
	poetry run ruff check .
	poetry run ruff format --check .
	poetry run python manage.py check
	poetry run python manage.py makemigrations --check --dry-run

test:
	poetry run pytest

ci:
	make check
# 	make test

install-hooks:
	./scripts/install-hooks.sh

docker-up:
	docker compose up --build

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f

# Production
prod-down:
	docker compose \
	-f docker-compose.prod.yml \
	down

prod-shell:
	docker compose \
	-f docker-compose.prod.yml \
	exec web python manage.py shell

prod-admin:
	docker compose \
	-f docker-compose.prod.yml \
	exec web python manage.py createsuperuser

deploy:
	./scripts/deploy.sh

logs:
	./scripts/logs.sh

# Help
help:
	@echo "runserver         Start Django server"
	@echo "migrate           Apply migrations"
	@echo "makemigrations    Create migrations"
	@echo "createsuperuser   Create admin user"
	@echo "collectstatic     Collect static files"
	@echo "check             Run quality checks"
	@echo "test              Run tests"
	@echo "ci                Run full CI locally"
	@echo "install-hooks     Install git hooks"
	@echo "deploy            Deploy project"
