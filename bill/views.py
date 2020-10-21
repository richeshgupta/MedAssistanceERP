from django.shortcuts import render
from .models import Bill_Retailer,Purchase
from django.http import HttpResponse,JsonResponse
from company.models import Product,Batch
from party.models import Party_Wholeseller
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import connection
from users.views import ErrorPage
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
import os
from django.conf import settings
from django.contrib.staticfiles import finders



@login_required(login_url='/')
def Sale(request):
    return render(request,"bill/sale2.html",{})

def Bill_Purchase(request):
    return render(request,"bill/purchase.html",{})

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
        a='done'
        return HttpResponse(json.dumps({'a': a}), content_type="application/json")
    # else:
    #     return ErrorPage(request,"Only POST allowed")

def Create_Bill_Purchase(request):
    if request.method == 'POST':
        Purchase.objects.create(
            party_id = int(request.POST['party_wholeseller']),
            mode_of_payment = request.POST['mode_of_payment'],
            total_bill = request.POST['total_bill'],
            name = request.POST.getlist('name'),
            company = request.POST.getlist('company'),
            batch_number = request.POST.getlist('batch_number'),
            quantity = request.POST.getlist('quantity'),
            discount = request.POST.getlist('discount'),
            deal = request.POST.getlist('deal'),
            tax = request.POST.getlist('tax'),
            purchase_rate = request.POST.getlist('purchase_rate'),
        )
        a='done'
        return HttpResponse(json.dumps({'a': a}), content_type="application/json")



def GetMedName(request):
    if request.method=="GET":
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM company_product")
        data= cursor.fetchall()
        b=[]
        [b.append(a[0]) for a in data if a[0] not in b]
        return HttpResponse(json.dumps(b), content_type='application/json')
    else:
        return ErrorPage(request,"Only GET allowed")


def GetMedCompany(request):
    if request.method=="GET":
        medName=request.GET['medName']
        # print("Requesting db for : ",medName)
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
    else:
        ErrorPage(request,"POST requests are not allowed")

def getQuantity(request):
    if request.method=="GET":
        medName=request.GET['medName']
        medCompany = request.GET['medCompany']
        batch_no = request.GET['batch']
        print("Batch came : ",batch_no," medName : ",medName," company :",medCompany)
        cursor = connection.cursor()
        cursor.execute("select id from company_company where comp_name=%s",[medCompany])
        comp_id = cursor.fetchone()[0]
        print("comp id: ",comp_id)
        cursor.execute('select id from company_product where name=%s and company_id=%s ',[medName,comp_id])
        med_id = cursor.fetchone()[0]
        print("medId : ",med_id)
        cursor.execute('select quantity from company_batch where product_id=%s and batch_number=%s',[med_id,batch_no])
        quan = cursor.fetchone()[0]
        print("comp id:",comp_id,"\n product id:",med_id,"\n Quantity :",quan)

        return HttpResponse(json.dumps(quan),content_type='application/json')
    else:
        return ErrorPage(request,"POST requests are not allowed")

def getPurchaseRate(request):
    if request.method=="GET":
        medName=request.GET['medName']
        medCompany = request.GET['medCompany']
        batch_no = request.GET['batch']
        cursor = connection.cursor()
        cursor.execute('select id from company_company where comp_name=%s',[medCompany])
        comp_id = comp_id = cursor.fetchone()[0]
        cursor.execute('select id from company_product where name=%s and company_id=%s ',[medName,comp_id])
        med_id = cursor.fetchone()[0]
        cursor.execute('select purchase_rate from company_batch where product_id=%s and batch_number=%s',[med_id,batch_no])
        purchase_rate = cursor.fetchone()[0]
        return HttpResponse(json.dumps(purchase_rate),content_type='application/json')
    else:
        return ErrorPage("Only GET requests are allowed")


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
    else:
        return ErrorPage(request,"POST requests are not allowed")



        


def GetPartyWholeseller(request):
    if request.method=="GET":
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM party_party_wholeseller")
        data= cursor.fetchall()
        b=[]
        [b.append(a[0]) for a in data if a[0] not in b]
        return HttpResponse(json.dumps(b), content_type='application/json')
    else:
        return ErrorPage(request,"only GET requests are allowed")

def GetMedPurchaseRate(request):
    medName = request.GET['medName']    # Getting all MedName from client
    compname = request.GET['medCompany']
    batch_no = request.GET['medBatch']
    cursor = connection.cursor()
    cursor.execute("select id from company_company where comp_name=%s",[compname])
    comp_id = cursor.fetchone()[0]
    cursor.execute('select id from company_product where name=%s and company_id=%s ',[medName,comp_id])
    med_id = cursor.fetchone()[0]
    cursor.execute('select purchase_rate from company_batch where product_id=%s and batch_number=%s',[med_id,batch_no])
    pur = cursor.fetchall()[0]
    return HttpResponse(json.dumps(pur),content_type="application/json")

def GetMedTax(request):
    if request.method == "GET":
        medName = request.GET['medName']
        medCompany = request.GET['medCompany']
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM company_company where comp_name=%s",[medCompany])
        medCompanyID = cursor.fetchone()[0]
        cursor.execute("SELECT gst FROM company_product where name=%s and company_id=%s",[medName,medCompanyID])
        return HttpResponse(json.dumps(cursor.fetchone()), content_type='application/json')
    else:
        return ErrorPage(request,"Only GET allowed")

