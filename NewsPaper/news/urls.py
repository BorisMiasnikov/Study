from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostsSearch, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate, \
    ArticlesUpdate, ArticlesDelete

urlpatterns = [
    path('', PostsList.as_view(), name= 'Posts_list'),
    path('<int:pk>/', PostDetail.as_view(), name= 'Post_detail'),
    path('search/', PostsSearch.as_view(), name= 'Posts_search'),
    path('news/create/', NewsCreate.as_view(), name='News_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='News_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='News_delete'),
    path('articles/create/', ArticlesCreate.as_view(), name='Articles_create'),
    path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='Articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='Articles_delete'),
]