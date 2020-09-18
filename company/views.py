from django.shortcuts import render, redirect
from .forms import *

def Company(request):
    form = companyForm()
    if request.method == 'POST':
        form = companyForm(request.POST)
        if form.is_valid:
            form.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            return render('company')
    else:
        form = companyForm()
    context = {'form':form}
    return render(request,'company/company.html',context)

def Product(request):
    return render(request,'company/product.html')

def Batch(request):
    return render(request,'company/batch.html')
