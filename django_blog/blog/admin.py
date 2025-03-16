from django.contrib import admin

# Register your models here.
from .models import Status, Category, Post

admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Post)
