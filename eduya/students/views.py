from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.user.is_authenticated(): #idk what this does
        return HttpResponseRedirect("/")
    
    form = RegisterForm(request.POST or None)
    
    if form.is_valid(): #probably needs some work
        new_student = MyUser.objects.create_user(email=form.cleaned_data['email'], 
        password=form.cleaned_data['password'], 
        fname=form.cleaned_data['fname'], 
        last_name=form.cleaned_data['lname']),
        new_user.is_tutor=form.is_tutor
        new_user.is_admin = False
        new_user.save()         
        login(request, new_user);   
        messages.success(request, 'Success! Your account was created.')
        return render(request, 'index.html')
    
    #if form isn't valid?
    context = { #todo, needs to be fleshed out
    }
    return render(request, 'put_index_here', context)

def login(request):
    return render(request, 'login.html')

def reset(request):
    return render(request, 'reset.html')