import os

from celery import Celery

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings')

app = Celery('lms')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task': '../academy.tasks.clear_log',
    # 'schedule': crontab(hour=0, minute=0),
    'schedule': 3
}
