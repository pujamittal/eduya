from django.shortcuts import render
from django.http import HttpResponse, Http404
from models import Post

# Create your views here.
"""
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    try:
        print request.POST['subject'], request.POST['course'], request.POST['location'], 
        request.POST['datetime'], request.POST['price'], request.POST['notes']
        # TODO: Create the Post/Return any errors after User registration/sessions have been completed
    except KeyError:
        pass
    else:
        pass
<<<<<<< HEAD
    return render(request, 'post_index.html', context)
"""
=======
    return render(request, 'posts/index.html', context)
        
>>>>>>> e56a7d5f84fd0712831fac442a2a4b0879bd0803
def post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        context = {'post': post}
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'posts/detail.html', context)