from django.shortcuts import render, redirect
from .forms import *
from users.custom_decorator import *
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponse,JsonResponse
import json
from company.models import Product,Batch


@login_required(login_url='home')
def Company(request):
    form = companyForm()
    if request.method == 'POST':
        form = companyForm(request.POST)
        if form.is_valid:
            form.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('company')
        else:
            return render('company')
    else:
        form = companyForm()
    context = {'form':form}
    return render(request,'company/company.html',context)

# @login_required(login_url='home')
# def Product(request):
#     form = productForm()
#     if request.method == 'POST':
#         form = productForm(request.POST)
#         if form.is_valid():
#             form.save()
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('product')
#         else:
#             return redirect('product')
#     else:
#         form = productForm()
#     context = {'form':form}
#     return render(request,'company/product.html',context)


# @login_required(login_url='home')
# def Batch(request):
#     form = batchForm()
#     if request.method == 'POST':
#         form = batchForm(request.POST)
#         if form.is_valid():
#             form.save()
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('batch')
#         else:
#             return redirect('batch')
#     else:
#         form = batchForm()
#     context = {'form':form}
#     return render(request,'company/batch.html',context)


#dont change the name to product
@login_required(login_url='home')
def Product2(request):
    context={}
    return render(request,"company/product2.html",context)

@login_required(login_url='home')
def Batch1(request):
    context={}
    return render(request,"company/batch.html",context)


def GetMedCompanies(request):
    if request.method=="GET":
        cursor = connection.cursor()
        cursor.execute("SELECT comp_name FROM company_company")
        data= cursor.fetchall()
        return HttpResponse(json.dumps(data), content_type='application/json')


def GetCompanyID(request):
    if request.method == "GET":
        compName = request.GET['CompanyName']
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM company_company where comp_name=%s",[compName])
        return HttpResponse(json.dumps(cursor.fetchone()), content_type='application/json')
    else:
        return ErrorPage(request,"Only GET allowed")


def AddProduct(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        cursor.execute("SELECT max(id) FROM company_product")
        a=cursor.fetchone()[0]
        if(isinstance(a, int)):
            a=a+1
        else:
            a=1
        Product.objects.create(
            id = a,
            name = request.POST['name'],
            company_id = int(request.POST['company']),
            scheduled_drug = request.POST['scheduled_drug'],
            unit_of_packing = request.POST['unit_of_packing'],
            sale_rate = request.POST['sale_rate'],
            gst = request.POST['gst'],
            free = 0,
        )
        return HttpResponse('')

def GetMedProducts(request):
    if request.method=="GET":
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM company_product")
        data= cursor.fetchall()
        b=[]
        [b.append(a[0]) for a in data if a[0] not in b]
        return HttpResponse(json.dumps(b), content_type='application/json')

def GetMedCompany(request):
    if request.method=="GET":
        medName=request.GET['medName']
        cursor = connection.cursor()
        cursor.execute("SELECT company_id FROM company_product where name=%s",[medName])
        data= cursor.fetchall()
        b=[a[0] for a in data]
        d=[]
        for a in b:
            cursor.execute("SELECT comp_name FROM company_company where id=%s",[a])
            d.append(cursor.fetchone()[0])
        return HttpResponse(json.dumps(d), content_type='application/json')

def GetMedID(request):
    if request.method == "GET":
        medName = request.GET['MedName']
        compName = request.GET['CompanyName']
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM company_company where comp_name=%s",[compName])
        medCompany=cursor.fetchone()[0]
        cursor.execute("SELECT id FROM company_product where name=%s and company_id=%s",[medName,medCompany])
        return HttpResponse(json.dumps(cursor.fetchone()), content_type='application/json')
    else:
        return ErrorPage(request,"Only GET allowed")

def AddBatch(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        cursor.execute("SELECT max(id) FROM company_batch")
        a=cursor.fetchone()[0]
        if(isinstance(a, int)):
            a=a+1
        else:
            a=1
        Batch.objects.create(
            id = a,
            batch_number = request.POST['batch_number'],
            expiry = request.POST['expiry'],
            product_id = int(request.POST['product_id']),
            mrp = request.POST['mrp'],
            purchase_rate = request.POST['purchase_rate'],
            quantity = 0,
        )
        return HttpResponse('')