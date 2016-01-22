from django.db import models
from validators import validate_year 

# Create your models here.

class Artist(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)


class Genre(models.Model):
    name = models.CharField(null=False, blank=False, max_length=30)


class Album(models.Model):
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre)
    name = models.CharField(null=False, blank=False, max_length=30)
    year = models.CharField(null=False, blank=False, max_length=4, validators=[validate_year])
    cover = models.ImageField(upload_to="covers/", default="covers/question_mark.jpg")
    price = models.DecimalField(null=False, blank=False, max_digits=6, decimal_places=2)
