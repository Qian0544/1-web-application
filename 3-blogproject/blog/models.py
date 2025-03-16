from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, models.PROTECT)
    published = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.ForeignKey("Status", models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField()
    categories = models.ManyToManyField("Category", related_name="posts")

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return f"{self.author}: {self.title}"
