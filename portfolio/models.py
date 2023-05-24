from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    subcategories = models.ManyToManyField(Subcategory)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="project_images/")
    categories = models.ManyToManyField(Category)
    sub_categories = models.ManyToManyField(Subcategory)
    skills = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
