from django.shortcuts import render

# Create your views here.
from .models import Category

def homepage(request):
    categories = Category.objects.all()
    return render(request, 'homepage.html', {'categories': categories})