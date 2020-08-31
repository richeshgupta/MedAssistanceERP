from django.db import models
from django.contrib.auth.models import User

# PhoneField import
from phone_field import PhoneField



# 1 - Basic, 2 - Intermediate, 3 - Admin (see docs) for better understanding of access_level
access_level = [(1,'basic'),(2,'Intermediate'),(3,'Admin')]

class user_extended(models.Model):
    access_level = access_level = models.PositiveSmallIntegerField(choices=access_level,default=1)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100,default="")
    mobile = PhoneField(blank=True,help_text="Mobile_Number")
    def __str__(self):
        return self.user.get_username()


