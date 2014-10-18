# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0005_auto_20141018_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='hierarchies',
            field=models.ManyToManyField(default=b'', related_name=b'groups', to=b'auth.Group'),
        ),
    ]
