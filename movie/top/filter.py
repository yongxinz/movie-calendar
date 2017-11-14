import django_filters
from .models import Movie


class MovieFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Movie
        fields = ['id', ]
