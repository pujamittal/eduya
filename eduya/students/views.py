from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return HttpResponse('Register Page')

def login(request):
    return HttpResponse('Login Page')

def reset(request):
    return HttpResponse('Reset Page')
