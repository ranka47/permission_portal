# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0003_auto_20141006_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.RemoveField(
            model_name='template',
            name='permission_id',
        ),
        migrations.AlterField(
            model_name='task',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
