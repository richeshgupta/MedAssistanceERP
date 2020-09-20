from django.contrib.auth.decorators import user_passes_test
from .models import user_extended
from django.shortcuts import render



def is_admin_access(func):
    def _wrapper_(request,*args,**kwargs):

        if not request.user.is_anonymous:
            try:
                xuser = user_extended.objects.get(user=request.user)
                if xuser.access_level != 3 and xuser!=None:
                    return render(request,"users/error.html",{'error':"You don't have access to this page"})
                return func(request,*args,**kwargs)
            except:
                msg = "Some Error Occured, Maybe Your access Level is not updated, Kindly Contact Admin"
                return render(request,"users/error.html",{'error':msg})

        else:
            msg = "You are not signed in"
            return render(request,"users/error.html",{'error':msg})
    return _wrapper_

def is_intermediate_access(func):
    def _wrapper_(request,*args,**kwargs):

        if not request.user.is_anonymous:
            try:
                xuser = user_extended.objects.get(user=request.user)
                if xuser.access_level != 2 and xuser!=None:
                    return render(request,"users/error.html",{'error':"You don't have access to this page"})
                return func(request,*args,**kwargs)
            except:
                msg = "Some Error Occured, Maybe Your access Level is not updated, Kindly Contact Admin"
                return render(request,"users/error.html",{'error':msg})

        else:
            msg = "You are not signed in"
            return render(request,"users/error.html",{'error':msg})
    return _wrapper_