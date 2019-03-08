# Generated by Django 2.1.6 on 2019-02-28 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_course_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='takenmodule',
            name='source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, related_name='tag_courses', to='accounts.Tag'),
        ),
    ]
