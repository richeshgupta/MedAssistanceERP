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
        duration = request.POST.get('time')
        print(duration)
        return redirect('ReportInfo')
    # if request.method == 'POST':
    #     return redirect('saleReportDurationInfo')

class Bill_View(TemplateView):
    template_name = 'reports/show.html'
    def get(self, request):
        # serializer = Bill_ViewSerializer()
        # return JsonResponse({"category details":serializer.data})
        bills = Bill_Retailer.objects.all()
        args = {'bills':bills}
        return render(request,self.template_name, args)
    # if request.method == 'POST':
        # duration = request.POST.get('time')
        # cur = connection.cursor()
        # cur.execute("Select * from bill_Bill_retailer")
        # data = cur.fetchall()
        # data = serializers.serialize('json', bill_Bill_retailer.objects.all(), fields=('date'))
        # b=[]
        # b.append(data)
        # return HttpResponse(json.dumps(data), content_type='application/json')
        # print(duration)

    # return render(request,'reports/report.html',{})

