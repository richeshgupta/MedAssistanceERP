from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import SignUpForm,User_Extended
from django.contrib.auth.models import User
from .models import user_extended


def home(request):
    return render(request,'users/index.html')
    
def Test(request):
    return render(request,"users/test.html",{})

def Reg(request):
    return render(request,"users/reg.html",{})

def Logout(request):
    logout(request)
    return redirect('home')

def Signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            access_level=request.POST.get('access_level')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            db = user_extended()
            form_username = form.cleaned_data.get('username')
            xuser = User.objects.get(username=form_username)
            db.user = xuser
            db.access_level = access_level
            db.mobile = phone
            db.address = address
            db.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')

    else:
        form = SignUpForm()
        form2 = User_Extended()
    return render(request,'users/reg.html',{'form':form,'form2':form2})

    context = {'form':form,}
    return render(request,'users/reg.html',context)
        
def Settings(request):
    return render(request,"users/settings.html",{})

def Tools(request):
    return render(request,'users/tools.html',{})