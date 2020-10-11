from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from cheque.models import Cheque
from phone_field import PhoneField


class Party_Wholeseller(models.Model):
    name = models.CharField(max_length=20,null=False)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    gstin = models.CharField(null=False,verbose_name="GST Number",max_length=20)
    dl_number = models.CharField(null=False,max_length=10)
    contact = PhoneField(blank=True, help_text='Company_Number')
    pan_number = models.CharField(max_length=11,null=False,unique=True)
    cheque = GenericRelation(Cheque)
    
    def __str__(self):
        return self.name



