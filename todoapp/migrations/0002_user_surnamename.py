# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='surnamename',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
