# Generated by Django 5.1.1 on 2024-10-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0021_jobapplymodel_apply_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobmodel',
            name='skils',
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='skills',
            field=models.CharField(choices=[('programming', 'Programming'), ('sing', 'Sing'), ('paly', 'Play'), ('hr', 'HR')], max_length=100, null=True),
        ),
    ]