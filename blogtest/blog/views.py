from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import Category,Post


def index(request):
    categories=Category.objects.all()
    print(categories)
    return render(request, "blog/index.html", {"categories": categories})

def category(request, category_id):
    category=get_object_or_404(Category, id=category_id)
    #category=Category.objects.get(id=category_id)
    # posts=Post.objects.filter(categories=category)
    posts=category.posts.filter(status__title="Published")
    return render(request, "blog/category.html", {"category": category,"posts":posts})

def post(request,post_id):
    post=get_object_or_404(Post, id=post_id,status__title="Published")
    return render(request,'post.html',{"post":post})