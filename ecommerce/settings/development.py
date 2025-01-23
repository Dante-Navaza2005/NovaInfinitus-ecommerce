from .base import *

DEBUG = True

IP_ADDRESS = os.getenv('ip_address')

ALLOWED_HOSTS = [IP_ADDRESS, '127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

MEDIA_URL = '/media/'  # The URL prefix for serving media files (uploaded by users).
