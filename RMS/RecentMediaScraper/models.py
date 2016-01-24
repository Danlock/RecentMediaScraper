from django.db import models
import json

# Create your models here.

class Movie(models.Model):
    posters = models.URLField()
    year = models.IntegerField()
    runtime = models.IntegerField()
    #abridged_cast
    cast = models.TextField()
    mpaa_rating = models.CharField(max_length=5)
    links = models.URLField()
    #id
    rt_id = models.IntegerField()
    #alternate_ids.imdb
    imdb_id = models.IntegerField()
    release_dates = models.DateField()
    title = models.CharField(max_length=50)
    #ratings.critics_score
    rt_rating = models.IntegerField()
    synopsis = models.TextField()

    #setter and getter for cast, which is a list of 
    #actor JSON objects, like so 
    #[ {"name": "Lily James", "characters": ["Ella"],"id": "771402472"},...]
    def setCast(self, x):
        self.cast = json.dumps(x)

    def getCast(self, x):
        return json.loads(self.cast)    
