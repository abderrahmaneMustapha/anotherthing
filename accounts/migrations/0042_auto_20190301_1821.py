# Generated by Django 2.1.6 on 2019-03-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_auto_20190301_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlevel',
            name='name',
            field=models.IntegerField(choices=[(1, 'Novice'), (2, 'Apprentice'), (3, 'Trainee'), (4, 'Beginner'), (5, 'Amateur '), (6, 'Professional'), (7, 'Master'), (8, 'Wizard '), (9, 'Mage'), (10, 'White Mage'), (11, 'Regent'), (12, 'King')], default=1),
        ),
    ]