from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .models import Post
from .forms import PostForm


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
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context




class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_field = 'N'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('Posts_list')


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_field = 'A'
        return super().form_valid(form)


class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('Posts_list')

