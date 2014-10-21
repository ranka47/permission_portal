# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0002_task_done_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_level',
            field=models.IntegerField(default=0),
        ),
    ]
