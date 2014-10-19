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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_department', models.CharField(max_length=100)),
                ('user_designation', models.CharField(max_length=100)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('purpose', models.TextField()),
                ('facilities_required', models.TextField()),
                ('current_group', models.ForeignKey(to='auth.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default=' ')),
                ('hierarchy_1', models.CharField(blank=True, max_length=32)),
                ('hierarchy_2', models.CharField(blank=True, max_length=32)),
                ('hierarchy_3', models.CharField(blank=True, max_length=32)),
                ('hierarchy_4', models.CharField(blank=True, max_length=32)),
                ('hierarchy_5', models.CharField(blank=True, max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='template_id',
            field=models.ForeignKey(to='Permission.Template'),
            preserve_default=True,
        ),
    ]
