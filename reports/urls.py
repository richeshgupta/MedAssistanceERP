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
    path('reports/getWeekly/',GetWeekly),
    path('reports/lastWeek/',GetLastWeekData),
    path('reports/last30days/',Last30days),
    path('reports/getYearly/',GetYearly),
    path('reports/get24hours/',Get24hours),
    path('reports/get24hoursprofit/',Get24hoursProfit),
    path('search/',Search_View,name="search"),
    path('search/getsaledetails/',GetSaleSearchDetail),
    path('search/deletesalebill/',DeleteSaleBill),
    path('search/viewsalebill/',ViewSaleBill)

]