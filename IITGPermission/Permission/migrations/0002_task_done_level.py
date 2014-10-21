# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done_level',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
