from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_Retailer
        fields=['Shop_Name','Address','GST','contact','DL_no']