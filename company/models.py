from django.db import models
from phone_field import PhoneField
from django.utils import timezone
from party.models import Party_Wholeseller

class Company(models.Model):
    comp_name = models.CharField(verbose_name='Company Name', max_length=20, null=False)
    comp_address = models.CharField(verbose_name='Company Address', max_length=50)
    comp_gst = models.CharField(max_length=35,verbose_name='GST Number', null=False)
    contact = models.CharField(blank=True,max_length = 15,null=False)

    def __str__(self):
        return self.comp_name

class Product(models.Model):
    name = models.CharField(max_length=35, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    scheduled_drug = models.BooleanField(default=False)
    unit_of_packing = models.CharField(max_length=15)    #Unit of packing has units in char e.g. 10*1TAB or 10*10CAP {(Number of Tab in each strip,no.of strips)}
    sale_rate = models.FloatField(null=True)
    gst = models.CharField(null=True,verbose_name="GST",max_length=35)
    free = models.IntegerField(null=True)
    

    def __str__(self):
        return str(self.name)

class Batch(models.Model):
    batch_number = models.CharField(verbose_name='Batch Number', max_length=10, null=False)
    expiry = models.DateField(default=timezone.now,null=False)
    product = models.ForeignKey(Product,on_delete=models.SET_DEFAULT,default=None)
    quantity = models.IntegerField(null=False)
    mrp = models.FloatField(null=False, verbose_name='MRP')
    purchase_rate = models.FloatField(null=True)
    def __str__(self):
        return self.batch_number

