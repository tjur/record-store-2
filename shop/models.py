# -*- coding: utf-8 -*-
from django.db import models
from validators import validate_year
from django.contrib.auth.models import User

# Create your models here.

class Artist(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)

    def __unicode__(self):
       return self.name


class Genre(models.Model):
    name = models.CharField(null=False, blank=False, max_length=30)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, null=False, blank=False, verbose_name="Artysta")
    genre = models.ForeignKey(Genre, null=False, blank=False, verbose_name="Gatunek")
    name = models.CharField(null=False, blank=False, max_length=30, verbose_name="Album")
    year = models.CharField(null=False, blank=False, max_length=4, validators=[validate_year], verbose_name="Rok wydania")
    cover = models.CharField(null=False, blank=False, max_length=200, default="/static/images/covers/question_mark.jpg", verbose_name="Okładka")
    price = models.DecimalField(null=False, blank=False, max_digits=6, decimal_places=2, verbose_name="Cena")
    desc = models.TextField(default="Brak opisu", verbose_name="Opis")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Liczba w magazynie")

    def __unicode__(self):
        return self.name

    def image_tag(self):
        return u'<img width="150" height="150" src="%s" />' % self.cover

    image_tag.short_description = 'Cover image'
    image_tag.allow_tags = True


class BasketItem(models.Model):
    basket = models.ForeignKey("Basket", null=False, blank=False)
    album = models.ForeignKey("Album", null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)


class Basket(models.Model):
    user = models.ForeignKey(User)


class OrderItem(models.Model):
    order = models.ForeignKey("Order", null=False, blank=False)
    album = models.ForeignKey("Album", null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)


class Order(models.Model):
    ACCEPTED = 1
    IN_PROGRESS = 2
    SHIPPED = 3
    COMPLETED = 4
    CANCELED = 5
    STATUS_CHOICES = (
        (ACCEPTED, 'Przyjęte'),
        (IN_PROGRESS, 'W trakcie realizacji'),
        (SHIPPED, 'Wysłane'),
        (COMPLETED, 'Zakończone'),
        (CANCELED, 'Anulowane'),
    )

    user = models.ForeignKey(User)
    status = models.IntegerField(null=False, blank=False, choices=STATUS_CHOICES, default=ACCEPTED)
    start_date = models.DateField(null=False, blank=False, auto_now_add=True)
    amount = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2)

    def __unicode__(self):
        return "Order #" + str(self.id)