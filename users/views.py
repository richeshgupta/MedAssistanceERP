from django.shortcuts import render


def Test(request):
    return render(request,"users/test.html",{})

def home(request):
    return render(request,"users/login.html",{})