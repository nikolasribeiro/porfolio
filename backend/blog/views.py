from django.shortcuts import render, HttpResponse
from .models import Porfolio, Blog


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

#Agregar proyectos de forma dinamica
def porfolio(request):
    projects = Porfolio.objects.all()

    context = {
        'projects':projects
    }

    return render(request, 'blog/porfolio.html', context)

#Agregar articulos al blog de forma dinamica
def blog(request):
    blogs = Blog.objects.all()

    context = {
        'blogs':blogs
    }

    return render(request, 'blog/blog.html', context)

def contact(request):
    return render(request, 'blog/contact.html')