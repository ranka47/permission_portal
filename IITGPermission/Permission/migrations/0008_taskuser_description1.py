# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0007_auto_20141007_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskuser',
            name='description1',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
    ]
