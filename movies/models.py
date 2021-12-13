from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """
    used for movies categories
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    used for movies directors and casting
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    used for movies countries
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    used for represents movies
    """
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    plot = models.TextField()
    categories = models.ManyToManyField(Category)
    directors = models.ManyToManyField(Person, related_name='director')
    casts = models.ManyToManyField(Person, related_name='cast')
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])
