# Generated by Django 4.2.1 on 2023-05-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_sub_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='skill',
            name='subcategory',
            field=models.ManyToManyField(to='portfolio.subcategory'),
        ),
    ]
