#!/bin/bash

# Bekleme işlemini gerçekleştir
while ! pg_isready -h db -U $DB_USER -d $DB_NAME; do
  echo "Veritabanı hazır olana kadar bekleniyor..."
  sleep 1
done

# Migrate işlemi gerçekleştir
python manage.py migrate

# Django uygulamasını başlat
exec python manage.py runserver 0.0.0.0:8000
