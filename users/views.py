from django.shortcuts import render
from django.contrib.auth import logout

def home(request):
    return render(request,'users/index.html')
    
def Test(request):
    return render(request,"users/test.html",{})

def Reg(request):
    return render(request,"users/reg.html",{})

def Logout(request):
    logout(request)
    return render(request,"users/logged-out.html",{})
