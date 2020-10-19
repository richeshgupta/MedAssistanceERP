from django.db import models

# Create your models here.
class Profile_Retailer(models.Model):
    Shop_Name = models.CharField(max_length=45,null=False)
    Address = models.CharField(max_length=50,null=False,verbose_name="Address")
    GST = models.CharField(max_length=20,verbose_name="GST")
    contact = models.CharField(max_length=12,verbose_name="Contact number")
    DL_no = models.CharField(max_length=20,verbose_name="DL Number")
    
