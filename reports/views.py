from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.db import connection
import json
from django.core.serializers.json import DjangoJSONEncoder

def report(request):
    if request.method == 'POST':
        duration = request.POST.get('time')
        cur = connection.cursor()
        cur.execute("Select * from bill_Bill_retailer")
        data = cur.fetchall()
        b=[]
        b.append(data)
        return json.dumps(
            data,
            sort_keys = True,
            indent = 1,
            cls = DjangoJSONEncoder
        )
        return HttpResponse(json.dumps(b), content_type='application/json')
        print(duration)

    return render(request,'reports/report.html',{})

