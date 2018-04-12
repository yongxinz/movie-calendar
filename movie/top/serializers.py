# coding=utf-8
from rest_framework import serializers

from .models import Top, Tag


class TopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Top
        exclude = ('operate_time', )


class TagSerializer(serializers.ModelSerializer):
    subject = serializers.ReadOnlyField(source='movie.subject')
    title = serializers.ReadOnlyField(source='movie.title')
    genres = serializers.ReadOnlyField(source='movie.genres')
    rating = serializers.ReadOnlyField(source='movie.rating')
    year = serializers.ReadOnlyField(source='movie.year')
    directors = serializers.ReadOnlyField(source='movie.directors')
    images = serializers.ReadOnlyField(source='movie.images')

    class Meta:
        model = Tag
        exclude = ('operate_time', 'is_going', 'is_done')
