from django.urls import path
from . import api


picture_list = api.PictureViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

picture_detail = api.PictureViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    # path('pictures/list', api.PictureList.as_view(), name  = 'api_pics_list'),
    # path('pictures/<int:pk>/', api.PictureDetail.as_view(), name  = 'api_pics'),

    path('pictures/', picture_list, name  = 'pics_list'),
    path('pictures/<int:pk>/', picture_detail, name  = 'pics_details'),


]
