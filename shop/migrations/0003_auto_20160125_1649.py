# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160125_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.URLField(default=b'/static/images/covers/question_mark.jpg'),
        ),
    ]
