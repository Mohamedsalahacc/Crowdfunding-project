# Generated by Django 4.1.1 on 2022-09-19 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_project_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_images',
        ),
    ]
