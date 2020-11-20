from django.urls import path
from .views import *

urlpatterns = [
    path('saleReportDuration/',ReportView.as_view(),name='saleReportDuration'),
    path('ReportInfo/',Bill_View.as_view(),name='ReportInfo'),
    path('saleReportCompany/',ReportView.as_view(),name='saleReportCompany'),
    path('saleReportDate/',ReportView.as_view(),name='saleReportDate'),
    path('reports/',Reports_View,name="reports"),
    path('reports/getRevenue/',GetRevenue),
    path('reports/getPurchase/',GetPurchase),
    path('reports/getdetails/',GetDetails),
    path('reports/getProfit/',GetProfit),
    path('search/',Search_View,name="search"),
    path('search/getsaledetails/',GetSaleSearchDetail),
    path('search/deletesalebill/',DeleteSaleBill),
    path('search/viewsalebill/',ViewSaleBill)
]