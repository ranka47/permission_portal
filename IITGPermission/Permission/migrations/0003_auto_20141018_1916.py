# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0002_auto_20141018_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='hierarchies',
            field=models.ManyToManyField(related_name=b'groups', null=True, to=b'auth.Group'),
        ),
    ]
