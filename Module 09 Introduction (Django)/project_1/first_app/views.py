from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is app/home page")

def courses(request):
    return HttpResponse("This is app/course page")

def about(request):
    return HttpResponse("This is app/about page")
