from django.urls import path
from .views import *

urlpatterns = [
    path('saleReportDuration/',ReportView.as_view(),name='saleReportDuration'),
    path('ReportInfo/',Bill_View.as_view(),name='ReportInfo'),
    path('saleReportCompany/',ReportView.as_view(),name='saleReportCompany'),
    path('saleReportDate/',ReportView.as_view(),name='saleReportDate'),
]