# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_emailmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='salt',
            field=models.BinaryField(default=b'AJ\xf6\x12\x970B\x82\x15\xd6\xea\x01\x81k0S'),
        ),
    ]
