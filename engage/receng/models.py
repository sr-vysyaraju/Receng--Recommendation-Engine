from __future__ import generator_stop
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#movie model
class Movie(models.Model):
   name = models.CharField(max_length=20)
   rating = models.DecimalField(max_digits=2, decimal_places=1)
   lang = models.CharField(max_length=10)
   poster = models.ImageField()
   
   #genre
   #stores the value to what extent the movie belongs to a certain genre
   action = models.IntegerField()
   comedy = models.IntegerField()
   drama = models.IntegerField()
   fantasy = models.IntegerField()
   horror = models.IntegerField()
   romance = models.IntegerField()
   scifi = models.IntegerField()
   thriller = models.IntegerField()

class Profile(models.Model):
   userid = models.IntegerField(default=0)
   #genres
   #stores the value to what extent the user likes a certain genre
   action = models.IntegerField()
   comedy = models.IntegerField()
   drama = models.IntegerField()
   fantasy = models.IntegerField()
   horror = models.IntegerField()
   romance = models.IntegerField()
   scifi = models.IntegerField()
   thriller = models.IntegerField()
   #langs
   #stores information if the language is preferred by the user
   telugu = models.BooleanField()
   hindi = models.BooleanField()
   english = models.BooleanField()
   #to-watch movies list
   to_watch = models.ManyToManyField(Movie)