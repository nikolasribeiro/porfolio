from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Porfolio(models.Model):
    name_project    = models.CharField(max_length=250, default="")
    github_url      = models.URLField(default="")
    img             = models.ImageField(upload_to="static/img")

    def __str__(self):
        return self.name_project

class Blog(models.Model):
    title           = models.CharField(max_length=250, default="")
    slug            = models.SlugField(max_length=250, default="")
    author          = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    image           = models.ImageField(upload_to="static/img/blog")
    description     = models.TextField(default="")
    content_of_blog = models.TextField(default="")
    published       = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('published',)
    
    def __str__(self):
        return self.title