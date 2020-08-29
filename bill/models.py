from django.db import models
from django.utils import timezone

payment = [(1,'Cash'),(2,'Credit')]

class Bill_Wholeseller(models.Model):
    date = models.DateField(default=timezone.now,null=False)
    mode_of_payment = models.PositiveSmallIntegerField(choices=payment,default=1)
    


