from settings.base import *

DEBUG = True 

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ['127.0.0.1','http://ec38397f.ngrok.io/']

# PayPal Settings
RESOURCES_DIR = 'media/product_videos/'
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'https://d8d947ba.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'maaisiexx-facilitator@hotmail.co.uk'
PAYPAL_TEST = True