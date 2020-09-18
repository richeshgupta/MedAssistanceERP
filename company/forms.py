from django.forms import ModelForm
from django import forms
from .models import *

class companyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

        widgets = {
            'comp_name': forms.TextInput(attrs={'placeholder':'Company Name'}),
            'comp_address': forms.TextInput(attrs={'placeholder':'Company Address'}),
            'comp_GST': forms.NumberInput(attrs={'placeholder':'GST'}),
            'contact': forms.NumberInput(attrs={'placeholder':'Contact'})
        }

class productForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class batchForm(ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'

    widgets = {
        'batch_number' : forms.TextInput(attrs={'placeholder':'Batch Number'}),
        'quantity' : forms.NumberInput(attrs={'placeholder':'Quantity'}),
    }