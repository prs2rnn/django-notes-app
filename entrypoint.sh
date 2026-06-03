#!/bin/sh

set -e

sleep 5

python manage.py migrate

python manage.py collectstatic --noinput

exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
