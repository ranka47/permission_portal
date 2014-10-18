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
                ('current_group', models.ForeignKey(to='auth.Group')),
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
                ('hierarchies', models.ManyToManyField(related_name=b'groups', to='auth.Group')),
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
