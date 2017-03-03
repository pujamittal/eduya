# Python first
# Django second
# Your apps
# Local apps


from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from students.models import Student 
from django.http import HttpResponse

def index(request):
    # TODO: Link this to index.html/homepage route
    return render(request, 'index.html')


def confirm_email(request):
    subject = 'Thank you for registering with eduya'
    message = 'Welcome to eduya! Please confirm your email address at the following link.'
    from_email = settings.EMAIL_HOST_USER
    to_list = [Student.email, settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
        
    #return HttpResponseRedirect('/homepage/')
    #return render("homepage.html", locals(), context_instance=RequestContext(request))
	
