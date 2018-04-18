# coding=utf-8
from rest_framework.pagination import PageNumberPagination


class YMPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'size'
    max_page_size = 1000


class YMMixin(object):
    def get_queryset(self):
        fields = [f.name for f in self.get_serializer().Meta.model._meta.local_fields]

        queryset = self.queryset
        if self.request.user and 'user' in fields:
            queryset = queryset.filter(user=self.request.user)

        return queryset
