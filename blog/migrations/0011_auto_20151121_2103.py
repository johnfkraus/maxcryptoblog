# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20151120_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='message_content',
            field=models.TextField(default='Empty'),
        ),
    ]
