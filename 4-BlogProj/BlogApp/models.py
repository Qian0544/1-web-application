from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User, models.SET_NULL, blank=True,null=True)
    published=models.DateTimeField()
    title=models.CharField(max_length=255)
    content=models.TextField()
    status=models.ForeignKey('Status', models.SET_NULL,blank=True,null=True)
    categories=models.ManyToManyField("Category", related_name="posts")
    def __str__(self):
        return(f"\"{self.title}\", author: {self.author}")

class Status(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return(self.title)

class Category(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return(self.title)
    class Meta:
    	verbose_name_plural="Categories"

class ContactMessage(models.Model):
    createdat=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=123)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return(f"{self.name}\t{self.email}\t{self.createdat}")
