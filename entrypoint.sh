#!/bin/sh
sleep 3
cd project
python manage.py migrate
python manage.py collectstatic  --noinput
gunicorn project.wsgi:application --bind 0.0.0.0:8000
exec "$@"
