from django.urls import path
from .views import *

urlpatterns = [
    path('tools/cheque/',Cheque,name='cheque'),
]