from django.forms import ModelForm
from django import forms
from .models import *

class ChequeForm(ModelForm):

    class Meta:
        model = Cheque
        fields = '__all__' 

        widgets = {
            'cheque_num' : forms.TextInput(attrs={'placeholder': 'Cheque Number'}),
            'date_issued' : forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'date_for_assigned' : forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'amount' : forms.NumberInput(attrs={'placeholder': 'Amount'}),
        }