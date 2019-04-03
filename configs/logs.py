__author__ = 'singo'
__datetime__ = '2019/4/3 10:20 AM '

import os
from .base import DEBUG, BASE_DIR

if DEBUG:
    LOG_LEVEL = 'DEBUG'
else:
    LOG_LEVEL = 'INFO'
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