# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'djangoexample.custmiddle.DisableCSRF',
)

ROOT_URLCONF = 'djangoexample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'djangoexample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

mysql_host="127.0.0.1"
mysql_port=3306
mysql_user="root"
mysql_pwd=""
mysql_name="djangoexample"

redis_host='127.0.0.1'
redis_port=2277
redis_db=0

OPTIONS = {'charset':'utf8mb4'}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': mysql_name,
        'USER': mysql_user,
        'PASSWORD': mysql_pwd,
        'HOST': mysql_host,
        'PORT': mysql_port,
        'OPTIONS': OPTIONS,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

DEFAULT_CHARSET="UTF-8"

LOCALES = (
    ('en', u'English'),
    ('zh-hans', u'简体中文'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


###########custom

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
            'datefmt' : "%Y/%m/%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'file': {
            #出错日志
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/u01/logs/djangoexample.error.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 20,  # 20 mb
        },
        'celery': {
            #celery日志
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/u01/logs/djangoexample.celery.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 20,  # 20 mb
        },
        'crontab': {
            #crontab日志
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/u01/logs/djangoexample.crontab.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 20,  # 20 mb
        },
        'comm': {
            #普通打印信息用的日志
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/u01/logs/djangoexample.comm.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 20,  # 100 mb
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['null',],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers':['file','mail_admins'],
            'level':'ERROR',
            'propagate': False,
        },
        'django_crontab.crontab': {
            'handlers':['file','mail_admins'],
            'level':'WARNING',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery', 'mail_admins'],
            'level': 'DEBUG',
        },
        'crontab': {
            'handlers': ['crontab', ],
            'level': 'DEBUG',
        },
        'comm': {
            'handlers': ['comm', ],
            'level': 'DEBUG',
        },
    }
}

import logging
log_comm    = logging.getLogger('comm')
log_crontab = logging.getLogger('crontab')
log_celery  = logging.getLogger('celery')


#Celery Broker
BROKER_URL = 'redis://%s:%d/1' % ( redis_host, redis_port )
CELERY_RESULT_BACKEND = 'redis://%s:%d/1' % ( redis_host, redis_port)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

#Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:%d/%d" % (redis_host, redis_port , redis_db),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        #'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DATETIME_FORMAT':'%Y-%m-%d %H:%M:%S',
}
