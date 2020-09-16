from django.db import models
from django.contrib.auth.models import User

# PhoneField import
# from phone_field import PhoneField



# 1 - Basic, 2 - Intermediate, 3 - Admin (see docs) for better understanding of access_level
access_level = [(1,'Basic'),(2,'Intermediate'),(3,'Admin')]

class user_extended(models.Model):
    access_level = access_level = models.PositiveSmallIntegerField(choices=access_level,default=1,verbose_name="Staff Level",null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100,default="")
    
    # not using phonefield because of limitation of django to validate user in same page {i.e. no forms requires alot of backend}
    mobile = models.CharField(blank=True,max_length = 15,null=False)
    def __str__(self):
        return self.user.get_username()


