# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_basket_basketitem_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 1, 26, 19, 11, 41, 449000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Przyj\xc4\x99te'), (2, b'W trakcie realizacji'), (3, b'Wys\xc5\x82ane'), (4, b'Zako\xc5\x84czone'), (5, b'Anulowane')]),
        ),
    ]
