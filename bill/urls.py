from django.urls import path
from .views import Sale,Create_Bill_Sale,GetMedName,GetMedBatch,GetMedSaleRateANDtax,GetMedCompany,ComputeLoss

urlpatterns = [
    path('sale/',Sale,name='sale'),
    path('sale/create/',Create_Bill_Sale),
    path('sale/getMedName/',GetMedName),
    path('sale/getMedCompany/',GetMedCompany),
    path('sale/getMedBatch/',GetMedBatch),
    path('sale/getMedSaleRate&Tax/',GetMedSaleRateANDtax),
    path('sale/computeloss/',ComputeLoss),
]