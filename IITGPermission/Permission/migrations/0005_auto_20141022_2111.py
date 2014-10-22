# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0004_task_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='to_date',
            field=models.DateField(),
        ),
    ]
