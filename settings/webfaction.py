from __future__ import absolute_import
from .base import *

# Configure these however you like for local development.
# Don't forget to configure a database!

DEBUG=False
TEMPLATE_DEBUG=DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'crazyweber_mbd',       # Or path to database file if using sqlite3.
        'USER': 'crazyweber_mbd',                  # Not used with sqlite3.
        'PASSWORD': '4334803c',             # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}