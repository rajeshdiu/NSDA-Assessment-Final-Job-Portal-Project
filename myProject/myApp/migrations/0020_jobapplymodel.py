# Generated by Django 5.1.1 on 2024-10-24 04:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_alter_jobmodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobApplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resume', models.FileField(blank=True, max_length=200, null=True, upload_to='Media/Resume')),
                ('Cover', models.TextField(blank=True, null=True)),
                ('Skills', models.CharField(blank=True, max_length=200, null=True)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.jobmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]