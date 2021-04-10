web: gunicorn LMS.wsgi --log-file -
worker: celery -A LMS.celery worker -B --loglevel=info
beat: celery -A LMS.celery beat