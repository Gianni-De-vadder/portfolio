# Generated by Django 4.2.1 on 2023-05-24 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_remove_skill_subcategory_skill_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='subcategory',
            new_name='subcategories',
        ),
    ]