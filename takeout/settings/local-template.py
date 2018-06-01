from .base import *
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'udatabase',
        'USER': '{username-changeme}',
        'PASSWORD': '{password-changeme}',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}