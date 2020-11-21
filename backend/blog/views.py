from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

#Agregar proyectos de forma dinamica
def porfolio(request):
    return render(request, 'blog/porfolio.html')

#Agregar articulos al blog de forma dinamica
def blog(request):
    return render(request, 'blog/blog.html')

def contact(request):
    return render(request, 'blog/contact.html')