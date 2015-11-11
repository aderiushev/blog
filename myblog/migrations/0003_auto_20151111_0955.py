# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20151111_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ts',
            field=models.DateTimeField(verbose_name='ts created'),
        ),
    ]
