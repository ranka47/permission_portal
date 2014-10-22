# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0003_auto_20141007_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_department', models.CharField(max_length=100)),
                ('user_designation', models.CharField(max_length=100)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('purpose', models.TextField()),
                ('facilities_required', models.TextField()),
                ('level', models.IntegerField(default=1)),
                ('status', models.CharField(default=b'Pending', max_length=32)),
                ('done_level', models.IntegerField(default=0)),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('current_group', models.ForeignKey(to='auth.Group', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default=b' ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            field=models.ManyToManyField(to='auth.Group', through='Permission.TemplateGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='template_id',
            field=models.ForeignKey(to='Permission.Template'),
            preserve_default=True,
        ),
    ]
