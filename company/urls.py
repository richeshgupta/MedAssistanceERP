from django.urls import path
from .views import *

urlpatterns = [
    path('company/',Company,name='company'),
    path('product2/',Product2,name='product'),
    path('batch/',Batch1,name='batch'),
    path('product2/getMedCompanies/',GetMedCompanies),
    path('product2/addProduct/',AddProduct),
    path('product2/getCompanyID/',GetCompanyID),
    path('batch/getMedProducts/',GetMedProducts),
    path('batch/getMedCompany/',GetMedCompany),
    path('batch/getMedID/',GetMedID),
    path('batch/addBatch/',AddBatch),
]