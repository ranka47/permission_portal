# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0005_auto_20141022_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='from_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='to_date',
            field=models.DateTimeField(),
        ),
    ]
