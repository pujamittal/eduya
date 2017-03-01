from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # TODO: Link this to index.html/homepage route
    return HttpResponse('Index')