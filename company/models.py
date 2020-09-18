from django.db import models
from phone_field import PhoneField
from django.utils import timezone
from party.models import Party_Wholeseller

class Company(models.Model):
    comp_name = models.CharField(verbose_name='Company Name', max_length=20, null=False)
    comp_address = models.CharField(verbose_name='Company Address', max_length=50)
    comp_GST = models.PositiveIntegerField(verbose_name='GST', null=False)
    contact = models.CharField(blank=True,max_length = 15,null=False)

    def __str__(self):
        return self.comp_name

class Product(models.Model):
    name = models.CharField(max_length=35, null=False)
    comp = models.ForeignKey(Company, on_delete=models.CASCADE)
    purchase_rate = models.FloatField(null=True)
    purchase_sgst = models.FloatField(null=True)
    scheduled_drug = models.BooleanField(default=False)
    unit_of_packing = models.CharField(max_length=15)    #Unit of packing has units in char e.g. 10*1TAB or 10*10CAP {(Number of Tab in each strip,no.of strips)}
    sale_rate = models.FloatField(null=True)
    sale_sgst = models.FloatField(null=True)
    free = models.IntegerField(null=True)
    mrp = models.FloatField(null=False)
    party_wholeseller = models.ForeignKey(Party_Wholeseller, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.id)

class Batch(models.Model):
    batch_number = models.CharField(max_length=10)
    expiry = models.DateField(default=timezone.now,null=False)
    product_id = models.ForeignKey(Product,on_delete=models.SET_DEFAULT,default=0)
    quantity = models.IntegerField(null=False)
    def __str__(self):
        return self.batch_number

