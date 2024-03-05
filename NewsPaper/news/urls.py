from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostsSearch

urlpatterns = [
    path('', PostsList.as_view(), name= 'Posts_list'),
    path('<id>', PostDetail.as_view(), name= 'Post_detail'),
    path('search/', PostsSearch.as_view(), name= 'Post_search'),
]