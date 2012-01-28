# coding: utf-8

from django.conf.urls.defaults import patterns, url, include
from views import Posts, PostsIndex
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('views',
    url(r'^admin/', include(admin.site.urls)),
    # Укажем дополнительный маршрут, чтобы главная страница была доступна без указания номера страницы
    # Отдельный список статей для главной страницы (рейтинг которых выше, либо равен, 10
    url(r'^$', PostsIndex.as_view()),
    url(r'^page(?P<page>\d+)/$', PostsIndex.as_view()),

    # Список всех аткивных статей
    url(r'^posts/$', Posts.as_view()),
    url(r'^posts/page(?P<page>\d+)/$', Posts.as_view())
)
