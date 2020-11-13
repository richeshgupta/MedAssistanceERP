from django.urls import path
from .views import GSTGenerate,GSTSaleReturn,GSTPurchaseReturn,GSTSaleReport
urlpatterns = [
    path('',GSTGenerate,name="gst"),
    path('saleReturn/',GSTSaleReturn,name="saleReturn"),
    path('PurchaseReturn/',GSTPurchaseReturn,name="purchaseReturn"),
    path('GenSaleReturn/',GSTSaleReport,name='gst-sale-return'),
]