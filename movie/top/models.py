# coding=utf-8

from django.db import models


class Top(models.Model):
    """
    电影
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
