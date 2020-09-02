from django.shortcuts import render

# Create your views here.
def Sale(request):
    return render(request,"bill/sale.html",{})