# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='hierarchies',
            field=models.ManyToManyField(related_name=b'groups', to=b'auth.Group', blank=True),
        ),
    ]
