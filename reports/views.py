from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.db import connection
from django.views.generic import TemplateView
import json
from django.http import JsonResponse
from bill.models import *
from .serializers import *

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

