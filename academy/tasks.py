from celery import shared_task, app

#from LMS.celery import app
from logger.models import LogRecord

@shared_task
def clear_log():
    print('clear_log worked!')
    LogRecord.objects.delete()
