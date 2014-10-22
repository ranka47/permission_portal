# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_department', models.CharField(max_length=100)),
                ('user_designation', models.CharField(max_length=100)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('purpose', models.TextField()),
                ('facilities_required', models.TextField()),
                ('level', models.IntegerField(default=1)),
                ('status', models.CharField(max_length=32, default='Pending')),
                ('approved_or_denied_by', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('current_group', models.ForeignKey(null=True, to='auth.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default=' ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('number', models.PositiveSmallIntegerField()),
                ('group', models.ForeignKey(to='auth.Group')),
                ('template', models.ForeignKey(to='Permission.Template')),
            ],
            options={
                'ordering': ('number',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='template',
            name='groups',
            field=models.ManyToManyField(through='Permission.TemplateGroup', to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='template_id',
            field=models.ForeignKey(to='Permission.Template'),
            preserve_default=True,
        ),
    ]
