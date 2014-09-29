# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='tagline',
            new_name='text',
        ),
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=datetime.date(2014, 9, 25)),
            preserve_default=False,
        ),
    ]
