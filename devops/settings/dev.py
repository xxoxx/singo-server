__author__ = 'singo'
__datetime__ = '2019/4/3 2:02 PM '

import os
from .base import BASE_DIR, DEBUG

LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devops2',
        'USER': 'devops',
        'PASSWORD': 'lemon1912',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
              'init_command': "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES';SET foreign_key_checks = 0;",
          }
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'detail': {
            # 'format': '{"levelname":"%(levelname)s","asctime":"%(asctime)s","module":"%(name)s","fullpath":"%(pathname)s","funcName":"%(funcName)s","lineno":"%(lineno)s","message":"%(message)s"}',
            'format': '%(levelname)s %(asctime)s %(name)s %(pathname)s %(funcName)s  %(lineno)s  %(message)s',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler'
        },
        'db_backends': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'db_backends.log'),
            'formatter': 'detail'
        },
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'detail'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
            'filename': os.path.join(BASE_DIR, 'logs', 'devops.log'),
            'formatter': 'detail'
        },
        'django_server': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django_server.log'),
            'formatter': 'detail'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False
        },
        "django.server": {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            "propagate": False
        },
        'django.request':{
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.db.backends': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False
        },
        'devops':{
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}


# Salt API

SALTAPI = {
    'URL': 'https://127.0.0.1:5120',
    'USERNAME': 'saltapi',
    'PASSWORD': 'saltapi'
}

# OA API

OAAPI = {
    'URL': 'http://oa.ztocwst.com:8000/seeyon/rest/',
    'USERNAME': 'rest',
    'PASSWORD': 'Lemon1912'
}