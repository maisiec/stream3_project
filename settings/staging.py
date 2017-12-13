from base import *
import os
import dj_database_url

DEBUG = False 

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


INSTALLED_APPS += ['storages', ]

# Load the ClearDB connection details from the environment variable
DATABASES['default'] =  dj_database_url.config()

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://d8d947ba.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'maaisiexx-facilitator@hotmail.co.uk'
 
SITE_URL = 'http://wayv-videos.herokuapp.com/'
ALLOWED_HOSTS = ('wayv-videos.herokuapp.com',)
 
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

# Amazon S3
# - https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
# - http://django-storages.readthedocs.io/
# - https://github.com/boto/boto

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = "wayv-production"
AWS_AUTO_CREATE_BUCKET = False
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATICFILES_LOCATION = 'static'
#STATICFILES_STORAGE = 'media_hub.storages.StaticS3Boto3Storage'
#STATIC_URL = "https://{0}/{1}/".format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


# Media files
#

#MEDIAFILES_LOCATION = 'media'
#MEDIA_URL = "https://{0}/{1}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
#DEFAULT_FILE_STORAGE = 'media_hub.storages.MediaS3Boto3Storage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'maaisiexx@gmail.com'
EMAIL_HOST_PASSWORD = 'qpwoeiruTY1'
EMAIL_PORT = 587
EMAIL_USE_TLS = True