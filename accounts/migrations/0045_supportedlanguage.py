# Generated by Django 2.1.6 on 2019-03-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_auto_20190315_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportedLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='supported_language/')),
            ],
        ),
    ]