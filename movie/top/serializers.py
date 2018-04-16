# coding=utf-8
from rest_framework import serializers

from .models import Top, Tag


class TopSerializer(serializers.ModelSerializer):
    stars = serializers.SerializerMethodField()

    def get_stars(self, obj):
        star_num = obj.stars / 10
        stars = ['no', 'no', 'no', 'no', 'no']
        i = 0

        while i < 5:
            if star_num >= 1:
                stars[i] = 'full'
            elif star_num >= 0.5:
                stars[i] = 'half'

            star_num -= 1
            i += 1

        return stars

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
