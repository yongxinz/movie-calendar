# coding=utf-8

from django.test import TestCase, RequestFactory, Client

from django.test import tag

from rest_framework.test import APIClient

from rest_framework.test import force_authenticate

from django.contrib.auth.models import User, AnonymousUser
import datetime
from decimal import Decimal


class YMTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="2fce6d7d-50ed-11e7-a71f-4c32758a6411")
