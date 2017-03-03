from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from .forms import loginForm, registerForm
from .models import Student

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
        message = 'Welcome to eduya! Please confirm your email address at the following link.'
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
        return HttpResponseRedirect('/')
    
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
    
    
def logoutUser(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return HttpResponseRedirect('/')

def reset(request):
    return render(request, 'students/reset.html')
    
def my_profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
        
    context = {'user': request.user}
        
    return render(request, 'students/user_profile.html', context)
    
def all_tutors(request):
    tutors = Student.objects.all().filter(is_tutor=True)
    context = { 'tutors': tutors }
    return render(request, 'students/tutors.html', context)
    
def individual_tutor(request, tutor_id):
    try:
        tutor = Student.objects.get(is_tutor=True, pk=tutor_id)
        context = {'tutor' : tutor}
    except Student.DoesNotExist:
        return HttpResponseNotFound('<h1>Tutor not found</h1>')
        
    return render(request, 'students/tutor_profile.html', context)