# Extract the arguments after the first target word
RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
# Convert those argument words into empty, do-nothing targets
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
