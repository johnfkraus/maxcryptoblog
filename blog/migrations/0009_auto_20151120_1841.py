# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151120_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='message_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
