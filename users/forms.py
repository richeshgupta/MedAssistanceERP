from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user_extended


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']

class User_Extended(forms.ModelForm):
    class Meta:
        model = user_extended
        fields = ['access_level','address','mobile']
