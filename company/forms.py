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

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Name'}),
            'purchase_SGST': forms.NumberInput(attrs={'placeholder':'Purchase SGST'}),
            'purchase_Rate': forms.NumberInput(attrs={'placeholder':'Purchase Rate'}),
            'unit_of_Packing': forms.TextInput(attrs={'placeholder':'Unit of Packing'}),
            'sale_Rate': forms.NumberInput(attrs={'placeholder':'Sale Rate'}),
            'sale_SGST': forms.NumberInput(attrs={'placeholder':'Sale SGST'}),
            'free': forms.NumberInput(attrs={'placeholder':'Free'}),
            'mrp': forms.NumberInput(attrs={'placeholder':'Maxium Retail Price'}),
        }


class batchForm(ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'

        widgets = {
            'batch_number' : forms.TextInput(attrs={'placeholder':'Batch Number'}),
            'expiry' : forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}),
            'quantity' : forms.NumberInput(attrs={'placeholder':'Quantity'}),
        }