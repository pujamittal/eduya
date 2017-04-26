from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from courses.models import *
from students.models import TutorCourse, Tutor, Student 
from django.contrib import messages
import datetime
import json
import ast

from students.forms import contributeForm
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
    course = ProfessorCourse.objects.all().get(professor=professor_id).course
    professor_comments = ProfessorComment.objects.all().filter(professor=professor).reverse()

    #subject_id = Course.objects.get(pk=course_id).subject.pk;
    #subject = Subject.objects.all().get(abbreviation=subject_id)
    #course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    
    context = {'course': course, 'professor': professor, 'professor_comments': professor_comments}
    
    return render(request, 'courses/professor_page.html', context)

def professor(request, subject_id, course_id, professor_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    professor = Professor.objects.all().get(pk=professor_id)
    professor_comments = ProfessorComment.objects.all().filter(professor=professor).reverse()
    context = {'course': course, 'professor': professor, 'professor_comments': professor_comments}
    
    return render(request, 'courses/professor_page.html', context)
    

def professor_direct_comment(request, professor_id):
    p = ProfessorComment()
    
    professor = Professor.objects.all().get(pk=professor_id)
    student = request.user
    text = str(request.POST.get('notes'))
    
    print professor, student, text
    
    p.professor = professor
    p.student = student
    p.text = text
    p.save()
    
    return redirect('/professors/%s/' % professor_id)
    

def contribute_information(request, subject_id, course_id):
    if request.method == 'POST':
        form = contributeForm(request.POST)
        subject = Subject.objects.all().get(abbreviation=subject_id)
        course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
        l = FileLinker()
        l.course = course
        l.typeOfInfo = str(request.POST.get('info_type'))
        l.infoLink = str(request.POST.get('url'))
        l.notes = str(request.POST.get('notes'))
        l.save()
        return HttpResponseRedirect('/my-courses')
    else:
        return render(request, 'courses/add_info.html')
        
def contributed_information(request, subject_id, course_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    contrib = FileLinker.objects.all().filter(course=course)
    context = {'filelink': contrib}
    return render(request, 'courses/user_urls.html', context)
    