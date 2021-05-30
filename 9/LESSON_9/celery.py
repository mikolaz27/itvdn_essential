import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LESSON_9.settings')

app = Celery('itvdn')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


