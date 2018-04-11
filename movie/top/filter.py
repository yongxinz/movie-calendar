import django_filters
from .models import Top


class TopFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Top
        fields = ['id', ]
