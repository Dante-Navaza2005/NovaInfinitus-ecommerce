from .base import *
import dj_database_url


load_dotenv()

DEBUG = True


ALLOWED_HOSTS = [
    'novainfinitus.up.railway.app',
    'novainfinitus.com',
    'https://www.mercadopago.com.br/checkout/v1/payment/redirect/',
]

CSRF_TRUSTED_ORIGINS = [
    'https://novainfinitus.up.railway.app',
    'https://novainfinitus.com',
    'https://www.mercadopago.com.br/checkout/v1/payment/redirect/',
]

INSTALLED_APPS += ['cloudinary_storage', 'cloudinary']

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dvc64z04k',
    'API_KEY': os.getenv('CLOUD_API_KEY'),
    'API_SECRET': os.getenv('CLOUD_API_SECRET'),
}

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'

MEDIA_URL = '/ecommerce/media/'  # The URL prefix for serving media files (uploaded by users).

# Compress and cache static files for better performance
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_HSTS_SECONDS = 31536000  # Ajuste o valor conforme necessário
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Para incluir subdomínios
SECURE_HSTS_PRELOAD = True  # Para pré-carregar a configuração nos navegadores

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

