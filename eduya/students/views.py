from __future__ import division
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404

from .forms import loginForm, registerForm #, reviewForm
from .models import Student, Tutor, Review, TutorCourse, Course, Subject, MyCourse


# Create your views here.
def registerUser(request):
    #If you're already logged in
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/profile')
    
    form = registerForm(request.POST or None)
    
    #If your submission is valid and email is not taken
    if form.is_valid():
        newStudent = Student.objects.create_user(email=form.cleaned_data['email'], 
        password=form.cleaned_data['password'], 
        first_name=form.cleaned_data['first_name'], 
        last_name=form.cleaned_data['last_name'],
        is_tutor=form.cleaned_data['is_tutor'])
        newStudent.save()
        # Used to send email
        subject = 'Thank you for registering with eduya'
        message = 'Welcome to eduya! Your account is now active.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [newStudent.email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        #login(request, newStudent);    
        messages.success(request, 'Success! Your account was created.')
        return HttpResponseRedirect('/login')

    #if the form is not valid or the email is taken
    messages.error(request, 'Error: invalid form.')
    return render(request, 'students/register.html')
    

def loginUser(request):
    #If you're already logged in
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/profile')
    
    form = loginForm(request.POST or None)
    
    #If your submission is valid
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, 'Welcome '+ (user.first_name) + ' !')
            login(request, user)
            return HttpResponseRedirect('/profile') #change to user profile url
        else:
            messages.warning(request, 'Invalid username or password.')
    
    #if the form is not valid or the password is incorrect
    messages.error(request, 'Error: invalid form.')
    return render(request, 'students/login.html')

def temp(request):
    return render(request, 'students/tutor_review.html')

def reviewTutor(request, tutor_id, tutor_id2):
    if request.user.is_authenticated():
        if request.method == 'POST':
            #form = reviewForm(request.POST)
            #if form.is_valid():
            #if not str(request.POST.get('subject'))
            tutorID = str(request.path)
            tutorID = str(tutorID[tutorID.find("review") + 7:]) #extract tutor number from url of form /tutors/tutor_id/reviews/tutor_id/
            Skills = float(request.POST.get('Skills'))
            Prices = float(request.POST.get('Prices'))
            notes = str(request.POST.get('notes'))
            tutorToChange = Tutor.objects.get(pk=tutorID)
            tutorToChange.skillRating = float(((tutorToChange.numRatings*tutorToChange.skillRating)+Skills)/(tutorToChange.numRatings + 1))
            tutorToChange.moneyRating = float(((tutorToChange.numRatings*tutorToChange.moneyRating)+Prices)/(tutorToChange.numRatings + 1))
            tutorToChange.numRatings = tutorToChange.numRatings + 1
            #print tutorToChange.skillRating
            tutorToChange.save()
            newReview = Review.objects.create(tutor=Tutor.objects.get(pk=tutorID), reviewer_name = request.user.get_long_name(), skillRating = Skills, moneyRating = Prices, notes = notes);
            newReview.save()
            messages.success(request, 'Success! Your review has been posted.')
            return HttpResponseRedirect('/tutors')
        else:
            #tutors = Student.objects.all().filter(is_tutor=True)
            #args = {'tutors': tutors}
            args = {'tutors': Tutor.objects.get(pk=tutor_id)}
            return render(request, 'students/tutor_review.html', args)
    else:
        return HttpResponseRedirect('/login')

