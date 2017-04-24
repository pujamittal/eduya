from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from posts.models import Post
import datetime

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if 'postTime' in request.POST:
                posts = Post.objects.all().order_by('-datetime', 'student_name');
            elif 'postTimeBack' in request.POST:
                posts = Post.objects.all().order_by('datetime', 'student_name');
            elif 'moneyUp' in request.POST:
                posts = Post.objects.all().order_by('price', 'student_name');
            elif 'moneyDown' in request.POST:
                posts = Post.objects.all().order_by('-price', 'student_name');
            elif 'nameUp' in request.POST:
                posts = Post.objects.all().order_by('student_name');
            elif 'nameDown' in request.POST:
                posts = Post.objects.all().order_by('-student_name');
            elif 'subjectUp' in request.POST:
                posts = Post.objects.all().order_by('subject');
            elif 'subjectDown' in request.POST:
                posts = Post.objects.all().order_by('-subject');
            elif 'courseUp' in request.POST:
                posts = Post.objects.all().order_by('course', 'student_name');
            elif 'courseDown' in request.POST:
                posts = Post.objects.all().order_by('-course', 'student_name');
            else:
                posts = Post.objects.all()
            args = {'posts': posts}
            return render(request, 'posts/listing_page.html', args)
        else:
            posts = Post.objects.all()
            args = {'posts': posts}
            return render(request, 'posts/listing_page.html', args)
            
    else:
        return HttpResponseRedirect('/login')
        
def new_post(request):
    if not request.user.is_authenticated(): 
        return HttpResponseRedirect('/login/')
        
    if request.method == 'POST':
        p = Post(
            student=request.user,
            student_name=str(request.user.get_long_name()),
            subject=str(request.POST.get('subject')),
            course=str(request.POST.get('course')),
            location=str(request.POST.get('location')),
            datetime=datetime.datetime.now(),
            price=float(request.POST.get('price')),
            notes=str(request.POST.get('notes'))
        )
        p.save()
        if p.pk is not None:
            return HttpResponseRedirect('/posts/')
        else:
            return render(request, 'posts/tutor_posting.html')
    else:
        return render(request, 'posts/tutor_posting.html')

        
def post(request, post_id):
    if not request.user.is_authenticated(): 
        return HttpResponseRedirect('/login/')
    
    try:
        post = Post.objects.get(pk=post_id)
        context = {'post': post}
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'posts/listing_profile.html', context)