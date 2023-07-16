from .base import *
DEBUG = True

SECRET_KEY="django-insecure-h*wprd2xbt#!jq#rrkr_ww2h(md#=bm&a0ok4h!tp(081%+6)6"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME','carlhubdb'),
        'USER': os.getenv('DB_USER','carlhub'),
        'PASSWORD': os.getenv('DB_PASS','1234'),
        'HOST': os.getenv('DB_HOST','localhost'),
        'PORT':os.getenv('DB_PORT','5432'),
    }
}
