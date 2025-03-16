from django.contrib import admin

from .models import Category, Post


admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "published"]
    filter_horizontal = ["categories"]


admin.site.register(Post, PostAdmin)
