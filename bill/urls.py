from django.urls import path

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('sell/',auth_views.LoginView.as_view(template_name='bill/sell.html'),name='sell'),


]