from django.shortcuts import render
from users.custom_decorator import *
from .models import *
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='home') 
@is_admin_access
def Profile_page(request):
    if request.method=='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProfileForm()
        else:
            return ErrorPage(request,"Some error occurred!")
    else:
        form = ProfileForm()

    return render(request,"profile_retailer/profile.html",{'form':form})