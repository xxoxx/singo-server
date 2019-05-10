__author__ = 'singo'
__datetime__ = '2019/4/3 2:02 PM '

import os
from .base import BASE_DIR, DEBUG

LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'
FRONT_END_URL = 'http://127.0.0.1:9528'

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
            'format': '%(levelname)s %(asctime)s %(name)s %(module)s %(funcName)s %(lineno)s %(message)s',
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

# LDAP API

LADPAPI = {
    'LDAP_HOST': '172.16.102.18:389',
    'LDAP_USE_SSL': False,
    'LDAP_SEARCH_FILTER': 'uid={uid}',
    'LDAP_BASE_DC': 'dc=ztyc,dc=net',
    'LDAP_BASE_DN': 'ou=people,dc=ztyc,dc=net',
    'LDAP_BIND_USER_DN': 'cn=root,dc=ztyc,dc=net',
    'LDAP_BIND_USER_PASSWORD': 'ztyc1234'
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://:@127.0.0.1:6379/1'
    }
}

SQLAUDIT = {
    'HOST': '172.16.102.31',
    'PORT': 27017,
    'USERNAME': 'dba',
    'PASSWORD': 'dba_123'
}

GITLABS = [
    {
        'URL': 'http://git.ops.com',
        'TOKEN': 'gsdU_1zEq5Cmoq3seGSF'
    }
]

# JENKINS = {
#     # 'URL': 'http://ci.ops.com',
#     # 'USER': 'cainanjie',
#     # 'TOKEN': '119c8e97980559a91210458a8a9e8864f3',
#     'SALT_KEY': '',
#     'URI': 'http://{}:{}@ci.ops.com'.format('cainanjie', '119c8e97980559a91210458a8a9e8864f3')
# }
JENKINS = {
    'URL': 'http://jenkins.it',
    'USER': 'zhoujinliang',
    'TOKEN': '117c911a35acf51e428e29f3ccb363f53f',
    'URI': 'http://{}:{}@jenkins.it'.format('zhoujinliang', '117c911a35acf51e428e29f3ccb363f53f')
}

DEPLOY = {
    'CODE_PATH': '/srv/salt/deploy/',
    'M_MINION': 'devops',   # master下的minion
    'ROLLBACK_SIZE': 5      # jenkins上面保留版本必须大于ROLLBACK_SIZE否则会导致回滚失败
}

DINGTALK_CHATBOT = {
    'URI': 'https://oapi.dingtalk.com/robot/send?access_token=a21a1df49d416fd8cca372a3ce7b3435bd3604f0c1d25779116f96d46bb390b1'
}