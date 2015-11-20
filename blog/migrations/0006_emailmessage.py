# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('message_content', models.TextField(verbose_name='post.content')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('destin_email', models.CharField(max_length=200)),
                ('post', models.ForeignKey(to='blog.Post', related_name='emails')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='senders')),
            ],
        ),
    ]
