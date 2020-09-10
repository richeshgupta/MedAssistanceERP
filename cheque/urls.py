from django.urls import path
from .views import *

urlpatterns = [
    path('cheque/',Cheque,name='cheque'),
]