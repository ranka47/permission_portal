# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0002_auto_20141006_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('display_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('permission_id', models.ForeignKey(to='Permission.Permission')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='task',
            old_name='groups',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='task',
            name='approved',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateField(default=datetime.date(2014, 10, 6), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='template_id',
            field=models.ForeignKey(default=0, to='Permission.Template'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateField(default=datetime.date(2014, 10, 6), auto_now=True),
            preserve_default=False,
        ),
    ]
