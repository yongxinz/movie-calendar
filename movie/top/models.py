# coding=utf-8

from django.db import models

from passport.models import WeixinUsers


class Top(models.Model):
    """
    豆瓣 top250
    """
    subject = models.CharField(u"电影ID", max_length=15)
    title = models.CharField(u"电影中文名", max_length=50, null=True, blank=True)
    link = models.CharField(u"电影地址", max_length=100, null=True, blank=True)
    rating = models.CharField(u"电影评分", max_length=10, null=True, blank=True)
    comment = models.CharField(u"电影评论", max_length=100, null=True, blank=True)
    year = models.CharField(u"电影上映年份", max_length=10, null=True, blank=True)
    directors = models.CharField(u"电影导演", max_length=50, null=True, blank=True)
    casts = models.CharField(u"电影演员", max_length=100, null=True, blank=True)
    images = models.CharField(u"电影海报", max_length=150, null=True, blank=True)
    stars = models.IntegerField(u"电影评星", null=True, blank=True)
    operate_time = models.DateTimeField(u"操作时间", auto_now=True)

    class Meta:
        ordering = ['-id']


class Movie(models.Model):
    """
    电影
    """
    subject = models.CharField(u"电影ID", max_length=15)
    title = models.CharField(u"电影中文名", max_length=50, null=True, blank=True)
    countries = models.CharField(u"上映城市", max_length=20, null=True, blank=True)
    genres = models.CharField(u"电影类型", max_length=20, null=True, blank=True)
    rating = models.CharField(u"电影评分", max_length=10, null=True, blank=True)
    year = models.CharField(u"电影上映年份", max_length=10, null=True, blank=True)
    directors = models.CharField(u"电影导演", max_length=50, null=True, blank=True)
    casts = models.CharField(u"电影演员", max_length=100, null=True, blank=True)
    images = models.CharField(u"电影海报", max_length=150, null=True, blank=True)
    stars = models.IntegerField(u"电影评星", null=True, blank=True)
    ratings_count = models.IntegerField(u"评价人数", null=True, blank=True)
    summary = models.CharField(u"电影简介", max_length=1000, null=True, blank=True)
    operate_time = models.DateTimeField(u"操作时间", auto_now=True)

    class Meta:
        ordering = ['-id']


class Tag(models.Model):
    """
    标记
    """
    user = models.ForeignKey(WeixinUsers, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    is_going = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    operate_time = models.DateTimeField(u"操作时间", auto_now=True)

    class Meta:
        ordering = ['-id']


class InTheaters(models.Model):
    """
    热映电影
    """
    subject = models.CharField(u"电影ID", max_length=15)
    title = models.CharField(u"电影中文名", max_length=50, null=True, blank=True)
    countries = models.CharField(u"上映城市", max_length=20, null=True, blank=True)
    genres = models.CharField(u"电影类型", max_length=20, null=True, blank=True)
    rating = models.CharField(u"电影评分", max_length=10, null=True, blank=True)
    year = models.CharField(u"电影上映年份", max_length=10, null=True, blank=True)
    directors = models.CharField(u"电影导演", max_length=50, null=True, blank=True)
    casts = models.CharField(u"电影演员", max_length=100, null=True, blank=True)
    images = models.CharField(u"电影海报", max_length=150, null=True, blank=True)
    stars = models.IntegerField(u"电影评星", null=True, blank=True)
    ratings_count = models.IntegerField(u"评价人数", null=True, blank=True)
    summary = models.CharField(u"电影简介", max_length=1000, null=True, blank=True)
    operate_time = models.DateTimeField(u"操作时间", auto_now=True)

    class Meta:
        ordering = ['id']
