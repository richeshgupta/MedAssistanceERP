from django.db import models
from phone_field import PhoneField

class Party_Wholeseller(models.Model):
    name = models.CharField(max_length=20,null=False)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    gstin = models.IntegerField(null=False)
    dl_number = models.IntegerField(null=False)
    contact = PhoneField(blank=True, help_text='Company_Number')
    pan_number = models.CharField(max_length=11,null=False)

    # def __str__(self):
    #     return self.name

class Party_Retailer(models.Model):
    name = models.CharField(max_length=20,null=False)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    contact = PhoneField(blank=True, help_text='Company_Number')
    doctor = models.CharField(max_length=20,null=False)

    # def __str__(self):
        # return self.name


