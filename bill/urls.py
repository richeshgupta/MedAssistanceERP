from django.urls import path
from .views import *

urlpatterns = [
    path('sale/',Sale,name='sale'),
    path('sale/create/',Create_Bill_Sale),
    path('sale/getMedName/',GetMedName),
    path('sale/getMedCompany/',GetMedCompany),
    path('sale/getMedBatch/',GetMedBatch),
    path('sale/getMedSaleRate&Tax/',GetMedSaleRateANDtax),
    path('sale/computeloss/',ComputeLoss),
    path('sale/getquantity/',GetQuantity),
]