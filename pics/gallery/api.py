from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PictureSerializer
from .models import Picture


class PictureList(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']


class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


    # def put(self, request, *args, **kwargs):
    #     import ipdb; ipdb.set_trace()
    #     # return self.update(request, *args, **kwargs)

