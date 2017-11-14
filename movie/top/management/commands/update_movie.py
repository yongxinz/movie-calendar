# coding:utf-8

import time
import requests

from django.core.management.base import BaseCommand

from top.models import Movie


class Command(BaseCommand):
    help = 'update movie'

    def handle(self, *args, **options):
        obj = Movie.objects.filter(images=None)
        api = 'https://api.douban.com/v2/movie/subject/'

        for item in obj:
            url = api + item.subject
            response = requests.get(url)
            year = response.json().get('year', '')
            directors_list = response.json().get('directors', '')
            casts_list = response.json().get('casts', '')
            images = response.json().get('images', '').get('large')

            directors = ''
            casts = ''
            for m in directors_list:
                directors += m.get('name', '') + '/'

            for m in casts_list:
                casts += m.get('name', '') + '/'

            print(year, images, directors[0: -1], casts[0: -1])
            time.sleep(2)
