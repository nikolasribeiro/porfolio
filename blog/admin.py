from django.contrib import admin
from .models import (
    Porfolio, 
    Blog, 
    Profile, 
    Skills,
    Category
)
from import_export import resources
from import_export.admin import ImportExportModelAdmin
 

## Import Export class for save data
class PorfolioResource(resources.ModelResource):
    class Meta:
        model = Porfolio

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog

class SkillsResource(resources.ModelResource):
    class Meta:
        model = Skills

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class PorfolioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name_project','github_url')
    resource_class = PorfolioResource


class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','author','published')
    resource_class = BlogResource


class SkillsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name_of_skill', 'skill_percent']
    resource_class = SkillsResource

class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name','full_name','profession']
    resource_class = ProfileResource

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['category_name']
    resource_class = CategoryResource


# Register your models here.
admin.site.register(Porfolio, PorfolioAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
