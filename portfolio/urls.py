from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("skills/", views.skills, name="skills"),
    path("categories/", views.categories, name="categories"),
    path(
        "categories/<int:category_id>/",
        views.category_details,
        name="categories_details",
    ),
    path(
        "categories/<int:category_id>/skills/",
        views.category_skills,
        name="category_skills",
    ),
    path(
        "categories/<int:category_id>/subcategories/",
        views.category_subcategories,
        name="category_subcategories",
    ),
    path(
        "categories/<int:category_id>/subcategories/<int:subcategory_id>/",
        views.subcategory_details,
        name="subcategory_details",
    ),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:pk>/", views.project_details, name="project_details"),
    path("skills/<int:pk>/", views.skill_details, name="skill_details"),
    path(
        "skills/<int:skill_id>/projects/", views.skill_projects, name="skill_projects"
    ),
    path("contact/", views.contact, name="contact"),
]
