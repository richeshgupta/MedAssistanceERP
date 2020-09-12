from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('',home,name='home'),
    path('',auth_views.LoginView.as_view(template_name='users/index.html'),name='home'),
    path('test/',Test,name='test'),
    path('reg/',Signup,name="register"),
    path('logout/',Logout,name='logout'),
    path('tools/',Tools,name='tools'),
    path('settings/',Settings,name='settings'),
    ]

