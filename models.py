# coding: utf-8
# author: damirazo

from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

class Post(models.Model):
    author = models.ForeignKey(to=User, verbose_name=u'Автор')
    name = models.CharField(max_length=128, verbose_name=u'Название')
    text = models.TextField(verbose_name=u'Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата публикации')
    rating = models.IntegerField(default=0, verbose_name=u'Рейтинг')
    is_private = models.BooleanField(default=False, verbose_name=u'Приватная статья?')
    is_delete = models.BooleanField(default=False, verbose_name=u'Удаленная статья?')

    def __unicode__(self):
        return self.name

    class Meta(object):
        db_table = 'habraposts'
        ordering = ['-created_at',]

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at')
admin.site.register(Post, PostAdmin)