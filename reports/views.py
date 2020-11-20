from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.db import connection
from django.views.generic import TemplateView
import json
from django.http import JsonResponse
from bill.models import *
from django.template.loader import get_template
from bill.utils import render_to_pdf
from profile_retailer.models import *
from django.urls import resolve

def Reports_View(request):
    return render(request,"reports/reports.html",{})

def Search_View(request):
    return render(request,"reports/search.html",{})

class ReportView(TemplateView):
    def get(self, request):
        return render(request,'reports/report.html')
    def post(self, request):
        global duration
        duration = request.POST.get('time')
        return redirect('ReportInfo')
    # if request.method == 'POST':
    #     return redirect('saleReportDurationInfo')

class Bill_View(TemplateView):
    template_name = 'reports/show.html'
    def get(self, request):
        # serializer = Bill_ViewSerializer()
        # return JsonResponse({"category details":serializer.data})
        # bills = Bill_Retailer.objects.all()
        cur = connection.cursor()
        cur.execute("Select * from bill_Bill_retailer")
        data = cur.fetchall()
        # data = serializer.data
        # data = serializers.serialize('json', bill_Bill_retailer.objects.all(), fields=('date'))
        print(data)
        date=[]
        customer_name= []
        mail= []
        name = []
        for i in range(0,len(data)):
        #     # args = {'date':(data[i][1], ), 'customer_name':(data[i][2], )}
            date.append(data[i][1])
            customer_name.append(data[i][2])
            mail.append(data[i][3])
            name.append(data[i][6])
        args = {'date':date, 'customer_name':customer_name, 'mail':mail, 'name':name}
        # print(args)
        return render(request,self.template_name, args)
        # return HttpResponse(json.dumps(data), content_type='application/json')
    # return render(request,'reports/report.html',{})

def GetRevenue(request):
    if request.method=="GET":
        cursor = connection.cursor()
        #years
        # cursor.execute("Select extract(year from date) from bill_bill_retailer")
        # data= cursor.fetchall()
        # i=0
        # year=[]
        # while(i<len(data)):
        #     if(data[i][0] not in year):
        #         year.append(int(data[i][0]))
        #     i+=1
        # for y in year:
        i=1
        data=[]
        while(i<=12):
            cursor.execute("Select sum(total_bill) from bill_bill_retailer where date_part('month',date)=%s",[i])
            data.append(cursor.fetchall()[0][0])
            i+=1

        return HttpResponse(json.dumps(data),content_type="application/json")
    else:
        return ErrorPage(request,"Only GET allowed")

def GetPurchase(request):
    if request.method=="GET":
        cursor = connection.cursor()
        #years
        # cursor.execute("Select extract(year from date) from bill_bill_retailer")
        # data= cursor.fetchall()
        # i=0
        # year=[]
        # while(i<len(data)):
        #     if(data[i][0] not in year):
        #         year.append(int(data[i][0]))
        #     i+=1
        # for y in year:
        i=1
        data=[]
        while(i<=12):
            cursor.execute("Select sum(total_bill) from bill_purchase where date_part('month',date)=%s",[i])
            data.append(cursor.fetchall()[0][0])
            i+=1

        return HttpResponse(json.dumps(data),content_type="application/json")
    else:
        return ErrorPage(request,"Only GET allowed")

def GetProfit(request):
    if request.method=="GET":
        cursor = connection.cursor()
        i=1
        data=[]
        while(i<=12):
            cursor.execute("Select sum(profit) from bill_bill_retailer where date_part('month',date)=%s",[i])
            data.append(cursor.fetchall()[0][0])
            i+=1

        return HttpResponse(json.dumps(data),content_type="application/json")
    else:
        return ErrorPage(request,"Only GET allowed")

def GetDetails(request):
    if request.method=="GET":
        cursor = connection.cursor()
        cursor.execute("Select quantity from bill_bill_retailer")
        temp=cursor.fetchall()
        sold=0
        for s in temp:
            for a in s[0]:
                sold+=a
        cursor.execute("Select quantity from bill_purchase")
        temp=cursor.fetchall()
        purchased=0
        for s in temp:
            for a in s[0]:
                purchased+=a
        cursor.execute("Select sum(free) from company_product")
        stock=cursor.fetchone()[0]
        data=[]
        data.append(sold)
        data.append(purchased)
        data.append(stock)
        #employee
        cursor.execute("Select count(id) from users_user_extended")
        emp=cursor.fetchone()[0]
        data=[]
        data.append(sold)
        data.append(purchased)
        data.append(stock)
        data.append(emp)
        return HttpResponse(json.dumps(data),content_type="application/json")
    else:
        return ErrorPage(request,"Only GET allowed")


def GetSaleSearchDetail(request):
    if request.method=="GET":
        inp = request.GET['input']
        cat = request.GET['category']
        cursor = connection.cursor()
        if(cat=='cust name'):
            cursor.execute("Select * from bill_bill_retailer where customer_name=%s",[inp])
        elif(cat=='bill no'):
            cursor.execute("Select * from bill_bill_retailer where id=%s",[inp])
        elif(cat=='date'):
            cursor.execute("Select * from bill_bill_retailer where date=%s",[inp])
        elif(cat=='rate'):
            cursor.execute("Select * from bill_bill_retailer where total_bill=%s",[inp])
        data= cursor.fetchall()
        return JsonResponse(data, content_type='application/json',safe=False)

def DeleteSaleBill(request):
    if request.method=="POST":
        id=request.POST['id']
        cursor = connection.cursor()
        cursor.execute("Delete from bill_bill_retailer where id=%s",[id])
        data='success'
        return JsonResponse(data, content_type='application/json',safe=False)

def ViewSaleBill(request):
    cursor = connection.cursor()
    id=request.GET['id']
    cursor.execute("SELECT * FROM bill_bill_retailer where id=%s",[id])
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
    data['bill_id'] = id
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
    try:
        obj = Profile_Retailer.objects.all()[0]
        shop_name = obj.Shop_Name
        Address  = obj.Address
        GST = obj.GST
        DL = obj.DL_no
        contact = obj.contact
        # print("shop",shop_details)
    except Exception as e:
        print(e)
        shop_name = "NULL"
        Address  = "NULL"
        GST = "NULL"
        DL = "NULL"
        contact = "NULL"
            
    data['shop_name'] = shop_name
    data['address']=Address
    data['GST'] = GST
    data['dl'] = DL
    data['contact'] = contact
    template = get_template("bill/sale_pdf_page.html")
    pdf = render_to_pdf('bill/sale_pdf_page.html',data)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("CustomerName_Date")
        content = "inline; filename='%s" %(filename)
        download = request.GET.get("download")
        content = "attachment; filename='%s" %(filename)
        response['Content-Disposition'] = content
        current_url = resolve(request.path_info).url_name
        print(current_url)
        return response
    return ErrorPage(request,"PDF Not Found")


