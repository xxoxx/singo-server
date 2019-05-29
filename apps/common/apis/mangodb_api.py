__author__ = 'singo'
__datetime__ = '2019/4/17 6:09 PM '

from django.conf import settings
from pymongo import MongoClient

from common.utils import logger

try:
    URI = 'mongodb://{}:{}@{}:{}/'.format(
        settings.SQLAUDIT.get('USERNAME'),
        settings.SQLAUDIT.get('PASSWORD'),
        settings.SQLAUDIT.get('HOST'),
        settings.SQLAUDIT.get('PORT'),
    )
    mongodb_client = MongoClient(URI)
except Exception as e:
    mongodb_client = None
    logger.critical(e)
