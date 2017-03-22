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
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'glitter',
    'glitter.assets',
    'glitter.blocks.banner',
    'glitter.blocks.form',
    'glitter.blocks.html',
    'glitter.blocks.image',
    'glitter.blocks.redactor',
    'glitter.blocks.related_pages',
    'glitter.pages',
    'glitter.reminders',
    'glitter.tests.sample',
    'glitter.tests.sampleblocks',
    'glitter_documents',
    'mptt',
    'sorl.thumbnail',
    'taggit',
]

USE_TZ = True


APPEND_SLASH = True


STATIC_URL = '/static/'
