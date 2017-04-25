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
    return render(request, 'courses/courses_page.html', context)

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
    
    tutor_exists = len(TutorCourse.objects.all().filter(course=course, tutor=tutor))
    if tutor_exists == 0:
        t = TutorCourse()
        t.tutor = tutor
        t.course = course
        t.save()
    return redirect('/subjects/%s/courses/%s/' % (subject_id, course_id))


def professors(request):
    professors = Professor.objects.all()
    context = { 'professors': professors }
    return render(request, 'courses/professors.html', context)

def professor_direct(request, professor_id):
    professor = Professor.objects.all().get(pk=professor_id)
    course = ProfessorCourse.objects.all().get(professor=professor_id).course;
    #subject_id = Course.objects.get(pk=course_id).subject.pk;
    #subject = Subject.objects.all().get(abbreviation=subject_id)
    #course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    
    context = {'course': course, 'professor': professor }
    
    return render(request, 'courses/professor_page.html', context)

def professor(request, subject_id, course_id, professor_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    professor = Professor.objects.all().get(pk=professor_id)
    
    context = {'course': course, 'professor': professor }
    
    return render(request, 'courses/professor_page.html', context)
