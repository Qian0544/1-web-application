"""
URL configuration for BlogProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import add_category




urlpatterns = [
    path("post/<int:pid>/",views.BlogPost,name="blog_post"),
    path("",views.BlogMain),
    path("category/<int:cid>/",views.BlogCategory),
    path("contact",views.ContactView),
    path("feedbackthanks",views.FeedbackThanksView),
    path("contact/edit/<int:contact_id>",views.ContactEditView,name="contact_edit"),
    path('category/add/', add_category, name='add_category'),
]
