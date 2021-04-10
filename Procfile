web: gunicorn LMS.wsgi --log-file -
worker: celery -A LMS worker --beat
beat: celery -A LMS beat