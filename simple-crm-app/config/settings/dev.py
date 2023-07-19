from .base import *
DEBUG = True

SECRET_KEY="django-insecure-h*wprd2xbt#!jq#rrkr_ww2h(md#=bm&a0ok4h!tp(081%+6)6"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.getenv('DB_HOST'),
        'PORT':"",
    }
}
