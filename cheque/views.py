from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ChequeForm

@login_required(login_url='/')
def Cheque(request):
    form = ChequeForm(request.POST)
    if request.method == 'POST':
        print(request.POST)
        # if form.is_valid():
        #     form.save()
    return render(request,"cheque/main.html",{'form':form})
    
