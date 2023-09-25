from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ArrayField(models.ForeignKey('Author', on_delete=models.CASCADE), blank=True, null=True)


