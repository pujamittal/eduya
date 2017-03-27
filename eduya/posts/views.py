from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from posts.models import Post
import datetime

# Create your views here.

def index(request):
    if not request.user.is_authenticated(): 
        return HttpResponseRedirect('/login/')
        
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)
        
def new_post(request):
    if not request.user.is_authenticated(): 
        return HttpResponseRedirect('/login/')
        
    if request.method == 'POST':
        p = Post(
            student=request.user,
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
    return render(request, 'posts/detail.html', context)