from django.shortcuts import render
from .models import Project, Category, Subcategory, Skill
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render


def home(request):
    latest_projects = Project.objects.order_by("-created_at")[:4]
    context = {"latest_projects": latest_projects}
    return render(request, "portfolio/home.html", context)


def about(request):
    return render(request, "portfolio/about.html")


def skills(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "portfolio/skills.html", context)


def categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "portfolio/categories.html", context)


def category_details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {"category": category}
    return render(request, "portfolio/category_details.html", context)


def category_skills(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    skills = Skill.objects.filter(subcategories__category=category)

    context = {"category": category, "skills": skills}

    return render(request, "portfolio/category_skills.html", context)


def category_subcategories(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategory_set.all()
    return render(
        request,
        "portfolio/category_subcategories.html",
        {"category": category, "subcategories": subcategories},
    )


def skill_details(request, pk):
    skill = Skill.objects.get(pk=pk)
    subcategories = skill.subcategories.all()
    categories = Category.objects.filter(subcategory__in=subcategories).distinct()
    context = {
        "skill": skill,
        "categories": categories,
    }
    return render(request, "portfolio/skill_details.html", context)


def subcategory_details(request, category_id, subcategory_id):
    category = Category.objects.get(pk=category_id)
    subcategory = Subcategory.objects.get(pk=subcategory_id)
    return render(
        request,
        "portfolio/subcategory_details.html",
        {"category": category, "subcategory": subcategory},
    )


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "portfolio/projects.html", context)


def project_details(request, pk):
    project = Project.objects.get(pk=pk)

    # Segmenter la chaîne de caractères en sous-titres et descriptions
    segments = project.description.split("#%")
    subtitles = []
    descriptions = []
    for segment in segments:
        if "%#" in segment:
            subtitle, description = segment.split("%#")
            subtitles.append(subtitle.strip())
            descriptions.append(description.strip())
    categories = project.categories.all()
    subcategories = project.sub_categories.all()
    skills = project.skills.all()
    context = {
        "project": project,
        "subtitles": subtitles,
        "descriptions": descriptions,
        "categories": categories,
        "subcategories": subcategories,
        "skills": skills,
    }
    return render(request, "portfolio/project_details.html", context)


def skill_projects(request, skill_id):
    skill = Skill.objects.get(pk=skill_id)
    projects = skill.project_set.all()
    context = {"skill": skill, "projects": projects}
    return render(request, "portfolio/skill_projects.html", context)


def contact(request):
    if request.method == "POST":
        email = request.POST["email"]
        message = request.POST["message"]
        send_mail(
            "Un message du site",
            message,
            email,
            ["gianni@de-vadder.com"],
            fail_silently=False,
        )
        return render(request, "portfolio")
    return render(request, "portfolio/contact.html")
