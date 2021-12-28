web: cd showminder && ./manage.py migrate && gunicorn --bind 0.0.0.0:8000 --access-logfile - showminder.wsgi:application --threads 5
