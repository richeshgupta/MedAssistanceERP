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
                return redirect('company')
        else:
            return render('company')
    else:
        form = companyForm()
    context = {'form':form}
    return render(request,'company/company.html',context)

def Product(request):
    form = productForm()
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('product')
        else:
            return redirect('product')
    else:
        form = productForm()
    context = {'form':form}
    return render(request,'company/product.html',context)

def Batch(request):
    form = batchForm()
    if request.method == 'POST':
        form = batchForm(request.POST)
        if form.is_valid():
            form.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('batch')
        else:
            return redirect('batch')
    else:
        form = batchForm()
    context = {'form':form}
    return render(request,'company/batch.html',context)
