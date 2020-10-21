from rest_framework import serializers
from bill.models import *


class Bill_ViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bill_Retailer
        fields = '__all__'
