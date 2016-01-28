# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_album_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Liczba w magazynie'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(verbose_name=b'Artysta', to='shop.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.CharField(default=b'/static/images/covers/question_mark.jpg', max_length=200, verbose_name=b'Ok\xc5\x82adka'),
        ),
        migrations.AlterField(
            model_name='album',
            name='desc',
            field=models.TextField(default=b'Brak opisu', verbose_name=b'Opis'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(verbose_name=b'Gatunek', to='shop.Genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'Album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.DecimalField(verbose_name=b'Cena', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.CharField(max_length=4, verbose_name=b'Rok wydania', validators=[shop.validators.validate_year]),
        ),
    ]
