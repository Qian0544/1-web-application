from django.contrib import admin

from .models import Post, Category, ContactMessage

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal=["categories"]
    list_display=["title","author","published"]

admin.site.register(Post,PostAdmin)

admin.site.register(Category)

admin.site.register(ContactMessage)
