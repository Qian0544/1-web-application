from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import * 
from .forms import *
from django.http import Http404
from .forms import CategoryForm

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save category to the database
            return redirect('/blog/')  # Redirect to homepage or category list
    else:
        form = CategoryForm()  # Display empty form

    return render(request, 'add_category.html', {'form': form})



# Create your views here.
def BlogPost(request, pid):
    postdb = get_object_or_404(Post, id=pid)
    postcat = postdb.categories.all()
    return render(request,"blogpost.html",
                  {
                      "post":postdb,
                      "postcategories":postcat,
                  })

def BlogMain(request):
    blogcat = Category.objects.all()
    postdb = Post.objects.order_by("published").filter(status__id=2)[:10]
    print(postdb)
    return render(request,"BlogMain.html",
                  {
                      "blogcat":blogcat,
                      "posts":postdb,
                  })

def BlogCategory(request,cid):
    catdb = get_object_or_404(Category, id=cid)
    catpost = catdb.posts.filter(status__id=2)
    #foundposts = (catpost.first!=None)
    return render(request,"BlogCategory.html",
                  {
                    "cat":catdb,
                    "catpost":catpost,
                    #"foundposts":foundposts,
                  })

#def ContactView(request):
#    if request.method=="POST":
#        cform=ContactForm(request.POST)
#        if(cform.is_valid()):
#            data=cform.cleaned_data
#            return redirect("feedbackthanks")
#        return render(request,"ContactView.html",
#                      {"contactform":cform})
#    cform=ContactForm()
#    return render(request,"ContactView.html",
#                      {"contactform":cform})

def ContactView(request):
    if request.method=="POST":
        cform=ContactMessageForm(request.POST)
        if(cform.is_valid()):
            cform.save()
            return redirect("feedbackthanks")
        return render(request,"ContactView.html",
                        {"contactform":cform})    
    cform=ContactMessageForm()
    return render(request,"ContactView.html",
                    {"contactform":cform})

def FeedbackThanksView(request):
    return render(request,"ThanksForFeedback.html")

def ContactEditView(request,contact_id):
    contact=get_object_or_404(ContactMessage,id=contact_id)
    if(request.method=="POST"):
        cform=ContactMessageForm(request.POST,instance=contact)
        if(cform.is_valid()):
            cform.save()
            return redirect("")
    else:
        cform=ContactMessageForm(instance=contact)
    return render(request,"ContactEdit.html",{
        "contactform":cform
    })

