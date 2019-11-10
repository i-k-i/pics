from django.shortcuts import render
from .models import Picture

def pictures_list(request):
    pictures = Picture.objects.all()
    return render(request, 'gallery/pics_list.html', {'pictures': pictures}) 