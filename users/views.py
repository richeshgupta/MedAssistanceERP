from django.shortcuts import render

def home(request):
    return render(request,'users/index.html')
    
def Test(request):
    return render(request,"users/test.html",{})

def Reg(request):
    return render(request,"users/reg.html",{})