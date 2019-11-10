from django import forms
from django.contrib.auth.models import User 

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')
    
    def clean_password2(self):
        cdata = self.cleaned_data
        if cdata['password'] != cdata['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cdata['password']