#!/bin/sh

# Apply database migrations
python manage.py migrate

# Run import pokemon command to load data from CSV
python manage.py import_pokemon

# Start server
python manage.py runserver 0.0.0.0:8000

