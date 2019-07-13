# coding:utf-8

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from top.models import InTheaters, Movie


class Command(BaseCommand):
    help = 'in_theaters'

    def handle(self, *args, **options):
        InTheaters.objects.all().delete()

        url = settings.DOUBAN_API + '/v2/movie/in_theaters'
        response = requests.get(url).json()
        subjects = response.get('subjects', [])

        for item in subjects:
            subject = item['id']

            url = settings.DOUBAN_API + '/v2/movie/subject/' + subject
            res = requests.get(url).json()

            title = res['title']
            countries = ','.join(res['countries'])
            genres = ','.join(res['genres'])
            rating = res['rating']['average']
            stars = res['rating']['stars']
            year = res['year']
            directors = ','.join([m['name'] for m in res['directors']])
            casts = ','.join([m['name'] for m in res['casts']])
            images = res['images']['medium']
            ratings_count = res['ratings_count']
            summary = res['summary']

            print(subject, title, countries, genres, rating, stars, year, directors, casts, images, ratings_count, summary)
            InTheaters.objects.create(subject=subject, title=title, countries=countries, genres=genres, rating=rating, stars=stars, year=year,
                                      directors=directors, casts=casts, images=images, ratings_count=ratings_count, summary=summary)

            Movie.objects.update_or_create(subject=subject, defaults={'title': title, 'countries': countries, 'genres': genres,
                                                                      'rating': rating, 'stars': stars, 'year': year, 'directors': directors,
                                                                      'casts': casts, 'images': images, 'ratings_count': ratings_count,
                                                                      'summary': summary})
