from django.shortcuts import render

# Create your views here.
def Profile_page(request):
    return render(request,"profile_retailer/profile.html",{})