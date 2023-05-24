from django.contrib import admin
from .models import Skill, Project, Subcategory, Category


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
