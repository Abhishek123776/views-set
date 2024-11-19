from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from . models import Employee
from . serializers import EmpSerializer
# Create your views here.

class EmployeeViewset(viewsets.ViewSet):
    def create(self,request):
        serializer=EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def list(self,request):
        objs=Employee.objects.all()
        serializer=EmpSerializer(objs,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,pk=None):
        obj=get_object_or_404(Employee,id=pk)
        serializer=EmpSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Employee,id=pk)
        serializer=EmpSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Employee,id=pk)
        serializer=EmpSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Employee,id=pk)
        obj.delete()
        return Response(data={"msg":'DATA DELETED SUCCESSFULY'})