from django.urls import path
from . views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('test/',Test,name='test'),
    path('reg/',Reg,name="register"),

]