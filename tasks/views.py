from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("welcome to the task management system")
def contact(request):
  return HttpResponse("<h1 style='color:red'>welcome to the contact pase <h1/>")
def about(request):
  return HttpResponse("My name is rayhan")
def prodect(request):
  return HttpResponse("alu,komola,labu,am")

# url path extra file 
def show_task(request):
  return HttpResponse("show task your pase ")
  
