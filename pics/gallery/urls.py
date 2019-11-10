from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'gallery'

urlpatterns = [
    path('', views.pictures_list, name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name = 'account/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
]