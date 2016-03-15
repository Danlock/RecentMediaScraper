from django.db import models

# Create your models here.
class Media_Base(models.Model):
    class Meta:
        abstract = True
    title = models.CharField(max_length=300)
    release_date = models.DateTimeField('date released')
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

class Movie(Media_Base):
    lead_actors = models.CharField(max_length=300)

class TVShow(Media_Base):
    lead_actors = models.CharField(max_length=300)

class Anime(Media_Base):
    animation_studio = models.CharField(max_length=50)
