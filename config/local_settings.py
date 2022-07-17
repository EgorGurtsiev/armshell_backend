import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = '7sdfgf59ccfgsd83eeb85604113272asde8938sdfgfsfdg21523'

APPLICATION_ID = os.environ.get('APPLICATION_ID')

DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
