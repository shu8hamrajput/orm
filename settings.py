from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-g6ie!a$=sg7gwn&zglmtchuu#om8)rzn6j%1c@8wa%d5nk+=6&'

DEBUG = True

INSTALLED_APPS = ['orm']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
