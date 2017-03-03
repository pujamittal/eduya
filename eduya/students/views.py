from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import messages

from .forms import loginForm, registerForm
from .models import Student

# Create your views here.
def registerUser(request):
    
    if request.user.is_authenticated(): 
        #return HttpResponseRedirect("/user/" + request.user.id) #TODO: Change to fit profile url format
        return HttpResponseRedirect('/logout')
    form = registerForm(request.POST or None)
    if form.is_valid(): #probably needs some work
        newStudent = Student.objects.create_user(email=form.cleaned_data['email'], 
        password=form.cleaned_data['password'], 
        first_name=form.cleaned_data['first_name'], 
        last_name=form.cleaned_data['last_name'],
        is_tutor=form.cleaned_data['is_tutor'])
        #newStudent.is_admin = False
        newStudent.save()         
        #login(request, newStudent);    
        messages.success(request, 'Success! Your account was created.')
        #return render(request, 'login.html', {'form': form})
        return HttpResponseRedirect('/')
    #else:
        #return HttpResponse('Fuck')
    #TODO: Figure out this context shit

    messages.error(request, 'Error: invalid form.')
    return render(request, 'register.html')
    

def loginUser(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, 'Welcome '+ (user.first_name) + ' !')
            login(request, user)
            return HttpResponseRedirect('/index.html')
        else:
            messages.warning(request, 'Invalid username or password.')
    
    #TODO: Figure out this context shit
    """
    context = {
        "form": form,
        "page_name" : "Login",
        "button_value" : "Login",
        "links" : ["register"],
    }
    return render(request, 'auth_form.html', context)
    """
    messages.error(request, 'Error: invalid form.')
    return render(request, 'login.html')
    
    
def logoutUser(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return HttpResponseRedirect('/')


def reset(request):
    return render(request, 'reset.html')
