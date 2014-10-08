# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0012_taskuser_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskuser',
            name='TaskGroup_id',
        ),
        migrations.AddField(
            model_name='taskgroup',
            name='task_id',
            field=models.ForeignKey(default=1, to='Permission.TaskUser'),
            preserve_default=False,
        ),
    ]
