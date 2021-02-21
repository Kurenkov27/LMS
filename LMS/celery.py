import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings')

app = Celery('LMS')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'clear-log': {
        'task': 'academy.tasks.clear_log',
        'schedule': 10.0,
    # 'schedule': crontab(hour=0, minute=0),
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

