from base import *

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

# PayPal Settings
RESOURCES_DIR = 'media/product_videos/'
SITE_URL = 'http://wayv-videos.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'http://wayv-videos.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL = 'maaisiexx-facilitator@hotmail.co.uk'
PAYPAL_TEST = True
