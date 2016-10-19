# coding=utf-8
from __future__ import unicode_literals

from DjangoUeditor.models import UEditorField
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']  # 排序


class Article(models.Model):
    column = models.ForeignKey(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    # author = models.ForeignKey(User, blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容')
    sort_rank = models.IntegerField('排序', default=100)

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
        ordering = ['sort_rank', '-update_time']  # 排序
