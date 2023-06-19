from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from app.models import *
from app.serialization import *
from rest_framework.response import Response
from rest_framework import status
@api_view()

def Employeedata(request):
    EQS=Employee.objects.all()
    ESD=EmployeeMS(EQS,many=True)
    return Response(ESD.data)
    
    
    