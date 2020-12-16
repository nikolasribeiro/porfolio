from django.shortcuts import render, HttpResponse
from .models import Porfolio, Blog, Profile, Skills


# Create your views here.
def index(request):
    profile = Profile.objects.all()
    context = {
        "profile": profile
    }
    return render(request, 'blog/index.html', context)

def about(request):
    profile = Profile.objects.all()
    skills  = Skills.objects.all()


    context = {
        "profile":profile,
        "skills": skills
    }
    return render(request, 'blog/about.html', context)

#Agregar proyectos de forma dinamica
def porfolio(request):
    projects = Porfolio.objects.all()

    context = {
        'projects':projects
    }

    return render(request, 'blog/porfolio.html', context)

#Agregar articulos al blog de forma dinamica
def blog(request):
    blogs = Blog.objects.all().order_by('-published')

    context = {
        'blogs':blogs
    }

    return render(request, 'blog/blog.html', context)

def contact(request):
    return render(request, 'blog/contact.html')


def detail_blog(request, slug):
    posts = Blog.objects.get(slug=slug)
    context = {
        'posts':posts
    }
    return render(request, 'blog/detail_blog.html', context)