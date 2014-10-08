# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0010_taskuser_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskuser',
            name='user_id',
        ),
    ]
