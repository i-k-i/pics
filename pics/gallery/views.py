from django.shortcuts import render, redirect
from .models import Picture
from .forms import UserRegistrationForm
from django.contrib.auth import login


def pictures_list(request):
    pictures = Picture.objects.all()
    return render(request, 'gallery/gallery.html', {'pictures': pictures}) 

def send_gallery_to_email(request):
    pass

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('gallery:home')
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})




