from django.urls import path
from .views import *
urlpatterns=[
    path('create-wholeseller/',CreateWholeseller.as_view(),name='create-wholeseller'),
    
]