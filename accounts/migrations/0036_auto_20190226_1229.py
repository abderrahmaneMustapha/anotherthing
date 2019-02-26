# Generated by Django 2.1.6 on 2019-02-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20190225_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='badge_logo/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='quizzes',
            field=models.ManyToManyField(blank=True, related_name='quize_student', through='accounts.TakenQuiz', to='accounts.Quiz'),
        ),
    ]
