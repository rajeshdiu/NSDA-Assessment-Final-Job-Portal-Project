# Generated by Django 5.1.1 on 2024-10-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0023_seekerprofilemodel_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobmodel',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='seekerprofilemodel',
            name='skills',
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='skils',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplymodel',
            name='Apply_Image',
            field=models.ImageField(null=True, upload_to='Media/Job_Image'),
        ),
    ]
