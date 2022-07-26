#!/bin/sh
set -e

# Ready for DB connection
bash ./wait-for-it.sh -t 30 db:5432

python manage.py migrate

# Create superuser if not exists
python manage.py createsuperuser \
  --noinput \
  --username $DJANGO_SUPERUSER_USERNAME \
  --email $DJANGO_SUPERUSER_EMAIL \
  || echo "Skip creating superuser."

# Start up
python manage.py runserver 0.0.0.0:8000

exec "$@"
