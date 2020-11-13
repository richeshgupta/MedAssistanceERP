from django.shortcuts import render
from bill.models import *
from users.views import ErrorPage
from django.http import HttpResponse
import csv
import json
# Create your views here.
def GSTGenerate(request):
    return render(request,"gst/gst.html",{})

def GSTPurchaseReturn(request):
    return render(request,"gst/gst_pur.html",{})

def GSTSaleReturn(request):
    return render(request,"gst/gst_sale.html",{})    

def GSTSaleReport(request):
    if request.method=='GET':
        month = request.GET['month']
        year = request.GET['year']
        query = Bill_Retailer.objects.filter(date__year=year,date__month=month)
        fields=['bill no','date','customer name','customer email','mode of payment','total bill (Rs.)']
        filename='D:/Sale_GSTR-'+month+"-"+year+".csv"
        data = []
        for i in query:
            data.append([i.id,i.date,i.customer_name,i.customer_email,i.mode_of_payment,i.total_bill])
            

        with open(filename,'w',newline='') as csvf:
            csvw = csv.writer(csvf)
            csvw.writerow(fields)
            csvw.writerows(data)
            
    else:       
        
        return ErrorPage(request,"only GET req. allowed")

def GSTPurchaseReport(request):
    if request.method=='GET':
        month = request.GET['month']
        year = request.GET['year']
        query = Purchase.objects.filter(date__year=year,date__month=month)
        fields=['bill no','date','party','mode of payment','total bill (Rs.)']
        filename='D:/Purchase_GSTR-'+month+"-"+year+".csv"
        data = []
        for i in query:
            data.append([i.id,i.date,i.party,i.mode_of_payment,i.total_bill])
            

        with open(filename,'w',newline='') as csvf:
            csvw = csv.writer(csvf)
            csvw.writerow(fields)
            csvw.writerows(data)
            
    else:
        return ErrorPage(request,"Only GET req. allowed")       
        
    