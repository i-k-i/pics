from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PictureSerializer
from .models import Picture


class PictureList(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

