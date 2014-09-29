# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20140925_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='author',
            field=models.CharField(default=b'Incognito', max_length=100),
            preserve_default=True,
        ),
    ]
