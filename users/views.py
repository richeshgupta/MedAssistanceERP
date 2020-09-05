from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import SignUpForm

def home(request):
    return render(request,'users/index.html')
    
def Test(request):
    return render(request,"users/test.html",{})

def Reg(request):
    return render(request,"users/reg.html",{})

def Logout(request):
    logout(request)
    return render(request,"users/logged-out.html",{})

def Signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'users/reg.html',{'form':form})
        
