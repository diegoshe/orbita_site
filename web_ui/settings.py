import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import logging, json
import logging.config
from pythonjsonlogger import jsonlogger


with open('webui/logging.json', 'rt') as f:
            config = json.load(f)
logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


sentry_sdk.init(
    dsn="http://f7f43becb89d4028a62de9c6efc88e8c@127.0.0.1:8080/1",
    integrations=[DjangoIntegration()],
    send_default_pii=True
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'ozjvkcp2(tg)bzgahcuq^xm+5f&0j-e9$5uwc+$zmm$%t-8d!+'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0',"31.131.28.206", "web-api"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webui',
]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'winorbita@gmail.com'
EMAIL_HOST_PASSWORD = '+sh52!fiv'
DEFAULT_MAIL_NAME = "winorbita"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'deploy_static')

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "deployment", "media")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

