from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import timedelta
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


bank_list = [('Allahabad Bank','Allahabad Bank'),('Andhra Bank','Andhra Bank'),('Axis Bank','Axis Bank'),('Bank of Bahrain and Kuwait','Bank of Bahrain and Kuwait'),('Bank of Baroda - Corporate Banking','Bank of Baroda - Corporate Banking'),('Bank of Baroda - Retail Banking','Bank of Baroda - Retail Banking'),
('Bank of India','Bank of India'),('Bank of Maharashtra','Bank of Maharashtra'),('Canara Bank','Canara Bank'),('Central Bank of India','Central Bank of India'),('City Union Bank','City Union Bank'),('Corporation Bank','Corporation Bank'),('Deutsche Bank','Deutsche Bank'),('Development Credit Bank','Development Credit Bank'),
('Dhanlaxmi Bank','Dhanlaxmi Bank'),('Federal Bank','Federal Bank'),('ICICI Bank','ICICI Bank'),('IDBI Bank','IDBI Bank'),('Indian Bank','Indian Bank'),('Indian Overseas Bank','Indian Overseas Bank'),('IndusInd Bank','IndusInd Bank'),('ING Vysya Bank','ING Vysya Bank'),('Jammu and Kashmir Bank','Jammu and Kashmir Bank'),
('Karnataka Bank Ltd','Karnataka Bank Ltd'),('Karur Vysya Bank','Karur Vysya Bank'),('Kotak Bank','Kotak Bank'),('Laxmi Vilas Bank','Laxmi Vilas Bank'),('Oriental Bank of Commerce','Oriental Bank of Commerce'),('Punjab National Bank','Punjab National Bank'), 
('Punjab & Sind Bank','Punjab & Sind Bank'),('Shamrao Vitthal Co-operative Bank','Shamrao Vitthal Co-operative Bank'),('South Indian Bank','South Indian Bank'),('State Bank of Bikaner & Jaipur','State Bank of Bikaner & Jaipur'), 
('State Bank of Hyderabad','State Bank of Hyderabad'),('State Bank of India','State Bank of India'),('State Bank of Mysore','State Bank of Mysore'),('State Bank of Patiala','State Bank of Patiala'),('State Bank of Travancore','State Bank of Travancore'), ('Syndicate Bank','Syndicate Bank'),
('Tamilnadu Mercantile Bank Ltd.','Tamilnadu Mercantile Bank Ltd.'),('UCO Bank','UCO Bank'),('Union Bank of India','Union Bank of India'), ('United Bank of India','United Bank of India'), ('Vijaya Bank','Vijaya Bank'), ('Yes Bank Ltd','Yes Bank Ltd')]



class Cheque(models.Model):
    cheque_num = models.CharField(max_length=15,null=False,unique=True)
    bank = models.CharField(choices=bank_list, max_length=40, null=False)
    date_issued = models.DateField(default=timezone.now, null=False)
    date_for_assigned = models.DateField(default=timezone.now)
    amount = models.FloatField(default=0.0)
    party_wholeseller = models.ForeignKey(to='party.Party_Wholeseller', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.cheque_num)+" : "+str(self.bank)