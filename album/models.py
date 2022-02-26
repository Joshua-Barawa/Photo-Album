from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)




