import os

DEBUG = True

ALLOWED_HOSTS = ['*', ]

# DATABASE INFO
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydisplay.sqlite3',
        'HOST': 'localhost',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATIC_ROOT = 'static/'
