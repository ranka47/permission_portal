# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0003_auto_20141021_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comment',
            field=models.TextField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
