# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0008_auto_20141018_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='hierarchy_5',
            field=models.CharField(default=1, max_length=32, blank=True),
            preserve_default=False,
        ),
    ]
