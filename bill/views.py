from django.shortcuts import render
from .models import Bill_Retailer
from django.http import HttpResponse

# Create your views here.
def Sale(request):
    return render(request,"bill/sale.html",{})


def create_bill_sale(request):
    if request.method == 'POST':
        Bill_Retailer.objects.create(
            customer_name = request.POST['customer_name'],
            customer_email = request.POST['customer_email'],
            mode_of_payment = request.POST['mode_of_payment'],
            total_bill = request.POST['total_bill'],
            name = request.POST.getlist('name'),
            batch_number = request.POST.getlist('batch_number'),
            quantity = request.POST.getlist('quantity'),
            discount = request.POST.getlist('discount'),
            deal = request.POST.getlist('deal'),
            tax = request.POST.getlist('tax'),
            loss = request.POST.getlist('loss'),
            sale_rate = request.POST.getlist('sale_rate'),
        )
        # x.save()

        return HttpResponse('')