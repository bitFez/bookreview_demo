from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)
    fiction = models.BooleanField(default=False) # non-fiction by default
    pages = models.PositiveSmallIntegerField(blank=True)
    genre = models.CharField(max_length=30, blank=True)
    
