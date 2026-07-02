import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



app.conf.beat_schedule = {
    'task-every-3-minutes-40-seconds': {
        'task': 'task_manager.tasks.add',
        'schedule': timedelta(minutes=3, seconds=40),
    },
    'task-3-evening': {
        'task': 'task_manager.tasks.mul',
        'schedule': crontab(minute=0, hour='19-21'),
    },
    'task-sunrise': {
        'task': 'task_manager.tasks.add',
        'schedule': 'sunrise',
    }
}
