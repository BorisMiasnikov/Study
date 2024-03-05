from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail

urlpatterns = [
    path('', PostsList.as_view()),
    path('<id>', PostDetail.as_view()),
]