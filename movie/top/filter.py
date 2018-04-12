import django_filters

from .models import Top, Tag


class TopFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Top
        fields = ['id', ]


class TagFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Tag
        fields = ['is_going', 'is_done']
