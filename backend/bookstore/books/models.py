from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    acquired = models.BooleanField(default=False)
    published_year = models.CharField(max_length=120)

