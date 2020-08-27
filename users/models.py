from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 1 - Basic, 2 - Intermediate, 3 - Admin (see docs) for better understanding of access_level
access_level = [1,2,3]

class user_relationship(models.Model):
    access_level = models.IntegerField(choices=access_level,default=1)
    models.ForeignKey(User,on_delete=models.CASCADE)
    

