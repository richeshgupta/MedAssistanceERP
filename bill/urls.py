from django.urls import path
from .views import Sale,create_bill_sale

urlpatterns = [
    path('sale/',Sale,name='sale'),
    path('sale/create/',create_bill_sale),
]