def GetPartyWholesellerID(request):
    if request.method == "GET":
        partyName = request.GET['party_wholeseller']
        cursor = connection.cursor()
        cursor.execute("SELECT party_id FROM party_party_wholeseller where name=%s",[partyName])
        return HttpResponse(json.dumps(cursor.fetchone()), content_type='application/json')
    else:
        return ErrorPage(request,"Only GET allowed")


def PurchaseUpdateStock(request):
    if request.method == "POST":
        medName = request.POST.getlist('name')
        medCompany = request.POST.getlist('company')
        batch_no=request.POST.getlist('batch_number')
        quantity=request.POST.getlist('quantity')
        cursor = connection.cursor()
        #loop
        i=0
        l=len(medName)
        while(i<l):
            cursor.execute("SELECT id FROM company_company where comp_name=%s",[medCompany[i]])
            medCompanyID = cursor.fetchone()[0]
            cursor.execute("SELECT id,free FROM company_product where name=%s and company_id=%s",[medName[i],medCompanyID])
            a=cursor.fetchone()
            medID=a[0]
            pro_quantity=a[1]
            new_pro_quantity=int(pro_quantity)+int(quantity[i])
            cursor.execute("Update company_product SET free=%s where id=%s",[new_pro_quantity,medID])
            cursor.execute('select id,quantity from company_batch where product_id=%s and batch_number=%s',[medID,batch_no[i]])
            a=cursor.fetchone()
            batchID=a[0]
            batch_quantity=a[1]
            new_batch_quantity=int(batch_quantity)+int(quantity[i])
            cursor.execute("Update company_batch SET quantity=%s where id=%s",[new_batch_quantity,batchID])
            i+=1
        a='done'
        return HttpResponse(json.dumps({'a': a}), content_type="application/json")
    else:
        return ErrorPage(request,"Only POST allowed")


def SaleUpdateStock(request):
    if request.method == "POST":
        medName = request.POST.getlist('name')
        medCompany = request.POST.getlist('company')
        batch_no=request.POST.getlist('batch_number')
        quantity=request.POST.getlist('quantity')
        cursor = connection.cursor()
        #loop
        i=0
        l=len(medName)
        while(i<l):
            cursor.execute("SELECT id FROM company_company where comp_name=%s",[medCompany[i]])
            medCompanyID = cursor.fetchone()[0]
            cursor.execute("SELECT id,free FROM company_product where name=%s and company_id=%s",[medName[i],medCompanyID])
            a=cursor.fetchone()
            medID=a[0]
            pro_quantity=a[1]
            new_pro_quantity=int(pro_quantity)-int(quantity[i])
            cursor.execute("Update company_product SET free=%s where id=%s",[new_pro_quantity,medID])
            cursor.execute('select id,quantity from company_batch where product_id=%s and batch_number=%s',[medID,batch_no[i]])
            a=cursor.fetchone()
            batchID=a[0]
            batch_quantity=a[1]
            new_batch_quantity=int(batch_quantity)-int(quantity[i])
            cursor.execute("Update company_batch SET quantity=%s where id=%s",[new_batch_quantity,batchID])
            i+=1
        
        a='done'
        return HttpResponse(json.dumps({'a': a}), content_type="application/json")



def GetSalePDF(request):
    cursor = connection.cursor()
    cursor.execute("SELECT max(id) FROM bill_bill_retailer")
    bill_id=cursor.fetchone()[0]
    cursor.execute("SELECT * FROM bill_bill_retailer where id=%s",[bill_id])
    bill=cursor.fetchone()
    data={}
    data['id']=bill[0]
    data['date']=bill[1]
    data['customer_name']=bill[2]
    data['customer_email']=bill[3]
    if(bill[4] == 1):
        mop='Cash'
    else:
        mop='Card'
    data['mode_of_payment']=mop
    data['total_bill']=bill[5]

    i=0
    l=len(bill[6])
    product_list=[]
    while(i<l):
        temp={}
        temp['name']=bill[6][i]
        temp['company']=bill[7][i]
        temp['batch_number']=bill[8][i]
        temp['quantity']=bill[9][i]
        temp['discount']=bill[10][i]
        temp['deal']=bill[11][i]
        temp['tax']=bill[12][i]
        temp['loss']=bill[13][i]
        temp['sale_rate']=bill[14][i]
        product_list.append(temp)
        i+=1

    data['product_list']=product_list
    template=get_template("bill/sale_pdf_page.html")
    data_p=template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(data_p.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def GetPurchasePDF(request):
    cursor = connection.cursor()
    cursor.execute("SELECT max(id) FROM bill_purchase")
    bill_id=cursor.fetchone()[0]
    cursor.execute("SELECT * FROM bill_purchase where id=%s",[bill_id])
    bill=cursor.fetchone()
    data={}
    data['id']=bill[0]
    data['date']=bill[1]
    
    #party id
    party_id=bill[12]
    cursor.execute("SELECT name FROM party_party_wholeseller where party_id=%s",[party_id])
    data['party']=cursor.fetchone()[0]



    if(bill[2] == 1):
        mop='Cash'
    else:
        mop='Card'
    data['mode_of_payment']=mop
    data['total_bill']=bill[3]

    i=0
    l=len(bill[4])
    product_list=[]
    while(i<l):
        temp={}
        temp['name']=bill[4][i]
        temp['company']=bill[5][i]
        temp['batch_number']=bill[6][i]
        temp['quantity']=bill[7][i]
        temp['discount']=bill[8][i]
        temp['deal']=bill[9][i]
        temp['tax']=bill[10][i]
        temp['purchase_rate']=bill[11][i]
        product_list.append(temp)
        i+=1

    data['product_list']=product_list
    template=get_template("bill/purchase_pdf_page.html")
    data_p=template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(data_p.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


