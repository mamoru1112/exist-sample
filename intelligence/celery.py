import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intelligence.settings')
app = Celery('intelligence')
app.conf.broker_url = 'redis://exist-redis:6379/0'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
