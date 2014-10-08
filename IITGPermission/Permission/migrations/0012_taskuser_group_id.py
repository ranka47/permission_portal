# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0003_auto_20141007_2145'),
        ('Permission', '0011_remove_taskuser_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskuser',
            name='group_id',
            field=models.ForeignKey(default=1, to='auth.Group'),
            preserve_default=False,
        ),
    ]
