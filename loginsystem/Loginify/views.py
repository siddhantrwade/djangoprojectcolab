from django.shortcuts import render

# Create your views here.

# Test view to check if everything is running fine

from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome to the Loginify app!')