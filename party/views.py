from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from .models import *

class CreateWholeseller(CreateView):
    model = Party_Wholeseller
    fields = ['name','address','city','state','gstin','dl_number','contact','pan_number']
    template_name='party/wholeseller.html'