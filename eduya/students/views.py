from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    """
    if request.user.is_authenticated(): 
        return HttpResponseRedirect("/index.html") #idk if this works
    
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
        return render(request, 'login.html')
    
    #if form isn't valid?
    
    context = { #todo, needs to be fleshed out
    }
    return render(request, 'register.html', context)
    """
    return render(request, 'students/register.html')

def login(request):
    """
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if next_url is None:
        next_url = "/"
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, 'Success! Welcome, '+(user.first_name or ""))
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            messages.warning(request, 'Invalid username or password.')
    context = {
        "form": form,
        "page_name" : "Login",
        "button_value" : "Login",
        "links" : ["register"],
    }
    return render(request, 'auth_form.html', context)
    """
    return render(request, 'students/login.html')


def reset(request):
    return render(request, 'students/reset.html')