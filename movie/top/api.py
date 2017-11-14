# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from .models import Movie
from .serializers import MovieSerializer
from .filter import MovieFilter


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_class = MovieFilter

