# Generated by Django 4.1.1 on 2022-09-18 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(help_text='Project title should not exceed 100 character.', max_length=100)),
                ('project_details', models.TextField(null=True)),
                ('project_total_target', models.IntegerField(null=True)),
                ('project_start_date', models.DateField(blank=True, null=True)),
                ('project_end_date', models.DateField(blank=True, null=True)),
                ('project_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='project/imgs')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
