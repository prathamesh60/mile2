from rest_framework import serializers
from .models import *

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields= ['id','ifsc_code', 'city', 'region']

class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model=LandingPageVisitor
        fields='__all__'