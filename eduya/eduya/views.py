# Python first
# Django second
# Your apps
# Local apps


from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
<<<<<<< HEAD
from .models import Student 


# Create your views here.
def register(request):
    
    
#sendmail(subject, message, from_email, to_list, fail_silently=True)
def conf(request):
    
    form = 
    
    if form.is_Valid();
        save_it = form.save(commit=False)
        save_it.save();
        
        subject = 'Thank you for registering with eduya'
        message = 'Welcome to eduya! Please confirm your email address at the following link.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        messages.success(request, 'Thank you for registering, please check your email for a confirmation link.')
        return HttpResponseRedirect('/Thank-you/')
    return render("thankyou.html", locals(), context_instance=RequestContext(request))
	
=======
from django.http import HttpResponse

def index(request):
    # TODO: Link this to index.html/homepage route
    return HttpResponse('Index')
>>>>>>> c576ab931976ad0304130c12a26f08c82102bf4c
