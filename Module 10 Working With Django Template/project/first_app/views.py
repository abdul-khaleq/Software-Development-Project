from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("This is app/home page")
    return render(request, 'first_app/home.html')
