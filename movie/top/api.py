# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

import requests
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

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
        res = requests.get(url)

        return JsonResponse(res.json())
