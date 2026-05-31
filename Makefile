run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makem:
	poetry run python manage.py makemigrations

createsu:
	poetry run python manage.py createsuperuser


# Extract the arguments after the first target word
RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
# Convert those argument words into empty, do-nothing targets
$(eval $(RUN_ARGS):;@:)

startapp:
	poetry run python manage.py startapp $(RUN_ARGS)
