from rest_framework import serializers
from . import models

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ['text',]

class PictureSerializer(serializers.ModelSerializer):
    note = serializers.SerializerMethodField('get_note')

    def get_note(self, picture):
        query_set = models.Note.objects.filter(
            user_id = self.context['request'].user.id,
            picture = picture
        )
        serializer = NoteSerializer(instance = query_set, many = True)
        return serializer.data

    def update(self, *args, **kwargs):

        import ipdb; ipdb.set_trace()

    class Meta:
        model = models.Picture
        fields = ('id', 'note')