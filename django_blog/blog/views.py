from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Post

# Create your views here.

from django.http import HttpResponseRedirect

from .models import Category

def homepage(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    return render(request, 'homepage.html', {'categories': categories})

def blog_list(request):
    post=Post.objects.all()
    context={

        'blog_list':post

    }
    return render(request,'blog/blog_list.html',context)

def blog_detail(request,id):
    each_post=Post.objects.get(id=id)
    context={
        'blog_detail': each_post
    }
    return render(request,'blog/blog_detail,html',context)

def blog_delete(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post_list')