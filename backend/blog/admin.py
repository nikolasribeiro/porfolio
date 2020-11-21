from django.contrib import admin
from .models import Porfolio, Blog

class PorfolioAdmin(admin.ModelAdmin):
    list_display = ('name_project','github_url')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','published')

# Register your models here.
admin.site.register(Porfolio, PorfolioAdmin)
admin.site.register(Blog, BlogAdmin)