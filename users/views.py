from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import SignUpForm,User_Extended
from django.contrib.auth.models import User

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
        form2 = User_Extended(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()

            instance_username = form.cleaned_data.get('username')
            username_object = User.objects.filter(username=instance_username)[0]
            print("Id :",username_object)
            # form2.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')

    else:
        form = SignUpForm()
        form2 = User_Extended()
    return render(request,'users/reg.html',{'form':form,'form2':form2})


def Tools(request):
    return render(request,'users/tools.html',{})
        
def Settings(request):
    return render(request,"users/settings.html",{})