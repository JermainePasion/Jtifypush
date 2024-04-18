web: gunicorn Jtify.wsgi
worker: celery -A backend worker -l info
beat: celer -A backend beat -l INFO