from django.contrib import admin
from .models import Porfolio, Blog
from import_export import resources
from import_export.admin import ImportExportModelAdmin


## Import Export class for save data
class PorfolioResource(resources.ModelResource):
    class Meta:
        model = Porfolio

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog


class PorfolioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name_project','github_url')
    resource_class = PorfolioResource


class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','author','published')
    resource_class = BlogResource

# Register your models here.
admin.site.register(Porfolio, PorfolioAdmin)
admin.site.register(Blog, BlogAdmin)