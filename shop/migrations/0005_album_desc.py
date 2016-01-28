# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160125_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='desc',
            field=models.TextField(default=b'Brak opisu'),
        ),
    ]
