from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,                               name="index"),
    path('about/', views.about,                         name="about"),
    path('porfolio/', views.porfolio,                   name="porfolio"),
    path('blog/', views.blog,                           name="blog"),
    path('contact/', views.contact,                     name="contact"),
    path('detail_blog/<slug:slug>', views.detail_blog,  name="detail")
]