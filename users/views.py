from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import SignUpForm,User_Extended_Form
from django.contrib.auth.models import User
from .models import user_extended

from django.views.generic import UpdateView

# Error 404 modules
# from django.shortcuts import render_to_response
# from django.template import RequestContext


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
            db = user_extended()    # DB object
            form_username = form.cleaned_data.get('username') #Catching form1's username
            xuser = User.objects.get(username=form_username) #searching the user
            # Initialising the fields
            db.user = xuser 
            db.access_level = access_level
            db.mobile = phone
            db.address = address
            #saving all the changes in User_Extended model
            db.save()

            #redirection when there's queued route
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('register')

    else:
        form = SignUpForm()
    context = {'form':form,}
    return render(request,'users/reg.html',context)
        

def Settings(request):
    return render(request,"users/settings.html",{})

def Tools(request):
    return render(request,'users/tools.html',{})

def Manage_Staff(request):
    return render(request,"users/manage_staff.html",{})

def Edit_Permission(request):
    users = User.objects.all()
    return render(request,"users/edit_permission.html",{'users':users})


def ErrorPage(request,error):
    if len(error)<1:
        error = "No Thrown error"
    return render(request,"users/error.html",{'error':error})


def Access_Edit(request,user_id):
    try:
        xuser = user_extended.objects.get(user=user_id)
        if(request.method=='GET'):
            form = User_Extended_Form(instance=xuser)
        else:
            form = User_Extended_Form(request.POST,instance=xuser)
            form.save()
            form = User_Extended_Form
        context = {'form':form,'user':xuser}
        return render(request,"users/access_edit.html",context)
    except:
        print("HERE\n\n")
        try:
            super_user = User.objects.get(pk=user_id)
        except:
            return ErrorPage(request,"No User with this id")
        user_extended.objects.create(user=super_user)
        
        return Access_Edit(request,user_id)
        
    
    return render(request,"users/access_edit.html",{})
    
    
def User_List_Del(request):
    users = User.objects.all()
    return render(request,"users/user-list-del.html",{'users':users})
    
def Delete_Staff(request,user_id):
    try:
        extended_user = user_extended.objects.get(user=user_id)
    except:
        return ErrorPage(request,"No user with this id, in extended model")
    try:
        User_object = User.objects.get(pk=user_id)
    except:
        return ErrorPage(request,"No user with this id, in User model")
    extended_user.delete()
    User_object.delete()
    return redirect('manage_staff')