from rest_framework import serializers
from . import models

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        # fields = ['id', 'image']
        fields = '__all__'


