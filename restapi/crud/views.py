from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
import datetime

# Create your views here.

@csrf_exempt
def bank_list(request):
    if request.method =='GET' :
        banks=Bank.objects.all();
        serializer=BankSerializer(banks,many=True);
        return JsonResponse(serializer.data, safe=False)
    if request.method =='POST' :
       data=JSONParser().parse(request)
       serializer = BankSerializer(data=data)
      
        
       if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
       return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def LandingPage(request):
    print("Running")
    if request.method== 'POST':
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.date()
        data1={"visit_time":current_time,"visit_date":current_date}
        serializer=LandingPageSerializer(data=data1);

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    
    if request.method =='GET' :
        landing=LandingPageVisitor.objects.all();
        serializer=LandingPageSerializer(landing,many=True);
        return JsonResponse(serializer.data, safe=False)
       
      






