# coding=utf-8
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ('operate_time', )
