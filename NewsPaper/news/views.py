from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .filters import PostFilter
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-data_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostsSearch(ListView):
    model = Post
    ordering = '-data_in'
    template_name = 'posts_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context




class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    # pk_url_kwarg = 'pk'
