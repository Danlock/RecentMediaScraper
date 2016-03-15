from django.db import models

# Create your models here.
class Media_Base(models.Model):
    title = models.CharField(max_length=300)
    release_date = models.DateTimeField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)

class Movie(Media_Base):
    return

class TVShow(Media_Base):
    return

class Anime(Media_Base):
    return
