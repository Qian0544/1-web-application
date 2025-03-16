
from django.urls import path,include
 # Import the view from your app
from . import views
urlpatterns = [
    path("", views.index),
    path("category/<int:category_id>",views.category,name="category"),
    path("post/<int:post_id>", views.post,name="post"),
]