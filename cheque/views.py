from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ChequeForm

@login_required(login_url='/')
def Cheque(request):
    form = ChequeForm()
    if request.method == 'POST':
        form = ChequeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            return redirect('cheque')
    else:
        form = ChequeForm()
    return render(request,"cheque/main.html",{'form':form})
    
