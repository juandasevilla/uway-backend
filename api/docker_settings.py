import os
from .settings import *

# Base de datos para Docker
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'uway_db'),
        'USER': os.environ.get('POSTGRES_USER', 'uway_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'uway_password'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Configuración para Docker
ALLOWED_HOSTS = ['*']  # En producción, especifica dominios específicos
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

# Archivos estáticos
STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/media/'
MEDIA_URL = '/media/'
