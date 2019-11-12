from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return 'images/users/{0}/{1}'.format(instance.user_id, filename)

class Picture(models.Model):
    title = models.CharField(max_length=256)
    uploaded = models.DateTimeField(auto_now_add=True)
    image_path = models.ImageField(upload_to=upload_to)    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_pictures' )

    def __str__(self):
        return  self.title or self.image_path


    # def save(self, *args, **kwargs):
    #     import ipdb; ipdb.set_trace()

class Note(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='created_notes')
    picture = models.ForeignKey(Picture, on_delete = models.CASCADE, related_name='notes')
    text = models.TextField()
    ctime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'picture')


    def __str__(self):
        return '{0}:{1}:{2}'.format(self.user_id, self.picture_id, self.text[:57])