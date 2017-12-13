# Custom S3 boto storage so we can store static and media in subfolders
# - https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticS3Boto3Storage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaS3Boto3Storage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
