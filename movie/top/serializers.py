# coding=utf-8
from rest_framework import serializers

from .models import Top


class TopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Top
        exclude = ('operate_time', )
