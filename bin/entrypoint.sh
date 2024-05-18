#!/bin/bash

# Apply database migrations for admin panel
echo "Applying database migrations for admin panel"
python manage.py migrate

# Start Gunicorn server for admin panel
echo "Starting Gunicorn server for admin panel"
exec gunicorn admin_panel.wsgi:application --bind 0.0.0.0:8000 --workers 3