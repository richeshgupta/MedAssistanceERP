from django.urls import path
from .views import *

urlpatterns = [
    path('company/',Company,name='company'),
    path('product/',Product,name='product'),
    path('product2/',Product2,name='product'),
    path('batch/',Batch,name='batch'),

]