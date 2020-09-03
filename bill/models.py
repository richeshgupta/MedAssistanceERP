from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from party.models import Party_Retailer

payment = [(1,'Cash'),(2,'Credit')]

class Bill_Retailer(models.Model):
    date = models.DateField(default=timezone.now,null=False)
    customer_name= models.CharField(max_length=20,null=False)
    customer_email = models.EmailField(max_length=254)
    mode_of_payment = models.PositiveSmallIntegerField(choices=payment,default=1)
    total_bill = models.FloatField(null=False)
    name = ArrayField(models.CharField(max_length=35, null=False))
    batch_number = ArrayField(models.CharField(max_length=10))
    quantity = ArrayField(models.IntegerField(null=False))
    discount = ArrayField(models.FloatField(default=0))
    deal = ArrayField(models.IntegerField(default=0))
    tax = ArrayField(models.FloatField(default=0))
    loss = ArrayField(models.BooleanField(default=False))
    sale_rate = ArrayField(models.FloatField(null=True))

class Bill_Wholeseller(models.Model):
    date = models.DateField(default=timezone.now,null=False)
    customer = models.ForeignKey(Party_Retailer, on_delete=models.PROTECT) 
    mode_of_payment = models.PositiveSmallIntegerField(choices=payment,default=1)
    total_bill = models.FloatField(null=False)
    name = ArrayField(models.CharField(max_length=35, null=False))
    batch_number = ArrayField(models.CharField(max_length=10))
    quantity = ArrayField(models.IntegerField(null=False))
    discount = ArrayField(models.FloatField(default=0))
    deal = ArrayField(models.IntegerField(default=0))
    tax = ArrayField(models.FloatField(default=0))
    loss = ArrayField(models.BooleanField(default=False))
    sale_rate = ArrayField(models.FloatField(null=True))

class Purchase(models.Model):
    date = models.DateField(default=timezone.now,null=False)
    mode_of_payment = models.PositiveSmallIntegerField(choices=payment,default=1)
    total_bill = models.FloatField(null=False)
    name = ArrayField(models.CharField(max_length=35, null=False))
    batch_number = ArrayField(models.CharField(max_length=10))
    quantity = ArrayField(models.IntegerField(null=False))
    discount = ArrayField(models.FloatField(default=0))
    deal = ArrayField(models.IntegerField(default=0))
    tax = ArrayField(models.FloatField(default=0))
    loss = ArrayField(models.BooleanField(default=False))
    sale_rate = ArrayField(models.FloatField(null=True))
    
