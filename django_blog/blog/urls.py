from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blog/', views.homepage, name='blog-homepage'),
]