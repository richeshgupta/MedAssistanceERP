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
from datetime import datetime,timedelta

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

        cur = connection.cursor()
        cur.execute("Select * from bill_Bill_retailer")
        data = cur.fetchall()
       
        print(data)
        date=[]
        customer_name= []
        mail= []
        name = []
        for i in range(0,len(data)):
        
            date.append(data[i][1])
            customer_name.append(data[i][2])
            mail.append(data[i][3])
            name.append(data[i][6])
        args = {'date':date, 'customer_name':customer_name, 'mail':mail, 'name':name}
        
        return render(request,self.template_name, args)

def GetRevenue(request):
    if request.method=="GET":
        cursor = connection.cursor()
        #years

        i=1
        data=[]
        year = datetime.today().strftime("%Y")
        while(i<=12):
            cursor.execute("Select sum(total_bill) from bill_bill_retailer where date_part('month',date)=%s and date_part('year',date)=%s",[i,year])
            data.append(cursor.fetchall()[0][0])
            i+=1

        return HttpResponse(json.dumps(data),content_type="application/json")
    else:
        return ErrorPage(request,"Only GET allowed")

def GetPurchase(request):
    if request.method=="GET":
        cursor = connection.cursor()
        #years
     
        i=1
        data=[]
        year = datetime.today().strftime("%Y")
        while(i<=12):
            cursor.execute("Select sum(total_bill) from bill_purchase where date_part('month',date)=%s and date_part('year',date)=%s",[i,year])
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
        year = datetime.today().strftime("%Y")
        while(i<=12):
            cursor.execute("Select sum(profit) from bill_bill_retailer where date_part('month',date)=%s and date_part('year',date)=%s",[i,year])
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



def GetLastWeekData(request):
    week_date = datetime.now() - timedelta(days=7)
    x = Bill_Retailer.objects.filter(date__gte=week_date)
    weekly_data=[]
    for i in x:
        weekly_data.append(i.total_bill)
    return HttpResponse(json.dumps(weekly_data),content_type="application/json")

def Last30days(request):
    time_frame = datetime.now()-timedelta(days=30)
    objs = Bill_Retailer.objects.filter(date__gte=time_frame)
    last30days = []
    profit30days=[]
    for i in objs:
        last30days.append(i.total_bill)
        profit30days.append(i.profit)
    
    data = {'30daysale':sum(last30days),'30dayprofit':sum(profit30days)}
    print("Last 30 days : ",data)
    return HttpResponse(json.dumps(data),content_type="application/json")

    
def GetYearly(request):
    time_frame = datetime.now() - timedelta(days=365)
    objs = Bill_Retailer.objects.filter(date__gte=time_frame)
    Yearly_data = []
    for i in objs:
        Yearly_data.append(i.total_bill)

    return HttpResponse(json.dumps(sum(Yearly_data)),content_type="application/json")


def Get24hours(request):
    time_frame = datetime.now() - timedelta(days = 1)
    objs = Bill_Retailer.objects.filter(date__gte=time_frame)
    data24hours = []
    for i in objs:
        data24hours.append(i.total_bill)
    return HttpResponse(json.dumps(sum(data24hours)),content_type='application/json')
        
def GetWeekly(request):
    month = datetime.today().strftime("%m")
    year = datetime.today().strftime("%Y")
    cursor = connection.cursor()
    data=[]
    i=1
    d=7
    while(i<=5):
        cursor.execute("Select sum(total_bill) from bill_bill_retailer where date_part('month',date)=%s and date_part('year',date)=%s and date_part('day',date)<=%s and  date_part('day',date)>%s",[month,year,str(d),str(d-7)])
        a=cursor.fetchall()[0][0]
        if(a==None):
            data.append(0)
        else:
            data.append(a)
        i+=1
        d+=7
        
        return HttpResponse(json.dumps(data),content_type="application/json")
    else:
        return ErrorPage(request,"Only GET allowed")
    

