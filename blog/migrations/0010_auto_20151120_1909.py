# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20151120_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='sender',
            field=models.ForeignKey(related_name='emailmessage_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
