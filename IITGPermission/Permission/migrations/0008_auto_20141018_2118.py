# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0007_auto_20141018_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='hierarchies',
        ),
        migrations.AddField(
            model_name='template',
            name='hierarchy_1',
            field=models.CharField(default=1, max_length=32, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='hierarchy_2',
            field=models.CharField(default=1, max_length=32, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='hierarchy_3',
            field=models.CharField(default=1, max_length=32, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='hierarchy_4',
            field=models.CharField(default=1, max_length=32, blank=True),
            preserve_default=False,
        ),
    ]
