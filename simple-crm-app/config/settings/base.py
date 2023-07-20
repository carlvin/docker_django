import os
from pathlib import Path
import dotenv

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# Custom variable to read enviroment variables in development
# READ_DOT_ENV_FILE = env.bool("READ_DOT_ENV_FILE",default=False)
myvariable=os.environ['DJANGO_SETTINGS_MODULE']
print(f'This is running Module: { myvariable }' )

# # Get the value of an environmental variable
DEBUG = os.environ['DEBUG']
SECRET_KEY = os.environ['SECRET_KEY']

# Check if the environmental variable exists and retrieve its value
if SECRET_KEY:
    print(f"The SECRET_KEY is: {SECRET_KEY}")
else:
    print("SECRET_KEY is not set.")



ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]


# Application definition

INSTALLED_APPS = [
    # while in dev(working on appending this)
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'django_htmx',
    'django_htmx_refresh',
    'crispy_forms',
    'crispy_tailwind',

    # Local apps
    'client_relationship_manager',
    'agents',

    
]

# This setting is used by HtmxResponseMiddleware
HTMX_APPS = [
    'crm',
    'agents',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    # 'django_htmx_refresh.middleware.HtmxResponseMiddleware',
    '../../middleware.py.HtmxResponseMiddleware',
]

ROOT_URLCONF = 'config.urls'

# BASE_TEMPLATES_DIR = BASE_DIR / 'templates'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / '../templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#modified to the new config folder
WSGI_APPLICATION = 'config.wsgi.application'

#logging

FORMATTERS = (
    {
        "verbose": {
            "format": "{levelname} {asctime:s} {name} {threadName} {thread:d} {module} {filename} {lineno:d} {name} {funcName} {process:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {asctime:s} {name} {module} {filename} {lineno:d} {funcName} {message}",
            "style": "{",
        },
    },
)


HANDLERS = {
    "console_handler": {
        "class": "logging.StreamHandler",
        "formatter": "simple",
        "level": "DEBUG"
    },
    "info_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f"{BASE_DIR}/logs/data_info.log",
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "verbose",
        "level": "INFO",
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 5,  # 5 MB
    },
    "error_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f"{BASE_DIR}/logs/data_error.log",
        "mode": "a",
        "formatter": "verbose",
        "level": "WARNING",
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 5,  # 5 MB
    },
}

LOGGERS = (
    {
        "django": {
            "handlers": ["console_handler", "info_handler"],
            "level": "INFO",
        },
        "django.request": {
            "handlers": ["error_handler"],
            "level": "INFO",
            "propagate": True,
        },
        "django.template": {
            "handlers": ["error_handler"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.server": {
            "handlers": ["error_handler"],
            "level": "INFO",
            "propagate": True,
        },
    },
)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS[0],
    "handlers": HANDLERS,
    "loggers": LOGGERS[0],
}



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# Modified location based on config folder
STATICFILES_DIRS = [
    BASE_DIR / "../static"
]
MEDIA_URL = '/media/'
MEDIA_ROOT = "media_root"
STATIC_ROOT = "static_root"


AUTH_USER_MODEL = 'client_relationship_manager.User'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL = "/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

#test for development purposes
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.zoho.com"
EMAIL_HOST_USER = "info@carlhub.com"
EMAIL_HOST_PASSWORD = "zp!8lCkv"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "info@carlhub.com"



if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = "DENY"
    
    SECRET_KEY = os.environ['SECRET_KEY']
    
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = env('EMAIL_HOST')
    # EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    # EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    # EMAIL_USE_TLS = env('EMAIL_USE_TLS')
    # EMAIL_PORT = env('EMAIL_PORT')
    # DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
