from .base import *
load_dotenv()


DEBUG = True

ADDRESS_IP = os.getenv('ADDRESS_IP')

ALLOWED_HOSTS = [ADDRESS_IP, '127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

MEDIA_URL = '/media/'  # The URL prefix for serving media files (uploaded by users).
