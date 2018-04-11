# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

import requests
from rest_framework import viewsets
from rest_framework.decorators import list_route
from django.http import JsonResponse

from .models import Top, Movie
from .serializers import TopSerializer


class TopViewSet(viewsets.ModelViewSet):
    queryset = Top.objects.all()
    serializer_class = TopSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', '')
        if id == '':
            id_list = self.queryset.filter(casts='').values_list('id')
            count = self.queryset.count()
            random_num = random.randint(1, count)
            while random_num in id_list:
                random_num = random.randint(1, count)
            queryset = self.queryset.filter(id=random_num)
        else:
            queryset = self.queryset.filter(id=id)

        return queryset

    @list_route(methods=['get'])
    def detail(self, request):
        subject = self.request.query_params.get('subject')

        url = 'https://api.douban.com/v2/movie/subject/' + subject
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

        Movie.objects.update_or_create(subject=subject, defaults={'title': title, 'countries': countries, 'genres': genres,
                                                                  'rating': rating, 'stars': stars, 'year': year, 'directors': directors,
                                                                  'casts': casts, 'images': images, 'ratings_count': ratings_count,
                                                                  'summary': summary})

        return JsonResponse(res)