def logoutUser(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return HttpResponseRedirect('/')

def reset(request):
    return render(request, 'students/reset.html')
    
def add_course_to_student(request, subject_id, course_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    student = Student.objects.all().filter(email=request.user)[0]
    
    student_exists = len(MyCourse.objects.all().filter(course=course, student=student))
    if student_exists == 0:
        s = MyCourse()
        s.course = course
        s.student = student
        s.save()
    return redirect('/subjects/%s/courses/%s/' % (subject_id, course_id))
   
def remove_course_from_student(request, subject_id, course_id):
    subject = Subject.objects.all().get(abbreviation=subject_id)
    course = Course.objects.all().filter(subject=subject).filter(number=course_id)[0]
    student = Student.objects.all().filter(email=request.user)[0]
    
    student_exists = len(MyCourse.objects.all().filter(course=course, student=student))
    if student_exists == 0:
        s = MyCourse()
        s.course = course.delete()
        s.student = student
        s.save()
    return redirect('/subjects/%s/courses/%s/' % (subject_id, course_id))

def my_courses(request):
    try:
        student = Student.objects.get(pk=1)
        courses = MyCourse.objects.all().filter(student=student)
        context = {'courses': courses}
    except Student.DoesNotExist:
        return HttpResponseNotFound('<h1>Student not found</h1>')
    return render(request, 'courses/my_courses_page.html', context)

def my_listings(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/my_listings')
   
# def posts(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/posts')
        
def courses(request):
    return HttpResponseRedirect('/courses')

def professors(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/professors')

def my_profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    else:
        context = {'user': request.user}
        currentUser = Student.objects.get(email = request.user.email)
        if currentUser.is_tutor == True:
            context = {'user': request.user, 'tutor': Tutor.objects.get(studentLink = currentUser)}
            return render(request, 'students/user_profile_isTutor.html', context)
        return render(request, 'students/user_profile.html', context)
    
def all_tutors(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            tutors = Student.objects.all().filter(is_tutor=True)
            if 'skillUp' in request.POST:
                tutors = tutors.order_by('first_name');
            elif 'skillDown' in request.POST:
                tutors = tutors.order_by('-first_name');
            args = {'tutors': tutors}
            return render(request, 'students/tutors.html', args)
        else:
            tutors = Student.objects.all().filter(is_tutor=True)
            args = {'tutors': tutors}
            return render(request, 'students/tutors.html', args)
            
    else:
        return HttpResponseRedirect('/login')
    
def individual_tutor(request, tutor_id):
    try:
        student = Student.objects.get(is_tutor=True, pk=tutor_id)
        tutor = Tutor.objects.get(studentLink=student)
        courses = TutorCourse.objects.all().filter(tutor=tutor)
        reviews = Review.objects.all().filter(tutor=tutor)
        context = {'tutor' : tutor, 'courses': courses, 'reviews': reviews}
    except Student.DoesNotExist:
        return HttpResponseNotFound('<h1>Tutor not found</h1>')
        
    return render(request, 'students/tutor_profile.html', context)
    
def update_profile(request):
    if request.user.is_authenticated():
        """
        user_id = request.user.id
        #int(request.GET.get('id'))
        user = Student.objects.filter(id=user_id)[0]
        
        form = updateForm(request.POST or None, instance=request.user)
        
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.password = form.cleaned_data['password']
            user.save()
            form.save()
            return HttpResponseRedirect('/profile')
        else:
            return render(request, 'students/edit_user.html')
        """
        if request.method == 'POST':
            p = request.user
            #p.email=str(request.POST.get('email'))
            p.first_name=str(request.POST.get('first_name'))
            p.last_name=str(request.POST.get('last_name'))
            p.save()
            if p.pk is not None:
                return HttpResponseRedirect('/profile/')
            else:
                return render(request, 'students/edit_user.html')
        else:
            return render(request, 'students/edit_user.html')
    else:
        return HttpResponseRedirect('/login')

def view_tutors(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if 'skillUp' in request.POST:
                tutors = Tutor.objects.all().order_by('skillRating', 'tutor_name');
            elif 'skillDown' in request.POST:
                tutors = Tutor.objects.all().order_by('-skillRating', 'tutor_name');
            elif 'moneyUp' in request.POST:
                tutors = Tutor.objects.all().order_by('moneyRating', 'tutor_name');
            elif 'moneyDown' in request.POST:
                tutors = Tutor.objects.all().order_by('-moneyRating', 'tutor_name');
            elif 'nameUp' in request.POST:
                tutors = Tutor.objects.all().order_by('tutor_name');
            elif 'nameDown' in request.POST:
                tutors = Tutor.objects.all().order_by('-tutor_name');
            else:
                tutors = Tutor.objects.all().order_by('tutor_name')
            args = {'tutors': tutors}
            return render(request, 'students/tutors.html', args)
        else:
            tutors = Tutor.objects.all().order_by('tutor_name')
            args = {'tutors': tutors}
            return render(request, 'students/tutors.html', args)
            
    else:
        return HttpResponseRedirect('/login')

def become_tutor(request):
    if request.user.is_authenticated():
        currentUser = Student.objects.get(email = request.user.email)
        currentUser.is_tutor = True
        currentUser.save()
        Tutor.objects.create(studentLink = currentUser, tutor_name = str(currentUser.first_name + currentUser.last_name))
        return HttpResponseRedirect("/profile")
            
    else:
        return HttpResponseRedirect('/login')