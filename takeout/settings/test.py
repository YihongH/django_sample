from .base import *
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ascending_test',
        'USER': 'meter',
        'PASSWORD': 'password',
        'HOST': 'db-test.ascendingdc.com',
        'PORT': '5432',
    }
}