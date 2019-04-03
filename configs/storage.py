__author__ = 'singo'
__datetime__ = '2019/4/3 11:21 AM '

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