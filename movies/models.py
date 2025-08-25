from django.db import models

from accounts.models import Customer


# Create your models here.

class FavoriteMovie(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=20, unique=True)
    year = models.CharField(max_length=10, null=True, blank=True)
    poster_url = models.URLField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title