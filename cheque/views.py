from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ChequeForm

@login_required(login_url='/')
def Cheque(request):
    if request.method == 'POST':
        form = ChequeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('cheque')
    return render(request,"cheque/main.html",{'form':form})
    
