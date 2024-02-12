#!/bin/bash

# Wait for the database to be ready
while ! pg_isready -h db -U $DB_USER -d $DB_NAME; do
  echo "Waiting for database to become available..."
  sleep  1
done

python manage.py makemigrations
python manage.py migrate
exec python manage.py runserver  0.0.0.0:8000