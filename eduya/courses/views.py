from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from courses.models import *
from students.models import TutorCourse, Tutor, Student
import datetime
import json
import ast

# Create your views here.

def all_subjects(request):
    subjects = Subject.objects.all().order_by('abbreviation')
    context = {'subjects': subjects}
    return render(request, 'courses/subject_page.html', context)

def all_courses(request, subject_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    courses = Course.objects.all().filter(subject=subject).order_by('number')
    context = {'courses': courses}
    return render(request, 'courses/courses.html', context)

def course(request, subject_id, course_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    course_sections = CourseSection.objects.all().filter(course=course).order_by('crn')
    tutors = TutorCourse.objects.all().filter(course=course)
    professors = ProfessorCourse.objects.all().filter(course=course)
    teaching_assistants = TeachingAssistantCourse.objects.all().filter(course=course)

    for section in course_sections:
        meetings = []
        meetings_json = ast.literal_eval(section.meetings)
        for meeting in meetings_json:
            location = meetings_json[meeting]['Room']['BuildingCode'] + meetings_json[meeting]['Room']['RoomNumber']
            section.meetings = {'DaysOfWeek': meetings_json[meeting]['DaysOfWeek'], 'Location': location}
    context = {'course': course, 'course_sections': course_sections, 'tutors': tutors, 'professors': professors, 'teaching_assistants': teaching_assistants}
    return render(request, 'courses/course_profile.html', context)

def become_tutor_for_course(request, subject_id, course_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    tutor = Tutor.objects.all().filter(studentLink=request.user)[0]
    t = TutorCourse()
    t.tutor = tutor
    t.course = course
    t.save()
    return redirect('/subjects/%s/courses/%s/' % (subject_id, course_id))

# TODO: route functions below
def all_professors(request):
    return HttpResponse('all professors')
    
def professor(request, professor_id):
    return HttpResponse('professor %s' % professor_id)
    
def professor_reviews(request, professor_id):
    return HttpResponse('professor %s reviews' % professor_id)
