# Generated by Django 2.1.6 on 2019-03-22 20:50

import colorful.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),

        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('text', models.TextField()),
                ('video', models.URLField(blank=True)),
                ('file', models.FileField(blank=True, upload_to='content/file/')),
                ('image', models.ImageField(blank=True, upload_to='content/image/')),
                ('order', models.PositiveIntegerField(unique=True)),
                ('approved', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ContentNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=300)),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='content_note', to='course.Content')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_note', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, upload_to='courses_photos/')),
                ('approved', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_course', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('source', models.URLField(blank=True, default=None)),
                ('order', models.PositiveIntegerField(unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='modules_photos/')),
                ('approved', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_modules', to='course.Course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='subject_photos/')),
                ('approved', models.BooleanField(default=False)),
                ('color', colorful.fields.RGBColorField(default='#007bff')),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TakenContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_taken', to='course.Content')),
                ('module', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='content_module_taken', to='course.Module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_content', to='accounts.Student')),
            ],
        ),
        migrations.CreateModel(
            name='TakenCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_taken', to='course.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_course', to='accounts.Student')),
                ('subject', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='course_subject_taken', to='course.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='TakenModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(null=True)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='module_course_taken', to='course.Course')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_taken', to='course.Module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_module', to='accounts.Student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.Subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, related_name='tag_courses', to='accounts.Tag'),
        ),
        migrations.AddField(
            model_name='content',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='module_contents', to='course.Module'),
        ),
        migrations.AddField(
            model_name='content',
            name='question',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='question_contents', to='accounts.Question'),
        ),
    ]
