from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Student
from .forms import registerForm

# Create your views here.
def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        new_student = MyUser.objects.create_user(email=form.cleaned_data['email'], 
        password=form.cleaned_data['password'], 
        fname=form.cleaned_data['fname'], 
        last_name=form.cleaned_data['lname']),
        new_user.is_tutor=form.is_tutor
        new_user.is_superuser = False
        new_user.save()         
        login(request, new_user);   
        messages.success(request, 'Success! Your account was created.')
        return render(request, 'index.html')
    
    #if form isn't valid?
    context = {
    }
    return render(request, 'put_index_here', context)
