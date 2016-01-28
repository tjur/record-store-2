# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20160125_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.CharField(default=b'/static/images/covers/question_mark.jpg', max_length=200),
        ),
    ]
