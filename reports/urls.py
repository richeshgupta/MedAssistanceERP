from django.urls import path
from .views import *

urlpatterns = [
    path('saleReportDuration/',report,name='saleReportDuration'),
    path('saleReportCompany/',report,name='saleReportCompany'),
    path('saleReportDate/',report,name='saleReportDate'),
]