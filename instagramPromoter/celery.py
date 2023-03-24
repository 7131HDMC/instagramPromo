import os
from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 
    'instagramPromoter.settings'
)

app = Celery('instagramPromoter')

app.config_from_object('django.conf:settings', namespace='CELERY')
CELERY_BROKER_URL = 'redis://localhost:6379'

app.autodiscover_tasks()