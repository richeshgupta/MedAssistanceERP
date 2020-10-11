from django.shortcuts import render
from .models import Bill_Retailer
from django.http import HttpResponse,JsonResponse
from company.models import Product,Batch
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import connection
from users.views import ErrorPage

@login_required(login_url='/')
def Sale(request):
    return render(request,"bill/sale2.html",{})

@login_required(login_url='home')
def Create_Bill_Sale(request):
    if request.method == 'POST':
        Bill_Retailer.objects.create(
            customer_name = request.POST['customer_name'],
            customer_email = request.POST['customer_email'],
            mode_of_payment = request.POST['mode_of_payment'],
            total_bill = request.POST['total_bill'],
            name = request.POST.getlist('name'),
            company = request.POST.getlist('company'),
            batch_number = request.POST.getlist('batch_number'),
            quantity = request.POST.getlist('quantity'),
            discount = request.POST.getlist('discount'),
            deal = request.POST.getlist('deal'),
            tax = request.POST.getlist('tax'),
            loss = request.POST.getlist('loss'),
            sale_rate = request.POST.getlist('sale_rate'),
        )
        return HttpResponse('')
    # else:
    #     return ErrorPage(request,"Only POST allowed")


def GetMedName(request):
    if request.method=="GET":
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM company_product")
        data= cursor.fetchall()
        b=[]
        [b.append(a[0]) for a in data if a[0] not in b]
        return HttpResponse(json.dumps(b), content_type='application/json')
    # else:
    #     return ErrorPage(request,"Only GET allowed")


def GetMedCompany(request):
    if request.method=="GET":
        medName=request.GET['medName']
        print("Requesting db for : ",medName)
        cursor = connection.cursor()
        cursor.execute("SELECT company_id FROM company_product where name=%s",[medName])
        data= cursor.fetchall()
        b=[a[0] for a in data]
        d=[]
        for a in b:
            cursor.execute("SELECT comp_name FROM company_company where id=%s",[a])
            d.append(cursor.fetchone()[0])
        return HttpResponse(json.dumps(d), content_type='application/json')
    

def GetMedBatch(request):
    if request.method=="GET":
        medName=request.GET['medName']
        medCompany=request.GET['medCompany']
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM company_company where comp_name=%s",[medCompany])
        medCompany=cursor.fetchone()[0]
        cursor.execute("SELECT id FROM company_product where name=%s and company_id=%s",[medName,medCompany])
        pro_id=cursor.fetchall()[0]
        cursor.execute("SELECT batch_number FROM company_batch where product_id=%s",[pro_id])
        temp_batches=cursor.fetchall()
        batches=[a[0] for a in temp_batches]
        return HttpResponse(json.dumps(batches), content_type='application/json')


def GetMedSaleRateANDtax(request):
    if request.method == "GET":
        medName = request.GET['medName']
        medCompany = request.GET['medCompany']
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM company_company where comp_name=%s",[medCompany])
        medCompanyID = cursor.fetchone()[0]
        cursor.execute("SELECT sale_rate,gst FROM company_product where name=%s and company_id=%s",[medName,medCompanyID])
        return HttpResponse(json.dumps(cursor.fetchone()), content_type='application/json')
    else:
        return ErrorPage(request,"Only GET allowed")




def ComputeLoss(request):
    if request.method == "GET":
        medName = request.GET.getlist('medName')
        medCompany = request.GET.getlist('medCompany')
        batch_no = request.GET.getlist('batch_no')
        sale_rate = request.GET.getlist('sale_rate')
        cursor = connection.cursor()
        loss=[]
        i=0
        l=len(medName)
        while(i<l):
            cursor.execute("SELECT id FROM company_company where comp_name=%s",[medCompany[i]])
            medCompanyID = cursor.fetchone()[0]
            cursor.execute("SELECT id FROM company_product where name=%s and company_id=%s",[medName[i],medCompanyID])
            medProductID = cursor.fetchone()[0]
            cursor.execute("SELECT purchase_rate FROM company_batch where product_id=%s and batch_number=%s",[medProductID,batch_no[i]])
            purchase_rate=cursor.fetchone()[0]
            if(float(purchase_rate) < float(sale_rate[i])):
                loss.append('False')
            else:
                loss.append('True')
            i+=1
        return HttpResponse(json.dumps(loss), content_type='application/json')
