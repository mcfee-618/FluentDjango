from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def index1(request,name,age):
    return HttpResponse("name:{0} , age:{1}".format(name,age))

def index2(request,age):
    return HttpResponse("name:{0} , age:{1}".format("222",age))