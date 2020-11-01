from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('',auth_views.LoginView.as_view(template_name='users/index.html'),name='home'),
    path('test/',Test,name='test'),
    path('reg/',Signup,name="register"),
    path('logout/',Logout,name='logout'),
    path('tools/',Tools,name='tools'),
    path('settings/',Settings,name='settings'),
    path('change-pass/',ChangePassword,name='change-pass'),
    path('manage_staff/',Manage_Staff,name='manage_staff'),
    path('edit_permission/',Edit_Permission,name='edit_permission'),
    path('access_edit/<int:user_id>',Access_Edit,name='access_edit'),
    path('delete-staff/<int:user_id>',Delete_Staff,name='delete_staff'),
    path('user_list_del/',User_List_Del,name='user_list_del'),
    path('backup/',BackupPage,name='backup'),
    path('admin/',Super_Admin,name='super_admin'),
    path('reminders/',Reminders,name='reminders'),
    ]

