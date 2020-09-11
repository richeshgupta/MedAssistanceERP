from django.forms import ModelForm
from django import forms
from .models import *

class ChequeForm(ModelForm):
    # cheque_num = forms.CharField(widget=forms.NumberInput(), required=True, max_length=20)
    # bank = forms.CharField(widget=forms.TextInput(), required=True, max_length=35)
    # date_issued = forms.DateField(widget=forms.DateInput(), required=True)
    # date_assigned = forms.DateField(widget=forms.DateInput(), required=True)
    # amount = forms.FloatField(required=True)

    class Meta():
        model = Cheque
        fields = '__all__' 