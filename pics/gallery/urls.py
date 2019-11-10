from django.urls import path
from . import views, api
from django.contrib.auth import views as auth_views

app_name = 'gallery'

urlpatterns = [
    path('', views.pictures_list, name = 'home'),

    path('login/', auth_views.LoginView.as_view(template_name = 'account/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('register/', views.register, name = 'register'),

    path('send_gallery/', views.send_gallery_to_email, name = 'send_gallery'),

    path('api/pictures/list', api.PictureList.as_view()),
    path('api/pictures/<int:pk>/', api.PictureDetail.as_view()),
]