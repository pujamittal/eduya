from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from courses.models import *
import datetime
import json
import ast

# Create your views here.

def all_subjects(request):
    subjects = Subject.objects.all().order_by('abbreviation')
    context = {'subjects': subjects}
    return render(request, 'courses/subjects.html', context)

def all_courses(request, subject_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    courses = Course.objects.all().filter(subject=subject).order_by('number')
    context = {'courses': courses}
    return render(request, 'courses/courses.html', context)

def course(request, subject_id, course_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    course_sections = CourseSection.objects.all().filter(course=course).order_by('crn')

    for section in course_sections:
        meetings = []
        meetings_json = ast.literal_eval(section.meetings)
        for meeting in meetings_json:
            location = meetings_json[meeting]['Room']['BuildingCode'] + meetings_json[meeting]['Room']['RoomNumber']
            section.meetings = {'DaysOfWeek': meetings_json[meeting]['DaysOfWeek'], 'Location': location}
    context = {'course': course, 'course_sections': course_sections}
    return render(request, 'courses/course_profile.html', context)

def section(request, course_id, course_section_id):
    # section = CourseSection(pk=course_section_id)
    # context = {'section' : section}
    return render(request, 'courses/section_profile.html')

# TODO: route functions below
def all_professors(request):
    return HttpResponse('all professors')
    
def professor(request, professor_id):
    return HttpResponse('professor %s' % professor_id)
    
def professor_reviews(request, professor_id):
    return HttpResponse('professor %s reviews' % professor_id)
