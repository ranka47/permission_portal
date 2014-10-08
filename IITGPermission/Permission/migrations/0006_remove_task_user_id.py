# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0005_auto_20141007_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user_id',
        ),
    ]
