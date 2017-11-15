import os
from celery import Celery 
from django.conf import settings


#set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'media_hub.settings')

app = Celery('media_hub')

app.config_from_object('django.conf:settings')
app.autodiscover_task(lambda: settings.INSTALLED_APPS)