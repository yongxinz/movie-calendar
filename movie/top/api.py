# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from rest_framework import viewsets

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', '')
        if id == '':
            count = self.queryset.count()
            random_num = random.randint(1, count)
            queryset = self.queryset.filter(id=random_num)
        else:
            queryset = self.queryset.filter(id=id)

        return queryset
