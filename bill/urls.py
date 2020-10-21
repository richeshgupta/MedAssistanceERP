from django.urls import path
from .views import *

urlpatterns = [
    path('sale/',Sale,name='sale'),
    path('purchase/',Bill_Purchase,name='purchase'),
    path('sale/create/',Create_Bill_Sale),
    path('sale/getMedName/',GetMedName),
    path('sale/getMedCompany/',GetMedCompany),
    path('sale/getMedBatch/',GetMedBatch),
    path('sale/getMedSaleRate&Tax/',GetMedSaleRateANDtax),
    path('sale/computeloss/',ComputeLoss),
    path('sale/getQuantity/',getQuantity),
    path('purchase/getPartyWholeseller/',GetPartyWholeseller),
    path('purchase/getMedName/',GetMedName),
    path('purchase/getMedCompany/',GetMedCompany),
    path('purchase/getMedBatch/',GetMedBatch),
    path('purchase/getMedPurchaseRate/',GetMedPurchaseRate),
    path('purchase/getMedTax/',GetMedTax),
    path('purchase/create/',Create_Bill_Purchase),
    path('purchase/getPartyWholesellerID/',GetPartyWholesellerID),
    path('purchase/updateStock/',UpdateStock),
    path('sale/updateStock/',BillUpdateStock),
    path('sale/getPurchaseRate/',getPurchaseRate),

]