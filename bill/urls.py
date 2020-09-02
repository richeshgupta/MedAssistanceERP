from django.urls import path
from .views import Sale

urlpatterns = [
    path('sale/',Sale,name='sale'),


]