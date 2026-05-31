run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makem:
	poetry run python manage.py makemigrations

createsu:
	poetry run python manage.py createsuperuser
