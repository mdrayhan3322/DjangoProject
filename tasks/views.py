from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("welcome to the task management system")
def contact(request):
  return HttpResponse("<h1 style='color:red'>welcome to the contact pase <h1/>")