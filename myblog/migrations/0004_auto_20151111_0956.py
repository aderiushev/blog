# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20151111_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ts',
            field=models.DateTimeField(verbose_name='Date Created'),
        ),
    ]
