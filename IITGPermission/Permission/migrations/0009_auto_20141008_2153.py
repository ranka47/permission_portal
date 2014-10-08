# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Permission', '0008_taskuser_description1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskgroup',
            name='task_id',
        ),
        migrations.AddField(
            model_name='taskuser',
            name='TaskGroup_id',
            field=models.ForeignKey(default=1, to='Permission.TaskGroup'),
            preserve_default=False,
        ),
    ]
