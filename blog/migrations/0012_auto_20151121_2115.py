# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20151121_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='post',
            field=models.ForeignKey(related_name='post_emailmessages', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='sender',
            field=models.ForeignKey(related_name='sender_emailmessages', to=settings.AUTH_USER_MODEL),
        ),
    ]
