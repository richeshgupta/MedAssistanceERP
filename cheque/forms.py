from django.forms import ModelForm
from django import forms
from .models import *

class ChequeForm(ModelForm):
    class Meta:
        model = Cheque
        fields = '__all__' 