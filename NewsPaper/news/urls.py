from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostsSearch, NewsCreate, PostUpdate, PostDelete, ArticlesCreate, \
    CategoriesPostList, subscribe

urlpatterns = [
    path('', PostsList.as_view(), name= 'Posts_list'),
    path('<int:pk>/', PostDetail.as_view(), name= 'Post_detail'),
    path('search/', PostsSearch.as_view(), name= 'Posts_search'),
    path('news/create/', NewsCreate.as_view(), name='News_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='News_edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='News_delete'),
    path('articles/create/', ArticlesCreate.as_view(), name='Articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='Articles_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='Articles_delete'),
    path('categories/<int:pk>/', CategoriesPostList.as_view(), name='Category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='Subscribe'),
]