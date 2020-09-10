from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def Cheque(request):
    return render(request,"cheque/main.html",{})

def Create_Cheque(request):
    if reuqest.method == 'POST':
        Cheque.objects.create(
            cheque_num = request.POST['cheque_number'],
            bank = request.POST['bank_name'],
            

        )
