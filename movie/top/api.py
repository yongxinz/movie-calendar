# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

import requests
from rest_framework import viewsets
from rest_framework.decorators import list_route
from django.http import JsonResponse
from rest_framework.response import Response

from .models import Top, Movie, Tag
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

        movie, created = Movie.objects.update_or_create(subject=subject, defaults={'title': title, 'countries': countries, 'genres': genres,
                                                                                   'rating': rating, 'stars': stars, 'year': year,
                                                                                   'directors': directors,
                                                                                   'casts': casts, 'images': images, 'ratings_count': ratings_count,
                                                                                   'summary': summary})
        obj, created = Tag.objects.get_or_create(users=self.request.user, movie=movie)
        res['is_going'] = obj.is_going
        res['is_done'] = obj.is_done

        return JsonResponse(res)

    @list_route(methods=['get'])
    def tag(self, request):
        subject = self.request.query_params.get('subject')
        type = self.request.query_params.get('type')

        movie = Movie.objects.get(subject=subject)
        obj = Tag.objects.get(users=self.request.user, movie=movie)

        if type == 'Go':
            is_going = False if obj.is_going else True
            obj.is_going = is_going
        else:
            is_done = False if obj.is_done else True
            obj.is_done = is_done

        obj.save()

        return Response({'results': {'Go': obj.is_going, 'Done': obj.is_done}})
