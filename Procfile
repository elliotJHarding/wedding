release: python manage.py migrate
web: gunicorn --env DJANGO_SETTINGS_MODULE=wedding.settings --log-level debug wedding.wsgi

