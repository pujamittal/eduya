from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from courses.models import *
import datetime

# Create your views here.
def all_courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courses.html', context)

def course(request, course_id):
    course = Course.objects.get(course_id=course_id)
    context = {'course': course}
    return render(request, 'courses/course.html', context)

def all_sections(request, course_id):
    course_sections = CourseSection.objects.all().filter(course=course_id)
    context = {'course_sections' : course_sections}
    return render(request, 'courses/sections.html', context)

def section(request, course_id, course_section_id):
    section = CourseSection(pk=course_section_id)
    context = {'section' : section}
    return render(request, 'courses/section.html', context)


# TODO: route functions below
def all_professors(request):
    return HttpResponse('all professors')
    
def professor(request, professor_id):
    return HttpResponse('professor %s' % professor_id)
    
def professor_reviews(request, professor_id):
    return HttpResponse('professor %s reviews' % professor_id)
