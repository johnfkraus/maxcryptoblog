# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151109_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='save_password',
            field=models.BooleanField(default=True),
        ),
    ]
