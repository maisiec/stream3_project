from base import *

DEBUG = False 

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'http://ec38397f.ngrok.io//a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'maaisiexx-facilitator@hotmail.co.uk'
 
SITE_URL = 'http://wayv-videos.herokuapp.com/'
ALLOWED_HOSTS.append('wayv-videos.herokuapp.com/')
 
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'maaisiexx@gmail.com'
EMAIL_HOST_PASSWORD = 'qpwoeiruTY1'
EMAIL_PORT = 587
EMAIL_USE_TLS = True