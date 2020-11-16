from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.db import connection
from django.views.generic import TemplateView
import json
from django.http import JsonResponse
from bill.models import *

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