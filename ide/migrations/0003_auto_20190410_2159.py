# Generated by Django 2.1.6 on 2019-04-10 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0002_auto_20190408_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='code',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
