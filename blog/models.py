from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150, default="")
    
    def __str__(self):
        return self.category_name


class Profile(models.Model):
    name                = models.CharField(max_length=250, default="")
    full_name           = models.CharField(max_length=350, default="")
    profile_image       = CloudinaryField("image")
    profession          = models.CharField(max_length=250, default="")
    living_addres       = models.CharField(max_length=250, default="")
    actual_mail         = models.CharField(max_length=250, default="")
    github_profile      = models.CharField(max_length=250, default="")
    linkedin_profile    = models.URLField(max_length=400, default="")

    def __str__(self):
        return self.full_name

class Skills(models.Model):
    name_of_skill = models.CharField(max_length=100, default="")
    skill_percent = models.CharField(max_length=3, default="")

    def __str__(self):
        return self.name_of_skill

class Porfolio(models.Model):
    name_project    = models.CharField(max_length=250, default="")
    github_url      = models.URLField(default="")
    img             = CloudinaryField('image')
    modal_id        = models.CharField(max_length=300, default="")
    short_desc      = models.CharField(max_length=128, default="")
    modal_desc      = models.TextField(default="")
    category        = models.ManyToManyField(Category, default="")

    def __str__(self):
        return self.name_project

class Blog(models.Model):
    title           = models.CharField(max_length=250, default="")
    slug            = models.SlugField(max_length=250, default="")
    author          = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    image           = CloudinaryField('image')
    description     = models.TextField(default="")
    content_of_blog = RichTextField()
    published       = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('published',)
    
    def __str__(self):
        return self.title
