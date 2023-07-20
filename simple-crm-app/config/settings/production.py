from .base import *
  
DEBUG = False

CSRF_TRUSTED_ORIGINS = ['https://*.carlhub.com','https://*.127.0.0.1']

INTERNAL_IPS = ['127.0.0.1',]

ALLOWED_HOSTS = ['carlhub.com','localhost','www.carlhub.com','127.0.0.1']
SECRET_KEY = os.getenv('SECRET_KEY')

SITE_ID = 1
MEDIA_ROOT = "/home/media"
STATIC_ROOT = "/home/static"

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.getenv('DB_HOST'),
        'PORT':"",
     }
}


