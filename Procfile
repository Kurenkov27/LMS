web: gunicorn LMS.wsgi --log-file -
worker: celery -A LMS worker -B --loglevel=info
beat: celery -A LMS beat