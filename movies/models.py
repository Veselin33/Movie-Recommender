from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=20, unique=True)
    year = models.CharField(max_length=10, null=True, blank=True)
    poster = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title