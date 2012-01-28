# coding: utf-8
# author: damirazo

from django.views.generic import ListView
from django.views.generic.list import MultipleObjectMixin
from models import Post

class Posts(ListView):
    """
    Список всех доступных статей
    """

    # Нижеуказанные параметры можно также передать данному отображению через метод as_view()
    # url(r'^$', Posts.as_view(context_object_name='posts', template_name='posts.html))
    model = Post
    # Под данным именем наш список статей будет доступен в шаблоне
    context_object_name = 'posts'
    # Название шаблона
    template_name = 'posts.html'
    # Количество объектов на 1 страницу
    paginate_by = 10

    def get_queryset(self):
        qs = Post.objects.filter(is_delete=False).order_by('-created_at')
        if not self.request.user.is_authenticated():
            return qs.exclude(is_private=True)
        return qs

class PostsIndex(Posts):
    """
    Список статей для главной страницы
    """
    template_name = 'index.html'

    def get_queryset(self):
        return super(PostsIndex, self).get_queryset().exclude(rating__lt=10)