from rest_framework import serializers
from . import models

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ['text',]

class PictureSerializer(serializers.ModelSerializer):
    note = serializers.SerializerMethodField('get_note')
    user = serializers.StringRelatedField()

    def get_note(self, picture):
        query_set = models.Note.objects.filter(
            user_id = self.context['request'].user.id,
            picture = picture
        ).last()
        serializer = NoteSerializer(instance = query_set)
        return serializer.data

    class Meta:
        model = models.Picture
        fields = ('id', 'image_path', 'note', 'user', 'title')