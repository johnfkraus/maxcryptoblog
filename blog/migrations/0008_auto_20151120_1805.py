# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='post',
            field=models.ForeignKey(to='blog.Post', related_name='emailmessages'),
        ),
    ]
