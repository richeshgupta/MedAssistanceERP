from django.db import models
from phone_field import PhoneField
from django.utils import timezone

class Company(models.Model):
    comp_id = models.IntegerField(primary_key=True)
    comp_name = models.CharField(max_length=20, null=False)
    comp_address = models.CharField(max_length=50)
    comp_GST = models.PositiveIntegerField(null=False)
    contact = PhoneField(blank=True, help_text='Company_Number')

    # def __str__(self):
        # return self.comp_name

class Product(models.Model):
    name = models.CharField(max_length=20, null=False)
    comp_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    purchase_rate = models.FloatField(null=False)
    purchase_sgst = models.FloatField(null=False)
    scheduled_drug = models.BooleanField(default=False)
    unit_of_packing = models.PositiveIntegerField()
    sale_rate = models.FloatField(null=False)
    sale_sgst = models.FloatField(null=False)
    free = models.IntegerField(null=False)
    mrp = models.FloatField(null=False)

    # def __str__(self):
    #     return self.name

class Batch(models.Model):
    batch_number = models.PositiveIntegerField()
    expiry = models.DateField(default=timezone.now,null=False)
    product_id = models.OneToOneField(Product,on_delete=models.SET_DEFAULT,default=0)


