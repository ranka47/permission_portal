# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('permission_type', models.CharField(max_length=32)),
                ('applicant', models.CharField(max_length=32)),
                ('date_of_application', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('special_mentions', models.TextField(blank=True)),
                ('required_files', models.FileField(blank=True, null=True, upload_to='files')),
                ('urgency', models.DateField(blank=True, null=True)),
                ('status', models.TextField()),
                ('status_description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='Permission.Task'),
        ),
    ]
