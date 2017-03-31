from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from courses.models import *
import datetime

# Create your views here.
def all_courses(request):
    return HttpResponse('all courses')

def course(request, course_id):
    return HttpResponse('course id:%s' % course_id)

def all_sections(request, course_id):
    return HttpResponse('all sections for course:%s' % course_id)
    
def section(request, course_id, course_section_id):
    return HttpResponse('section %s' % course_section_id)
    
def all_professors(request):
    return HttpResponse('all professors')
    
def professor(request, professor_id):
    return HttpResponse('professor %s' % professor_id)
    
def professor_reviews(request, professor_id):
    return HttpResponse('professor %s reviews' % professor_id)
