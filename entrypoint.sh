#!/bin/sh

# Initiate database if it's a new one
python manage.py makemigrations

# Apply database migrations

python manage.py migrate

# Run import pokemon command to load data from CSV
python manage.py import_pokemon

# Start server
python manage.py runserver 0.0.0.0:8000


