#!/usr/bin/env python
# coding=utf-8

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'movie',
    }
}

INSTALLED_APPS += [
    'rest_framework',
]

WEIXIN = {
    'url': 'https://api.weixin.qq.com',
    'id': 'your appid',
    'key': 'your appsecret',
}
