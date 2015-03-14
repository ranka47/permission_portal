# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_department', models.CharField(max_length=100)),
                ('user_designation', models.CharField(max_length=100)),
                ('from_date', models.DateField()),
                ('from_time', models.TimeField()),
                ('to_date', models.DateField()),
                ('to_time', models.TimeField()),
                ('purpose', models.TextField()),
                ('facilities_required', models.TextField()),
                ('level', models.IntegerField(default=1)),
                ('status', models.CharField(max_length=32, default='Pending')),
                ('approved_or_denied_by', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('current_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default=' ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('template', models.ForeignKey(to='Permission.Template')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('number',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='template',
            name='users',
            field=models.ManyToManyField(through='Permission.TemplateUser', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='template_id',
            field=models.ForeignKey(to='Permission.Template'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='Permission.Task'),
            preserve_default=True,
        ),
    ]
