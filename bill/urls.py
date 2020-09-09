from django.urls import path
from .views import Sale,Create_Bill_Sale,GetMed

urlpatterns = [
    path('sale/',Sale,name='sale'),
    path('sale/create/',Create_Bill_Sale),
    path('sale/getMed/',GetMed),
]