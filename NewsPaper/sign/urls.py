from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
# from .views import BaseRegisterView

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name= 'logout.html'), name= 'logout'),
    path('logout_confirm/', TemplateView.as_view(template_name='logout_confirm.html'), name='logout_confirm'),
    # path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),

]