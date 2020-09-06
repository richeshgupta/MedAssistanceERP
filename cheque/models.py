from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
# from party.models import Party_Retailer,Party_Wholeseller


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Cheque(models.Model):
    cheque_num = models.CharField(max_length=10)
    bank = models.CharField(max_length=30)
    date_issued = models.DateField(auto_now=True)
    date_for_assigned = models.DateField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    amount = models.FloatField(default=0.0)
    def __str__(self):
        return str(self.cheque_num)+" : "+str(self.bank)