#!/usr/bin/env python
# coding=utf-8

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie',
        'USER': 'movie_dev',
        'PASSWORD': '123456',
        'HOST': 'mysql',
        'PORT': '3306',
        'CONN_MAX_AGE': 300,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'read_default_file': '/etc/my.cnf',
            'charset': 'utf8',
        }
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
