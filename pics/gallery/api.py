from rest_framework import generics, viewsets, permissions 
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PictureSerializer
from .models import Picture
from .permissions import IsOwnerOrReadOnly

# class PictureList(generics.ListAPIView):
#     queryset = Picture.objects.all()
#     serializer_class = PictureSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['user']
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Picture.objects.all()
#     serializer_class = PictureSerializer

#using viewset
class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        import ipdb; ipdb.set_trace()
        serializer.save(user=self.request.user)
