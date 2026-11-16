from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    descripion = models.TextField(max_length=1000, blank=True)
    pages = models.PositiveIntegerField(blank=True)
    genre = models.CharField(max_length=20, blank=True)
    fiction = models.BooleanField(default=False) # non-fiction by default
    
