# Generated by Django 4.1.1 on 2022-09-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_project_project_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
