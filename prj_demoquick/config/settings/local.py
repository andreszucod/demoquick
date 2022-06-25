from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
#STATIC_ROOT = [BASE_DIR.child('static')]

# En base.py se definio el directorio base BASE_DIR por lo que se hace referencia a este
STATICFILES_DIRS = [BASE_DIR.child('static'),]

# definir la localizacion de los archivos media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')