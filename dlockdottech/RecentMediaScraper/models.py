from django.db import models
import json
# Create your models here.
# class Media_Base(models.Model):
#     class Meta:
#         abstract = True

class Movie(models.Model):
    title = models.CharField(max_length=300,default=" ")
    release_date = models.DateTimeField('date released',default=" ")
    popularity = models.DecimalField(max_digits=12, decimal_places=9,default=0.0)
    backdrop_path = models.CharField(max_length=50,default=" ")
    genre_ids = models.CommaSeparatedIntegerField(max_length=30,default=[])
    poster_path = models.CharField(max_length=50,default="")
    vote_average = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    media_id = models.PositiveIntegerField('id',default=1)
    adult = models.BooleanField('adult',default=False)
    vote_count = models.PositiveIntegerField('vote_count',default="0")
    original_language = models.CharField(max_length=3,default=" ")
    overview = models.TextField('overview',default=" ")

    def __str__(self):
        return self.title

#JSON_size structure = {'backdrop_sizes': ['w300', 'w780', 'w1280', 'original'],'poster_sizes': ['w92', 'w154', 'w185', 'w342', 'w500', 'w780', 'original']}
class Config(models.Model):
    singleton_enforce = models.PositiveIntegerField(default=1,unique=True)
    TMDB_baseurl = models.CharField(max_length=300,default=" ")
    TMDB_secureBaseurl = models.CharField(max_length=300,default=" ")
    TMDB_JSON_size = models.CharField(max_length=300,default=" ")

    def getImageSizes(self):
        return json.loads(self.TMDB_JSON_size)

    def __str__(self):
        return 'config'

# class TVShow(Media_Base):
#     lead_actors = models.CharField(max_length=300)

# class Anime(Media_Base):
#     animation_studio = models.CharField(max_length=50)
#     original_title = models.CharField(max_length=300)
