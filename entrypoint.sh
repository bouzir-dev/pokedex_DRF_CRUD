#!/bin/sh

# Load environment variables
export $(cat .env | xargs)

# Apply database migrations
python manage.py migrate

# Run import pokemon command to load data from CSV
python manage.py import_pokemon

# Check if superuser exists
echo "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())" | python manage.py shell | grep -q False
if [ $? -eq 0 ]; then
  # Create superuser
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')" | python manage.py shell
fi

#Run tests
python manage.py test

# Start server
python manage.py runserver 0.0.0.0:8000


