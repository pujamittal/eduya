# Python first
# Django second
# Your apps
# Local apps


from django.conf import settings
from django.core.mail import send_mail

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