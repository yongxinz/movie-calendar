#!/usr/bin/env python
# coding=utf-8

from .settings import *
from os.path import join, abspath, dirname

# make root path
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

DEBUG = False

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-hans'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'movie.naturez.cn'
]

INTERNAL_IPS = ['127.0.0.1', 'movie.naturez.cn']
INSTALLED_APPS += [
    'top',
    'passport'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('tools.auth.YMAuthentication',),
    'DEFAULT_PAGINATION_CLASS': 'tools.rest_helper.YMPagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}
