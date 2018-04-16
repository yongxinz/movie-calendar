# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Top, Movie, Tag
from .serializers import TopSerializer, TagSerializer
from .filter import TagFilter
from tools.rest_helper import YMMixin


class TopViewSet(viewsets.ModelViewSet):
    queryset = Top.objects.all()
    serializer_class = TopSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', '')
        if id == '':
            queryset = self.queryset.order_by('?')[0:1]
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
        obj, created = Tag.objects.get_or_create(user=self.request.user, movie=movie)
        res['is_going'] = obj.is_going
        res['is_done'] = obj.is_done

        return JsonResponse(res)

    @list_route(methods=['get'])
    def tag(self, request):
        subject = self.request.query_params.get('subject')
        type = self.request.query_params.get('type')

        movie = Movie.objects.get(subject=subject)
        obj = Tag.objects.get(user=self.request.user, movie=movie)

        if type == 'Go':
            is_going = False if obj.is_going else True
            obj.is_going = is_going
        else:
            is_done = False if obj.is_done else True
            obj.is_done = is_done

        if obj.is_done:
            obj.is_going = False

        obj.save()

        return Response({'results': {'Go': obj.is_going, 'Done': obj.is_done}})


class TagViewSet(YMMixin, viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_class = TagFilter
