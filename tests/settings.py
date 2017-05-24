from django.utils.crypto import get_random_string

SECRET_KEY = get_random_string(length=50)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'glitter',
    'glitter.assets',
    'glitter.reminders',
    'glitter_documents',
    'taggit',
]

USE_TZ = True


APPEND_SLASH = True


STATIC_URL = '/static/'
