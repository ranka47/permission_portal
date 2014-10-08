# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0004_auto_20141007_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='task', max_length=255),
            preserve_default=False,
        ),
    ]
